<h1 align="center">Awesome Virtual Cell</h1>

<p align="center">
  <a href="README.md">English</a> · <strong>简体中文</strong>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <a href="https://github.com/Boom5426/Awesome-Virtual-Cell/stargazers"><img src="https://img.shields.io/github/stars/Boom5426/Awesome-Virtual-Cell?style=flat-square&logo=github&label=Stars" /></a>
  <a href="https://github.com/Boom5426/Awesome-Virtual-Cell/commits/main"><img src="https://img.shields.io/github/last-commit/Boom5426/Awesome-Virtual-Cell?style=flat-square&logo=github&label=Updated" /></a>
</p>

<p align="center"><b>面向 AI 虚拟细胞研究的论文、数据集、Benchmark 与社区资源导航。</b></p>

<p align="center">
  Virtual Cells &nbsp;·&nbsp; Perturbation &nbsp;·&nbsp; Intervention Design &nbsp;·&nbsp; Foundation Models &nbsp;·&nbsp; Spatial
</p>

<p align="center">
  <a href="https://boom5426.github.io/Awesome-Virtual-Cell/"><img src="https://img.shields.io/badge/检索与筛选-浏览目录-0B6E99?style=for-the-badge" alt="检索 Awesome Virtual Cell 目录" /></a>
  <a href="https://boom5426.github.io/Awesome-Virtual-Cell/landscape.html"><img src="https://img.shields.io/badge/研究版图-交互式地图-24B6A6?style=for-the-badge" alt="浏览交互式研究版图" /></a>
</p>

<p align="center">
  <sub>
    <a href="#从这里开始">从这里开始</a> ·
    <a href="README.md#research-papers">完整论文列表</a> ·
    <a href="README.md#datasets">数据集</a> ·
    <a href="README.md#challenges-and-competitions">挑战赛</a> ·
    <a href="#项目范围">项目范围</a> ·
    <a href="#参与贡献">参与贡献</a>
  </sub>
</p>

> [!NOTE]
> 中文版定位为**中文导航入口**。完整论文目录由结构化数据自动生成并持续更新，因此仍以英文主 README 和在线检索目录为唯一完整版本，避免中英文两份长列表不同步。论文标题、期刊名和模型名保留原文。

## 🚀 从这里开始

如果你刚进入 Virtual Cell / AI for Biology 方向，不建议从数百篇论文逐条向下读。可以先按问题选择入口：

先读所在方向的**加粗条目**，再比较其他代表工作。这里是精选阅读入口，不是性能排行榜；发表状态请以完整论文目录为准。

