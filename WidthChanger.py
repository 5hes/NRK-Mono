import fontforge
import psMat
import sys

# 检查参数数量
if len(sys.argv) < 4:
    raise Exception("Usage: python script.py <input_font.ttf> <output_directory> <scale_factor>")

input_font_path = sys.argv[1]
output_directory = sys.argv[2]
scale_factor = float(sys.argv[3])  # 将缩小倍数转换为浮点数

# 打开字体文件
font = fontforge.open(input_font_path)

# 对每个字形进行缩放
for g in font.glyphs():
    g.transform(psMat.scale(scale_factor, 1.0))

# 处理字体名称
fnv = font.fontname.split("-")
if len(fnv) != 2:
    raise Exception("Unexpected fontname")
style = fnv[1]

# 构建输出文件名
o = font.familyname + " Condensed " + style + ".ttf"
o = o.replace(" ", "-")

# 更新字体属性
font.fontname = fnv[0] + "Condensed-" + style
font.familyname = font.familyname + " Condensed"
font.fullname = font.fullname + " Condensed"

# 确定输出目录，确保以斜杠结尾
if not output_directory.endswith('/'):
    output_directory += '/'

# 生成新的字体文件
font.generate(output_directory + o)
