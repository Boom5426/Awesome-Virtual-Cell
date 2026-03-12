# 词云图以图形化方式展示文本数据中关键词的频率，将高频词以更大的字体展示，低频词以较小的字体呈现，从而突出数据的核心内容。
	
# 本案例读取并分析了文件 c07_text.txt​ 中关于词云图的介绍文本，并添加了云朵形状的蒙版，形状在图片 c07_shape.png​ 中定义，可以自行更改~

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib import colors as mcolors
from PIL import Image  # 用于加载自定义形状
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# 尝试加载样式文件（可选）
try:
    plt.style.use("robox.mplstyle")
except:
    pass

# 设置中文字体和背景透明（按需调整）
bgcolor = "#00000000"  # 背景透明
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 分词函数：使用 jieba 分词并过滤单字
def extract_words(text):
    words = jieba.cut(text, cut_all=False)
    filtered_words = [word for word in words if len(word) > 1]
    return Counter(filtered_words)

# 自定义颜色映射：生成渐变色彩
def create_color_map():
    colors = ["#71aacc", "#d7a6b3"]  # 颜色起始点和终止点
    return LinearSegmentedColormap.from_list("custom_colormap", colors)

# 颜色函数：根据词频动态生成颜色
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    freq = word_frequencies[word]
    factor = freq / max(word_frequencies.values())
    color_map = create_color_map()
    # 获取插值颜色并转为十六进制
    return mcolors.to_hex(color_map(factor))

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5), dpi=150)

# 加载自定义形状（需准备 c07_shape.png 文件）
mask_image = np.array(
    Image.open("./c07_shape.png").resize((1600, 1000), Image.LANCZOS)
)

# 读取文本内容（需准备 c07_text.txt 文件）
with open("./c07_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 手动添加自定义词汇（可选）
jieba.add_word("词云图")

# 分词并统计词频
word_frequencies = extract_words(text)

# 配置词云参数
wordcloud = WordCloud(
    font_path="msyh.ttc",  # 中文字体路径（需系统存在该字体）
    width=1600,
    height=1000,
    background_color=bgcolor,  # 背景透明
    mode="RGBA",
    color_func=color_func,      # 自定义颜色逻辑
    mask=mask_image,            # 应用自定义形状
).generate_from_frequencies(word_frequencies)

# 绘制词云
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")  # 隐藏坐标轴

# 优化布局并显示
plt.tight_layout()
plt.show()
