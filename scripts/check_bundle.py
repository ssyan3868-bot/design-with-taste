#!/usr/bin/env python3
"""Check this skill's flat YAML metadata and local Markdown links, using stdlib.

Deliberately supports only single-line scalar frontmatter used by this package.
Does not validate external URLs, rendered design, or skill registration.
"""
import argparse
import json
from pathlib import Path
import re
import tempfile
from urllib.parse import unquote, urlsplit


NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")
UNFINISHED = re.compile(r"\b(?:TO" + r"DO|FIX" + r"ME)\s*:", re.I)


def without_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = value
            elif value[0] == fence[0] and len(value) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return "\n".join(lines)


def scalar(value):
    value = value.strip()
    if not value or value in {"|", ">", "null", "~"}:
        raise ValueError("must be a nonempty single-line scalar")
    if value.startswith('"'):
        result = json.loads(value)
        if not isinstance(result, str) or "\n" in result or "\r" in result:
            raise ValueError("must be a single-line string")
        return result
    if value.startswith("'"):
        if not value.endswith("'") or len(value) < 2:
            raise ValueError("unclosed single quote")
        return value[1:-1].replace("''", "'")
    if value.startswith(("[", "{", "&", "*", "!")) or ": " in value:
        raise ValueError("unsupported YAML syntax; quote scalar values")
    return value.split(" #", 1)[0].strip()


def check_index_cases_consistency(root, errors):
    """Two-way consistency: index references vs cases on disk."""
    index_path = root / "references" / "source-index.md"
    cases_dir = root / "references" / "cases"
    if not index_path.is_file() or not cases_dir.is_dir():
        return
    disk_cases = {p.name for p in cases_dir.glob("*.md")}
    referenced = set()
    try:
        text = index_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return
    for match in LINK.finditer(without_fences(text)):
        dest = match.group(1).strip("<>")
        parts = urlsplit(dest)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        if parts.path.startswith("cases/") and parts.path.endswith(".md"):
            referenced.add(Path(parts.path).name)
    for name in sorted(disk_cases - referenced):
        errors.append(f"source-index.md: case file not referenced: {name}")
    for name in sorted(referenced - disk_cases):
        errors.append(f"source-index.md: referenced case missing on disk: {name}")


def check(root):
    root = Path(root).resolve()
    errors = []
    entry = root / "SKILL.md"
    result = {"root": str(root), "ok": False, "errors": errors,
              "checks": "metadata, unfinished markers, local Markdown targets",
              "limitations": ["external URLs not fetched", "fragment anchors not checked",
                              "runtime and aesthetics not tested"]}
    if not entry.is_file():
        errors.append("SKILL.md missing")
        return result
    try:
        text = entry.read_text(encoding="utf-8")
        lines = text.splitlines()
        end = lines.index("---", 1) if lines and lines[0] == "---" else -1
        meta = {}
        if end < 1:
            errors.append("frontmatter must begin and end with ---")
        else:
            for line in lines[1:end]:
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                match = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
                if not match:
                    errors.append("frontmatter: only flat scalar fields are supported")
                    continue
                key, value = match.groups()
                if key in meta:
                    errors.append(f"frontmatter: duplicate {key}")
                try:
                    meta[key] = scalar(value)
                except (ValueError, json.JSONDecodeError) as exc:
                    errors.append(f"frontmatter {key}: {exc}")
            name = meta.get("name", "")
            if not NAME.fullmatch(name):
                errors.append("name must use lowercase hyphen-case")
            if name != root.name:
                errors.append("name must equal folder name")
            description = meta.get("description", "")
            if not description or len(description) > 1024:
                errors.append("description required and must be <=1024 characters")
            result["body_lines"] = len(lines[end + 1:])
            if result["body_lines"] >= 500:
                errors.append("SKILL.md body must be <500 lines")
        files = sorted(p for p in root.rglob("*") if p.is_file())
        result["files"] = len(files)
        result["bytes"] = sum(p.stat().st_size for p in files)
        result["case_files"] = len(list((root / "references" / "cases").glob("*.md")))
        check_index_cases_consistency(root, errors)
        for path in files:
            relative = path.relative_to(root)
            if path.suffix.lower() not in {".md", ".py", ".json", ".html", ".txt"}:
                continue
            content = path.read_text(encoding="utf-8")
            if UNFINISHED.search(content):
                errors.append(f"{relative}: unfinished marker")
            if path.suffix.lower() != ".md":
                continue
            for match in LINK.finditer(without_fences(content)):
                destination = match.group(1).strip("<>")
                parts = urlsplit(destination)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                target = (path.parent / unquote(parts.path)).resolve()
                if not target.is_relative_to(root):
                    errors.append(f"{relative}: local link escapes package: {destination}")
                elif not target.exists():
                    errors.append(f"{relative}: missing local target: {destination}")
        if len(errors) > 40:
            result["omitted_errors"] = len(errors) - 40
            del errors[40:]
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"cannot check package: {type(exc).__name__}: {exc}")
    result["ok"] = not errors
    return result


