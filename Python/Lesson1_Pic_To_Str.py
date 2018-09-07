#编码格式
# -*- coding: utf-8 -*-  
#学习使用 Image库的安装和简单使用
#def 关键字修饰和定义函数
import argparse 
'''
1、argparse #python标准库里面用来处理命令行参数的库
2、命令行参数分为位置参数和选项参数：
    位置参数：程序根据该参数出现的位置来确定的
        如：[root@openstack_1 /]# ls root/    #其中root/是位置参数
    选项参数：应用程序已经提前定义好的参数，不是随意指定的
        如：[root@openstack_1 /]# ls -l    # -l 就是ls命令里的一个选项参数
3、实使用步骤
    （1）import argparse    首先导入模块
    （2）parser = argparse.ArgumentParser（）    创建一个解析对象
    （3）parser.add_argument()    向该对象中添加你要关注的命令行参数和选项
    （4）parser.parse_args()    进行解析
'''

#命令行输入参数处理
parser = argparse.ArgumentParser()
#parser.add_argument('file',default = 'ascii_dora.png')     #输入文件
#parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高
#解析参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

from PIL import Image
print("Hello World!")

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