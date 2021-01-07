#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# Author : Enming Huang
# Date : 1/7/2021

import csv
import sys
import os.path
## 字符串处理函数 M k m u n p f
def handlerstring(str):
    chengshu = ""
    if(str[-1]=='M'):
        chengshu="e6"
    elif(str[-1]=='k'):
        chengshu="e3"
    elif(str[-1]=='m'):
        chengshu="e-3"
    elif(str[-1]=='u'):
        chengshu="e-6"
    elif(str[-1]=='n'):
        chengshu="e-9"
    elif(str[-1]=='p'):
        chengshu="e-12"
    elif(str[-1]=='f'):
        chengshu="e-15"
    else:
        return abs(float(str))
    #print(str[0:-1])
    #print(chengshu)
    val = abs(float(str[0:-1]+chengshu))
    return val

def checkdir(pathname,sign):
    if(sign == 0):
        #输入路径
        if os.path.exists(pathname) is True:
            return True
        else:
            return False
    else:
        #输出路径判断
        partpath = pathname.split('\\')
        if(len(partpath)==1):
            return True
        else:
            newpath = ""
            for i in range(len(partpath)-1):
                newpath = newpath+partpath[i]+'\\'
            #print(newpath)
            if os.path.exists(newpath) is True:
                return True
            else:
                return False
            

def getres(indir,outdir):
    #提出文件名字
    dicname = indir.split('\\')
    filename=dicname[-1].split('.')[0]
    #print(filename)
    ##
    f=open(indir,mode='r',encoding='utf-8')
    content=f.readlines()
    #print(type(content))
    x = 0
    y = 0
    for i in range(len(content)):
        if content[i] == "x\n":
            x=i
        if content[i] == "y\n":
            y=i
            break
    #print(x)
    #print(y)
    if abs(y-x)<5:
        print("input file went wrong!")
        return
    ## 下面处理数据
    output= []
    ## 寻找有多少变量
    #row_value = x + 2
    valuenames = content[x+2].split(' ')[0:-1]
    #print(valuenames)
    new_valuenames = []
    for valuename in valuenames:
        if(valuename != ''):
            new_valuenames.append(valuename)
    #print(new_valuenames)
    if(len(new_valuenames)==0):
        print("input file went wrong!")
        return
    ##
    j=x+4
    while(j!=y):
        tmp=content[j][2:-1].split(' ')
        res=[]
        #j=j+1
        for val in tmp:
            if val !='':
                res.append(val)
                #print(val)
        #print("//////////////")
        #print(res)
        #处理字符串 M k m u n p f
        hang=[]
        for i in range(len(new_valuenames)):
            hang.append(handlerstring(res[i]))
        output.append(hang)
        #print(hang)
        j=j+1
    #print(len(output))
    #print(output)
    if outdir !="":
        csvout = open(outdir,'w',newline='')
    else:
        newfilename=".\\"+filename+".csv"
        csvout = open(newfilename,'w',newline='')
    writer=csv.writer(csvout)
    writer.writerow(new_valuenames)
    writer.writerows(output)
    csvout.close()
    f.close() 


if __name__ == "__main__":
    argint = len(sys.argv)
    #print(argint)
    Flag = False
    if(argint >3):
        print("input arguments are illegal!")
        Flag = True
    if(checkdir(sys.argv[1],0) == False):
        print("input Hspice file does not exist!")
        Flag = True
    ## 用户定义了输出路劲
    if(argint == 3) and checkdir(sys.argv[2],1) == False:
        print("output directory does not exist！")
        Flag = True
    if Flag == True:
        print("something went wrong!")
    else :
        if argint == 3:
            getres(sys.argv[1],sys.argv[2])
        else:
            getres(sys.argv[1],"") 