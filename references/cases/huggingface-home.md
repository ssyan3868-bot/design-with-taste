# Hugging Face 首页：开发者社区的深色门户

## 来源与观察边界
- 来源：https://huggingface.co/
- 来源性质：AI/ML 开源社区平台首页
- 整理：2026-09-20；初次浏览：2026-09-20
- 实际语言：英文
- 桌面范围：CSS 视口 1280×720；文档高度 5986px
- 观察对象：Hero、Trending 三栏区
- 证据载体：截图观察 + DOM 快照

## 已记录事实
- Hero 背景为深海军蓝/近黑色（#0b0f19 左右），左侧为品牌 emoji 吉祥物（黄色笑脸）+ H1 "The AI community building the future." 约 48px，白色粗体。
- 副文案 "The platform where the machine learning community collaborates on models, datasets, and applications." 灰色，左对齐。
- 两个 CTA："Explore AI Apps"（白色描边圆角按钮）+ "Browse 2M+ models"（文字链接带下划线）。
- 右侧为产品界面截图（模型浏览器），深色背景，展示模型列表、标签筛选、下载量/点赞数等元数据。
- 顶部导航：Models / Datasets / Spaces / Buckets(NEW) / Docs / Pricing / Log In / Sign Up。
- 第二屏白色背景，H2 "Trending on 🤗 this week" 居中，下方三栏（Models / Spaces / Datasets），每栏 5 个条目。
- Spaces 栏的卡片有彩色渐变背景（紫/蓝/绿），其他两栏为白色卡片带边框。
- 字体：Source Sans Pro, system-ui；正文 16px。

## 解释与推断
- 深色 Hero + 产品截图的组合让开发者直接看到平台界面，降低认知成本。
- 品牌 emoji 吉祥物增加亲和力，平衡深色背景的严肃感。
- 三栏 Trending 展示社区活跃度，用真实数据（下载量、点赞数）建立可信度。
- Spaces 卡片的彩色渐变背景让应用类内容更突出，与模型/数据集的简洁卡片形成区分。
- 整体设计偏向信息密度，适合开发者快速浏览和发现。

## 多维标签
- 范围：企业产品/品牌营销（社区平台）
- 页面任务：AI 社区平台入口与内容发现
- 叙事：品牌定位 → 平台预览 → 热门内容发现
- 布局：左文右图 Hero + 三栏 Trending 列表
- 字体：Source Sans Pro 48px H1 / 18px H2；正文 16px
- 图像：品牌 emoji、产品 UI 截图、Spaces 彩色渐变卡片
- 材质与色彩：深海军蓝 Hero、白色内容区、Spaces 彩色渐变
- 状态证据：Hero + Trending 区已观察；搜索和筛选行为未验证

## 条件化迁移
- 当平台需要展示真实内容生态时，用 Trending/热门列表代替功能说明。
  - 不适用于内容质量不稳定或需要策展的场景。
- 深色 Hero + 产品截图适合开发者工具，让用户直接看到界面。
  - 不适用于需要情感连接或非技术受众的场景。
- 三栏等宽布局适合并列展示三类内容，但需确保每栏内容量均衡。
  - 不适用于内容量差异大的分类。

## 不照搬项与反例
- 不继承 Source Sans Pro 字体或 48px H1。
- 品牌 emoji 是 Hugging Face 的独特资产，不泛化为"AI 产品用 emoji"。
- Spaces 卡片的彩色渐变是内容类型区分手法，不是通用卡片样式。

## 证据局限与后续核查
- 未验证搜索、筛选、登录等交互功能。
- 未测试移动端重排。
- 字体声明为 DOM 读取，实际渲染未二次确认。
