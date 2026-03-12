# Awesome Scientific Figures [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

📊 本仓库收录多种科学可视化 Jupyter Notebook 代码，基于 Python 生态库（`matplotlib`/`seaborn` 等 ）实现，覆盖科研分析、数据探索等场景，助力直观呈现数据规律。  


## 一、使用准备  
### 1. 依赖库安装 🛠️  
确保安装以下 Python 库（复制命令执行即可）：  
```bash  
pip install numpy pandas matplotlib seaborn jupyter  
```  

### 2. 运行方式 🚀  
启动 Jupyter 环境，运行 `.ipynb` 文件：  
```bash  
jupyter notebook  # 或 jupyter lab（推荐）  
```  
在浏览器界面找到目标文件，执行所有单元格，即可生成可视化图表。  


## 二、可视化图表分类与适用场景  
| 图表类型                  | 核心适用场景                                                                 |  
|---------------------------|------------------------------------------------------------------------------|  
| [对比点图](对比点图.ipynb)            | 📌 快速对比多组简单数值（如实验组别单一指标差异），直观呈现组间数值区别。       |  
| [分组气泡图](分组气泡图.ipynb)          | 🔵 呈现多组数据分布基础上，用气泡大小附加数值信息（如样本数量、基因表达强度）。 |  
| [单轴分组气泡图](单轴分组气泡图.ipynb)      | 🟢 聚焦一维数据分布，通过气泡附加信息（数量、类别），简化版多维度探索。         |  
| [堆叠柱状图](堆叠柱状图.ipynb)          | 📊 同时呈现多组数据数值大小与占比关系（如细胞亚群、基因功能分类占比）。         |  
| [多变量变化趋势图](多变量变化趋势图.ipynb)    | 📈 展示多个变量随共同因素（时间、浓度梯度）的变化趋势，对比响应模式差异。       |  
| [嵌套饼图](嵌套饼图.ipynb)              | 🥧 展示多层级、多类别数据的占比关系，清晰呈现数据的层级结构与比例分布。         |  
| [弦图](弦图.ipynb)                          | 🔗 呈现数据间流动/关联关系（代谢通路物质转化、种群迁移），展示关系方向与强度。   |  
| [径向柱状图](径向柱状图.ipynb)            | 🌀 以环形布局展示多组数据的数值大小，适合突出数据间的对比及环形分布特征。       |  
| [折线图](折线图.ipynb)                      | 📉 展示数据随连续变量（如时间、浓度）的变化趋势，清晰呈现数据的增减规律。       |  
| [散点图_误差棒组合图](散点图_误差棒组合图.ipynb) | 📍 对比不同方法/模型在双指标上的表现（如聚类算法 ARI、NMI 指标），误差棒体现结果波动。 |  
| [旭日图](旭日图.ipynb)                      | 🌞 可视化多层级、树状结构数据的占比关系，从整体到局部逐步展开数据层级。         |  
| [椭圆散点图](椭圆散点图.ipynb)            | ⭕ 在散点图基础上，用椭圆等几何图形辅助分析数据分布的集中趋势与离散程度。       |  
| [热力图](热力图.ipynb)                      | 🔥 以颜色矩阵形式展示数据的矩阵关系（如基因表达相关性、特征相似度），直观呈现数据密集度与关联强度。 |  
| [玫瑰图](玫瑰图.ipynb)                      | 🌹 展示周期性/环形分布数据（生物节律、风向频率），用半径+角度增强分布特征。     |  
| [环形蜂窝条形图](环形蜂窝条形图.ipynb)      | 🐝 融合蜂窝图（个体样本细节）与条形图（整体影响大小），适用于单细胞分析、通路影响展示。 |  
| [相关性网络图](相关性网络图.ipynb)        | 🧩 呈现变量间（如基因、代谢物）的相关性关系，用节点和连线展示关联网络结构。     |  
| [词云图](词云图.py)                          | 🔤 文本数据分析（基因功能注释词频、文献关键词），突出高频词汇核心信息。         |  
| [趋势分布散点图](趋势分布散点图.ipynb)    | 📊 结合散点分布与趋势分析，展示数据随变量变化的分布规律及整体趋势走向。         |  
| [边际直方图](边际直方图.ipynb)          | 📊 分析两个连续变量（如身高-体重、基因表达量-代谢物浓度）的联合分布与单变量分布。 |  
| [雷达图](雷达图.ipynb)                      | 🛡️ 展示多维度数据的综合表现，将各维度指标映射到雷达轴上，对比不同样本/组别的综合特征。 |  
| [云雨图](云雨图.ipynb)                      | 🌧️ 融合箱线图与核密度图特点，展示多组数据的分布形态、集中趋势与离散程度，便于组间分布对比  |  


## 三、通用调整建议  
1. **数据替换** 📥：找到代码中数据导入/生成部分（如 `pd.read_csv` ），替换为实际数据文件或自定义数据。  
2. **参数优化** ⚙️：  
   - 样式：调整颜色（`color`）、线条/点样式（`linestyle`/`marker` ）。  
   - 布局：修改图大小（`figsize`）、坐标轴范围（`xlim`/`ylim` ）。  
   - 数据映射：调整分箱数（`bins`）、误差棒大小（`capsize` ）等。  
3. **结果保存** 💾：如需导出图表，在 `plt.show()` 前添加（支持 PNG/PDF 等格式）：  
```python  
plt.savefig("路径/文件名.png", dpi=300, bbox_inches="tight")  
```  

可根据数据特征与分析目标，灵活选用图表并调整参数，高效呈现科研数据规律 🌟。


## Contributing 🤝

Contributions are warmly welcome!  

If you have:
- 🖌️ A **new type of plot**（新图表类型）  
- 📊 Improvements for **existing scripts**（现有代码优化）  
- 📚 Tips on **plot styling or figure preparation**（图表样式/制作技巧）  

Feel free to open a **Pull Request** or create an **Issue**.  
Please follow these simple rules:
1. Add your script under the correct folder (e.g., `scientific/`, `statistics/`).  
2. Keep the code **clear, documented, and minimal**（代码清晰、带注释、精简）.  
3. Provide a **preview image** of the output figure (PNG recommended，附输出图表预览图).  
4. Add your script to the **README Contents** section with a short description（在 README 中补充说明）.


## License 📜

This project follows the [MIT License](LICENSE).  
Plots are meant for learning, research, and sharing good practices（图表仅供学习、科研及分享优质实践使用）.
