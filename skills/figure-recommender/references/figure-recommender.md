# Figure Recommender Reference

Use this file to map user intent to chart types and notebooks in `Awesome-Scientific-Figures/`.

## Quick Intake

Extract or ask for:

- What data is being plotted
- What conclusion the user wants to communicate
- Variable structure: single variable, grouped comparison, trend, matrix, hierarchy, network, ranking, or multi-metric comparison
- Whether the figure is for a paper main figure, supplement, slides, or exploration
- Whether the user prefers safe readability or stronger styling

If the user is vague, default to readable paper-friendly figures first.

## Goal-to-Chart Mapping

| User goal | Prefer | Reference files | Notes |
|---|---|---|---|
| Compare a single metric across groups | 对比点图 | `Awesome-Scientific-Figures/对比点图.ipynb` | Best default for small-to-medium category counts |
| Compare composition or proportions across groups | 堆叠柱状图 | `Awesome-Scientific-Figures/堆叠柱状图.ipynb` | Good for cell composition and subgroup share |
| Show distributions across groups | 云雨图 | `Awesome-Scientific-Figures/云雨图.ipynb` | Better than a bare boxplot when distribution matters |
| Show joint distribution of two continuous variables | 边际直方图 | `Awesome-Scientific-Figures/边际直方图.ipynb` | Good for exploratory or supplement views |
| Show trend over time, dose, or pseudotime | 折线图 | `Awesome-Scientific-Figures/折线图.ipynb` | Best first choice when x-axis is ordered and continuous |
| Show multiple coordinated trends | 多变量变化趋势图 | `Awesome-Scientific-Figures/多变量变化趋势图.ipynb` | Use when several trajectories matter, but keep legend controlled |
| Show matrix pattern or correlation structure | 热力图 | `Awesome-Scientific-Figures/热力图.ipynb` | Strong default for many variables |
| Emphasize graph relations or modules | 相关性网络热图 | `Awesome-Scientific-Figures/相关性网络热图.ipynb` | Use only when edges and modules are central to the story |
| Show paired or two-sided network comparison | 相关性网络热图_蝴蝶图 | `Awesome-Scientific-Figures/相关性网络热图_蝴蝶图.ipynb` | Higher complexity; avoid for beginners unless clearly needed |
| Show explicit hierarchy or nested composition | 旭日图, 嵌套饼图 | `Awesome-Scientific-Figures/旭日图.ipynb`, `Awesome-Scientific-Figures/嵌套饼图.ipynb` | Only when there is real parent-child structure |
| Compare a small number of metrics per item | 雷达图 | `Awesome-Scientific-Figures/雷达图.ipynb` | Works only for a few dimensions |
| Show ranking plus extra encodings | 综合排序气泡图 | `Awesome-Scientific-Figures/综合排序气泡图.ipynb` | Useful for method comparison or leaderboard-style results |
| Encode x/y plus size and grouping | 分组气泡图, 单轴分组气泡图 | `Awesome-Scientific-Figures/分组气泡图.ipynb`, `Awesome-Scientific-Figures/单轴分组气泡图.ipynb` | Use when bubble size carries real meaning, not decoration |
| Show scattered groups or distribution envelopes | 椭圆散点图, 趋势分布散点图 | `Awesome-Scientific-Figures/椭圆散点图.ipynb`, `Awesome-Scientific-Figures/趋势分布散点图.ipynb` | Good for exploratory analysis |
| Show benchmark trade-offs with uncertainty | 散点图 + 误差棒 | `Awesome-Scientific-Figures/散点图_误差棒组合图.ipynb` | Useful for methods papers and model comparisons |
| Show flow, pairing, or interaction strength | 弦图 | `Awesome-Scientific-Figures/弦图.ipynb` | Strong style, but easily overloaded |
| Emphasize circular structure or presentation style | 玫瑰图, 径向柱状图 | `Awesome-Scientific-Figures/玫瑰图.ipynb`, `Awesome-Scientific-Figures/径向柱状图.ipynb` | Prefer only when circular encoding is actually helpful |
| Create a highly styled feature figure | 环形蜂窝条形图 | `Awesome-Scientific-Figures/环形蜂窝条形图.ipynb` | Strong visual style, not a default scientific chart |
| Pick color direction before plotting | 配色参考 | `Awesome-Scientific-Figures/配色.ipynb`, `Awesome-Scientific-Figures/配色.png` | Recommend only as a helper, not as the final figure itself |
| Prepare slides or graphic assets | PPT 模板 | `Awesome-Scientific-Figures/PPT配色模板.pptx`, `Awesome-Scientific-Figures/机器学习绘图模板.pptx` | Better for presentation packaging than data analysis |
| Show text term frequency | 词云图 | `Awesome-Scientific-Figures/词云图.py` | Supplementary only; not a primary evidence figure |

## Default Recommendations for New Users

If the user is new, unsure, or mainly wants a paper-ready figure, prefer these first:

- `Awesome-Scientific-Figures/对比点图.ipynb`
- `Awesome-Scientific-Figures/折线图.ipynb`
- `Awesome-Scientific-Figures/热力图.ipynb`
- `Awesome-Scientific-Figures/云雨图.ipynb`
- `Awesome-Scientific-Figures/堆叠柱状图.ipynb`

## High-Complexity Charts

Do not recommend these by default unless the structure clearly requires them or the user explicitly wants a style-forward figure:

- `Awesome-Scientific-Figures/弦图.ipynb`
- `Awesome-Scientific-Figures/环形蜂窝条形图.ipynb`
- `Awesome-Scientific-Figures/相关性网络热图_蝴蝶图.ipynb`
- `Awesome-Scientific-Figures/旭日图.ipynb`
- `Awesome-Scientific-Figures/径向柱状图.ipynb`

## Common “Not Recommended” Cases

Use these guardrails when adding a `不推荐` / `Not recommended` section:

- Do not recommend hierarchy charts when there is no real hierarchy.
- Do not recommend circular charts when the user needs precise value comparison.
- Do not recommend network charts when the graph is dense and there is no clear focal relation.
- Do not recommend radar charts when there are too many metrics or items.
- Do not recommend bubble charts when bubble size is only decorative.
- Do not recommend word clouds for core scientific claims.

## Language Cues

These phrases usually map to the following chart intents:

- `组间差异`, `compare groups`, `difference across groups` -> 对比点图, 云雨图
- `组成`, `占比`, `composition`, `proportion` -> 堆叠柱状图
- `趋势`, `时间`, `time course`, `trajectory`, `pseudotime` -> 折线图, 多变量变化趋势图
- `相关性`, `矩阵`, `correlation`, `matrix`, `cluster pattern` -> 热力图
- `网络`, `模块`, `interaction network`, `graph` -> 相关性网络热图
- `层级`, `父子结构`, `hierarchy`, `nested` -> 旭日图, 嵌套饼图
- `排名`, `综合表现`, `leaderboard`, `overall comparison` -> 综合排序气泡图, 雷达图
- `联合分布`, `joint distribution` -> 边际直方图
- `误差`, `uncertainty`, `benchmark comparison` -> 散点图 + 误差棒

## Response Bias

- If two options are equally valid, choose the simpler one first.
- If the user says “for a main paper figure”, bias toward readability.
- If the user says “for slides” or “I want something more striking”, style-forward options are acceptable as the second or third recommendation.
- If the user already proposed a chart type, evaluate it directly instead of ignoring it.
