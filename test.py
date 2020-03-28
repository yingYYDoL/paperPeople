#coding=utf-8
#将同一目录下的多个txt转成csv

import os
import os.path #文件夹遍历函数
import csv
import numpy as np
import pandas as pd

#获取目标文件夹的路径
filedir = r'C:\Users\l\Desktop\untitled\dest'
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('result2.csv','w',newline='',encoding='UTF-8')
writer=csv.writer(f)
#先遍历文件名
for filename in filenames:
    filepath = filedir+'/'+filename
    #遍历单个文件，读取行数
    '''for line in open(filepath,'r', encoding='UTF-8'):
        line.replace('\n',' ')
        line=list(line)
        #print(line)
        f.write(str(line))
        #line.to_csv("test.csv")'''
    with open(filepath,'r',encoding='utf8') as file:
        lines = file.readlines()  # 读取每一行

    a = ''  # 空字符（中间不加空格）
    for line in lines:
        a += line.strip()  # strip()是去掉每行末尾的换行符\n 1
    c = a.split()  # 将a分割成每个字符串 2
    b = ''.join(c)  # 将c的每个字符不以任何符号直接连接 3
    b.strip('\\n')
    #lst=[filepath,b]
    #print(a)
    #print(b)
    # 打印a,b观察不同
    writer.writerow([filename[:-4],b])

#关闭文件
f.close()