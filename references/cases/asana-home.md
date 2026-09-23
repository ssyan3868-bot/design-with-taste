# Asana 首页：超大字体的 AI 工作管理主张

## 来源与观察边界
- 来源：https://asana.com/
- 来源性质：工作管理/项目管理软件营销首页
- 整理：2026-09-20；初次浏览：2026-09-20
- 实际语言：英文
- 桌面范围：CSS 视口 1280×720；文档高度 8282px
- 观察对象：Hero、注册区、Accordion 内容区
- 证据载体：截图观察 + DOM 快照

## 已记录事实
- Hero 背景为纯白色，顶部导航包含 Products / Solutions / Learning & support / Pricing。
- H1 "AI that works across your teams" 约 102px，TWK Lausanne 字体，黑色，居中。字号极大，占据首屏主要空间。
- 副文案 "Asana is where humans and agents workflow together" 灰色，居中，约 20px。
- 下方为注册区：Google / Microsoft 社交登录按钮（白色圆角带边框）+ 邮箱输入框 + "Continue" 黑色按钮。
- 第二屏白色背景，H2 "AI that works the way your team works" 约 54px，左对齐。
- 下方为 Accordion 折叠面板（Asana Work Graph® / Multiplayer / Shared memory），每个面板有标题 + 展开/收起箭头 + 说明文案。
- 字体：TWK Lausanne, Helvetica Neue；正文 16px。

## 解释与推断
- 102px 超大 H1 是 Asana 的标志性设计手法，让主张本身成为视觉主体，不需要额外装饰。
- 注册区直接放在 Hero 下方，缩短从认知到行动的路径。
- 社交登录 + 邮箱注册的双入口降低注册摩擦。
- Accordion 折叠面板适合展示多个功能点而不占用过多垂直空间，用户可按兴趣展开。
- 整体设计极简，几乎无装饰，完全依赖字体和留白。

## 多维标签
- 范围：企业产品/品牌营销
- 页面任务：工作管理软件的品牌主张与注册转化
- 叙事：大胆主张 → 即时注册 → 功能展开
- 布局：居中超大 H1 + 注册区 + 左对齐 Accordion
- 字体：TWK Lausanne 102px H1 / 54px H2；正文 16px
- 图像：无明显图像，纯文字主导
- 材质与色彩：纯白背景、黑色文字/CTA、灰色副文案
- 状态证据：Hero + Accordion 区已观察；后续章节未完整滚动

## 条件化迁移
- 当品牌主张足够强时，用超大字体让文字本身成为视觉主体，不需要图像或装饰。
  - 不适用于主张需要图像支撑或受众对文字不敏感的场景。
- 注册区紧跟 Hero 适合需要最大化注册转化的产品。
  - 不适用于需要更多教育或信任建立的场景。
- Accordion 折叠面板适合展示多个功能点，让用户按兴趣探索。
  - 不适用于功能点需要同时对比或全部可见的场景。

## 不照搬项与反例
- 不继承 TWK Lausanne 字体或 102px H1（需根据主张强度和屏幕空间判断）。
- 超大字体的可读性需在不同设备上验证，不能盲目放大。
- Accordion 的展开/收起行为需确保键盘可达性和屏幕阅读器支持。

## 证据局限与后续核查
- 未验证注册流程的实际完成。
- Accordion 展开行为未验证。
- 未测试移动端重排（102px H1 在窄屏可能需要大幅缩小）。
- 字体声明为 DOM 读取，实际渲染未二次确认。
