
import os

#path=input('请输入文件路径(结尾加上/)：')      
path=os.path.abspath(os.path.join(os.getcwd(), "../.."))+'/pic/'

print('***获取当前目录***')
print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))

print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))

#获取该目录下所有文件，存入列表中
f=os.listdir(path)

n=0
for i in f:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path+f[n]
    
    #设置新文件名
    newname=path+str(n+1)+'.jpg'
    
    #用os模块中的rename方法对文件改名
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1
