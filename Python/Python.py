
import argparse
from PIL import Image
print("Hello World!")
#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output')   #输出文件
#获取参数
args = parser.parse_args()
OUTPUT = args.output
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

im = Image.open('ascii_dora.png')
im.show()
WIDTH = 80
HEIGHT = 80
im = im.resize((WIDTH,HEIGHT), Image.NEAREST)
txt = ""

for i in range(HEIGHT):
    for j in range(WIDTH):
        txt += get_char(*im.getpixel((j,i)))
    txt += '\n'

print(txt)

#字符画输出到文件
if OUTPUT:
    with open(OUTPUT,'w') as f:
        f.write(txt)
else:
    with open("output.txt",'w') as f:
        f.write(txt)