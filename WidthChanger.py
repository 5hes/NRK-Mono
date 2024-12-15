import fontforge
import psMat
import sys
import os

# 检查参数数量
if len(sys.argv) < 5:
    raise Exception("Usage: python WidthChanger.py <input_font.ttf> <output_directory> <scale_factor> <output_filename>")

input_font_path = sys.argv[1]
output_directory = sys.argv[2]
scale_factor = float(sys.argv[3])  # 将缩小倍数转换为浮点数
output_filename = sys.argv[4]  # 新增参数：自定义输出文件名

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 打开字体文件
font = fontforge.open(input_font_path)

# 对每个字形进行缩放
for g in font.glyphs():
    g.transform(psMat.scale(scale_factor, 1.0))

# 处理字体名称
print("Font name:", font.fontname)  # 打印字体名称以进行调试
fnv = font.fontname.split("-")

# 检查字体名称格式
if len(fnv) != 2:
    print("Warning: Unexpected fontname format. Using default style.")
    style = "Regular"  # 提供一个默认样式
else:
    style = fnv[1]

# 更新字体属性
font.fontname = fnv[0] + "Condensed-" + style
font.familyname = font.familyname + " Condensed"
font.fullname = font.fullname + " Condensed"

# 构建输出文件的完整路径
output_file_path = os.path.join(output_directory, output_filename)

# 生成新的字体文件
try:
    print("Generating font:", output_file_path)
    font.generate(output_file_path)
    print("Font generated successfully.")
except Exception as e:
    print("Error generating font:", e)