def self_test():
    tests = []
    base = '---\nname: fixture-skill\ndescription: "A test fixture"\n---\n\n# Test\n'
    with tempfile.TemporaryDirectory(prefix="taste-check-") as directory:
        root = Path(directory) / "fixture-skill"
        root.mkdir()
        entry = root / "SKILL.md"
        samples = [
            ("valid", base, True),
            ("missing-local-link", base + "[missing](missing.md)\n", False),
            ("wrong-name", base.replace("fixture-skill", "Wrong_Name"), False),
            ("duplicate-key", base.replace("name: fixture-skill", "name: fixture-skill\nname: fixture-skill"), False),
            ("long-description", base.replace("A test fixture", "x" * 1025), False),
            ("multiline-description", base.replace('"A test fixture"', "|\n  test"), False),
            ("long-body", base + "line\n" * 500, False),
            ("unfinished", base + "TO" + "DO: test\n", False),
            ("path-escape", base + "[outside](../outside.md)\n", False),
            ("external-and-fragment", base + "[web](https://example.com/) [here](#test)\n", True),
            ("fenced-example", base + "```md\n[example](missing.md)\n```\n", True),
        ]
        for label, content, expected in samples:
            entry.write_text(content, encoding="utf-8")
            report = check(root)
            tests.append({"test": label, "passed": report["ok"] == expected,
                          "detected_errors": report["errors"]})
        entry.unlink()
        tests.append({"test": "missing-entry", "passed": not check(root)["ok"]})

        # Index <-> cases consistency fixtures
        cases_dir = root / "references" / "cases"
        cases_dir.mkdir(parents=True, exist_ok=True)
        index_file = root / "references" / "source-index.md"
        # Case A: orphan on disk (file exists but not referenced)
        (cases_dir / "orphan.md").write_text("# orphan\n", encoding="utf-8")
        index_file.write_text("# Index\nNo case links here.\n", encoding="utf-8")
        entry.write_text(base, encoding="utf-8")
        report = check(root)
        tests.append({"test": "orphan-on-disk",
                      "passed": any("case file not referenced: orphan.md" in e for e in report["errors"])})

        # Case B: referenced but missing on disk
        index_file.write_text("# Index\n[missing](cases/missing.md)\n", encoding="utf-8")
        report = check(root)
        tests.append({"test": "referenced-missing",
                      "passed": any("referenced case missing on disk: missing.md" in e for e in report["errors"])})

        # Cleanup
        (cases_dir / "orphan.md").unlink()
        index_file.unlink()
        cases_dir.rmdir()
        (root / "references").rmdir()

    return {"ok": all(t["passed"] for t in tests), "tests": tests}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    report = self_test() if args.self_test else check(args.root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
