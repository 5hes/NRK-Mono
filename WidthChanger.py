#!/usr/bin/env python

import fontforge
import psMat
import sys

# 检查命令行参数
if len(sys.argv) < 3:
    raise Exception("Usage: script.py <fontfile> <scale_factor> [output_directory]")

# 打开字体文件
font = fontforge.open(sys.argv[1])

# 获取缩放因子，确保它是一个有效的数字
try:
    scale_factor = float(sys.argv[2])
except ValueError:
    raise Exception("Scale factor must be a number.")

# 遍历字体中的每个字形并进行缩放
for g in font.glyphs():
    g.transform(psMat.scale(scale_factor, 1.0))

# 处理字体名称
fnv = font.fontname.split("-")
if len(fnv) != 2:
    raise Exception("Unexpected fontname")
style = fnv[1]

# 创建输出文件名
o = font.familyname + " Condensed " + style + ".ttf"
o = o.replace(" ", "-")

# 更新字体名称
font.fontname = fnv[0] + "Condensed-" + style
font.familyname = font.familyname + " Condensed"
font.fullname = font.fullname + " Condensed"

# 设置输出目录
d = "./"
if len(sys.argv) > 3:
    d = sys.argv[3] + "/"

# 生成新的字体文件
font.generate(d + o)
