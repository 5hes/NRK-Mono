#!/bin/bash

# 检查是否提供了字体文件目录
if [ -z "\$1" ]; then
    echo "用法: \$0 <字体文件目录>"
    exit 1
fi

# 遍历指定目录下的所有字体文件
for font_file in "\$1"/*; do
    # 检查文件是否为字体文件
    if [[ $font_file == *.ttf || $font_file == *.otf ]]; then
        # 使用 ttx 导出字体信息
        ttx -o temp.ttx "$font_file" >/dev/null 2>&1

        # 检查是否存在 hinting 信息
        if grep -q "<hints>" temp.ttx; then
            echo "$font_file: 经过 hinting"
            ttfautohint -d $font_file
        else
            echo "$font_file: 未经过 hinting"
        fi

        # 删除临时文件
        rm temp.ttx
    fi
done
# 啊啊啊啊啊啊啊啊啊啊