| 目标 | 推荐入口 |
| --- | --- |
| 🧬 **理解 Virtual Cell 的整体问题** | **[Cell perspective](https://doi.org/10.1016/j.cell.2024.11.015)** · [Grow AI Virtual Cells](https://www.nature.com/articles/s41422-025-01101-y) · [Nature perspective](https://www.nature.com/articles/s41586-025-08710-y) |
| 🧫 **预测细胞扰动响应** | **[GEARS](https://www.nature.com/articles/s41587-023-01905-6)** · [STATE](https://doi.org/10.1016/j.cell.2026.07.052) · [PIE](https://doi.org/10.64898/2026.10.02.756297) · [MAP](https://doi.org/10.1038/s42256-026-01286-w) · [CellFlow](https://doi.org/10.1101/2025.04.11.648220) |
| 🧠 **细胞基础模型** | **[Geneformer](https://doi.org/10.1038/s41586-023-06139-9)** · [scGPT](https://doi.org/10.1038/s41592-024-02201-0) · [scFoundation](https://doi.org/10.1038/s41592-024-02305-7) · [UCE](https://doi.org/10.1038/s41586-026-10689-z) · [TranscriptFormer](https://doi.org/10.1126/science.aec8514) |
| 🌐 **世界模型与细胞状态转移** | **[A world model of the virtual cell](https://doi.org/10.1016/j.cell.2026.08.042)** · [CellOS](https://doi.org/10.64898/2026.06.18.733163) · [Chreode](https://arxiv.org/abs/2605.28111) |
| 🖼️ **多模态与空间组学** | **[Nicheformer](https://doi.org/10.1038/s41592-025-02814-z)** · [VirTues](https://doi.org/10.1038/s41586-026-10884-y) · [DePass](https://doi.org/10.1038/s41556-026-02067-8) · [UniPert-G2CP](https://doi.org/10.1016/j.cell.2026.06.005) |
| 🎯 **干预设计 / 逆向设计** | **[PDGrapher](https://doi.org/10.1038/s41551-025-01481-x)** · [DrugReflector](https://doi.org/10.1126/science.adi8577) · [CellNavi](https://doi.org/10.1038/s41556-025-01755-1) · [PAIRING](https://doi.org/10.1016/j.cels.2025.101405) · [VCDesign](https://github.com/Boom5426/VCDesign-CED/blob/main/paper/VCDesign.pdf) |
| 📏 **评价与测量分辨率** | **[Systema](https://doi.org/10.1038/s41587-025-02777-8)** · [SCMBench](https://doi.org/10.1038/s41467-026-72570-x) · [PertResolve](https://github.com/Boom5426/PertResolve/blob/main/manuscript/PertResolve_manuscript.pdf) · [Signal, Bounds & Baselines](https://doi.org/10.64898/2026.04.20.719650) · [Principled Evaluation](https://doi.org/10.64898/2026.07.23.740433) |

## 🗺️ 两种最推荐的浏览方式

### 1. 可检索论文目录

**[打开 Search & Filter Catalog ↗](https://boom5426.github.io/Awesome-Virtual-Cell/)**

支持按关键词、年份、研究主题和发表状态筛选。相比在 README 中逐条搜索，更适合快速回答：

- 有哪些 perturbation prediction 工作？
- 哪些论文提供开源代码？
- Foundation model、world model、intervention design 分别有哪些代表工作？
- 某一方向近一年新增了哪些论文？

### 2. 交互式研究版图

**[打开 Interactive Research Landscape ↗](https://boom5426.github.io/Awesome-Virtual-Cell/landscape.html)**

适合先建立领域结构，再进入具体论文。研究主题包括：

- Virtual Cell
- Perturbation Modeling
- Foundation Models
- World Models / JEPA
- Multimodal & Spatial Biology
- Morphology / Cell Painting
- Gene Regulation & Dynamics
- Intervention Design
- Evaluation & Measurement
- Biological AI Agents

## 🔬 完整论文目录

完整、持续更新的论文列表位于：

**[README → Research Papers](README.md#research-papers)**

论文采用多标签组织，一篇工作可以同时属于多个研究主题。标签定义见 [taxonomy](docs/taxonomy.md)。

同时可以直接查看机器可读数据：

- [Structured paper data](data/papers.json) — 论文结构化 JSON
- [Curation record](data/curation/2026-09-26.json) — 标签依据、来源链接与代码关联检查
- [Searchable catalog](https://boom5426.github.io/Awesome-Virtual-Cell/) — 在线搜索与筛选

## 🧬 数据集与 Benchmark

完整数据集资源见：

**[README → Datasets](README.md#datasets)**

Benchmark、挑战赛与社区评测见：

**[README → Challenges and Competitions](README.md#challenges-and-competitions)**

当前仓库不仅收集通用单细胞数据，还重点关注与 Virtual Cell 直接相关的：

- 扰动响应数据
- 单细胞与多组学数据
- Cell Painting / morphology 数据
- 空间组学数据
- 跨细胞背景与跨扰动泛化 benchmark
- Virtual Cell Challenge 与相关社区评测

## 🎯 项目范围

这里的 **AIVC** 指 **Artificial Intelligence Virtual Cell**。该概念由 *Cell* perspective [“How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities”](https://doi.org/10.1016/j.cell.2024.11.015) 等工作进一步系统化。

本仓库希望覆盖的是：**真正有助于理解、构建、评价或应用 Virtual Cell 的研究资源**，而不是泛化成一个无限扩张的 biomedical AI 列表。

主要纳入：

- Virtual Cell 相关 perspective、review 与方法论文
- 细胞扰动建模与 perturbation prediction
- 单细胞、多模态和空间 foundation models
- World model、JEPA 与细胞动态建模
- Cell Painting / morphology modeling
- 干预设计、药物或基因 perturbation prioritization
- Evaluation、benchmark 与 measurement
- 与 Virtual Cell 密切相关的 biological AI agents
- 高价值数据集、挑战赛和社区资源

通常不纳入：

- 与细胞建模关系较弱的通用 biomedical AI 工作
- 缺乏可靠来源的二手信息
- 已失效链接或信息无法核验的资源
- 与已有核心条目相比没有明显新增价值的外围工作

## ✅ 收录原则

- 优先同行评审论文、高信息量 preprint、官方项目主页和一手来源。
- 有价值时补充代码、数据集、项目主页或中文解读。
- 条目尽量简洁，方便快速浏览和复用。
- 使用统一的多标签 [taxonomy](docs/taxonomy.md)，标签依据实际任务与证据，而不是只看模型名字。

## 🧰 仓库与数据

这些入口主要面向复用、维护和贡献：

- **[Searchable catalog](https://boom5426.github.io/Awesome-Virtual-Cell/)** — 按关键词、年份、主题和发表状态筛选论文
- **[Structured paper data](data/papers.json)** — Research Papers 的机器可读数据
- **[Architecture](docs/architecture.md)** — 结构化数据、生成页面、验证与自动化的组织方式
- **[Automation](docs/automation.md)** — 文献更新如何提出和验证
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — 投稿与贡献规范

## 🤝 参与贡献

欢迎推荐新的论文、数据集、benchmark、博客或项目。

可以直接提交 **Issue** 或 **Pull Request**。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并尽量提供：

- 原始论文或官方项目链接
- 代码 / 数据集链接（如有）
- 推荐归类的研究主题
- 为什么该工作对 Virtual Cell 社区有价值

## ⭐ Star History

<p align="center">
  <a href="https://star-history.com/#Boom5426/Awesome-Virtual-Cell&Date">
    <img src="https://api.star-history.com/svg?repos=Boom5426/Awesome-Virtual-Cell&type=Date" alt="Star History Chart" />
  </a>
</p>

---

<p align="center">
  <a href="README.md">English README</a> ·
  <a href="https://boom5426.github.io/Awesome-Virtual-Cell/">在线论文目录</a> ·
  <a href="https://boom5426.github.io/Awesome-Virtual-Cell/landscape.html">研究版图</a>
</p>
