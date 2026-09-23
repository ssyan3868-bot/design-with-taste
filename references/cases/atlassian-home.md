# Atlassian 首页：企业软件的产品集合导航

## 来源与观察边界
- 来源：https://www.atlassian.com/
- 来源性质：企业协作软件公司首页
- 整理：2026-09-20；初次浏览：2026-09-20
- 实际语言：英文
- 桌面范围：CSS 视口 1280×720；文档高度 19887px
- 观察对象：Hero、产品集合 Tab 区
- 证据载体：截图观察 + DOM 快照

## 已记录事实
- Hero 背景为纯白色，顶部导航包含 Products / Solutions / Why Atlassian / Resources / Enterprise。
- H1 "Unleash your teams and their agents" 约 48-56px（估算），Charlie Text 字体，黑色粗体，居中。"and" 用紫色高亮。
- 副文案 "Everyone. Working on the right things. In Jira, teams and AI agents plan, execute, and deliver outcomes together." 深灰色，居中。
- CTA "Get started with Jira" 为蓝色圆角按钮 + "Contact us" 文字链接。
- Hero 背景有极浅的网格线纹理（几乎不可见）。
- 下方为 Tab 导航（Teamwork / Strategy / Service / Software / Product），Teamwork 为黑色实心选中态。
- Tab 下方为 "Teamwork Collection" 章节，左文右图布局：左侧 "The teamwork platform for the AI era" + 说明文案，右侧为产品截图（含 Rovo AI 助手界面）。
- 字体：Charlie Text, system-ui；正文 16px。

## 解释与推断
- 居中 H1 + 紫色关键词高亮是 Atlassian 的品牌手法，在极简白色背景上制造焦点。
- 产品集合 Tab 让用户按工作类型（而非产品名）浏览，降低多产品线的认知成本。
- 极浅网格纹理增加背景层次，避免纯白过于平淡。
- 左文右图的产品展示与 Quicken 类似，但 Atlassian 的截图更侧重 AI 功能（Rovo）。
- 页面极长（19887px），说明内容量大，需良好的章节节奏。

## 多维标签
- 范围：企业产品/品牌营销
- 页面任务：多产品企业软件平台的导航与转化
- 叙事：品牌主张 → 产品分类 → 产品集合详情
- 布局：居中 Hero + Tab 切换 + 左文右图产品集合
- 字体：Charlie Text 约 48-56px H1 / 12px 小标签；正文 16px
- 图像：产品 UI 截图（含 AI 助手界面）
- 材质与色彩：纯白背景、黑色文字、蓝色 CTA、紫色关键词高亮、极浅网格纹理
- 状态证据：Hero + Tab 区已观察；后续章节未完整滚动

## 条件化迁移
- 当产品线复杂时，用工作类型 Tab（而非产品名）组织导航，降低认知成本。
  - 不适用于产品线简单或用户已熟悉产品名的场景。
- 紫色关键词高亮在黑色 H1 中制造焦点，适合需要强调连接词或转折的场景。
  - 不适用于关键词过多或高亮颜色与品牌不符的场景。
- 极浅网格纹理可在白色背景上增加层次，但需确保不影响文字可读性。
  - 不适用于纹理过强干扰内容的场景。

## 不照搬项与反例
- 不继承 Charlie Text 字体或具体字号。
- 紫色高亮是 Atlassian 品牌色，不泛化为通用强调色。
- Tab 的数量和标签需根据实际产品线调整，不固定为 5 个。

## 证据局限与后续核查
- Tab 切换行为未验证。
- 未测试移动端重排、键盘操作。
- 字体声明为 DOM 读取，实际渲染未二次确认。
- 网格纹理的精确颜色和密度未测量。
