import os,shutil
import os.path #文件夹遍历函数

dstfile=r'C:\Users\l\Desktop\untitled\dest'
dictdir = r'C:\Users\l\Desktop\untitled\data'
dictnames=os.listdir(dictdir)
for dictname in dictnames:
    dictname = dictdir+'\\'+dictname
    filenames=os.listdir(dictname)
    for filename in filenames:
        filepath=dictname+'\\'+filename
        #print(filepath)
        shutil.move(filepath, dstfile)