#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil, os
import sys
import os
import time
import os.path
 
makeDirectory = os.getcwd()
f = open("CompareFiles.txt", "r+", encoding = 'utf-8')          #開啟檔案,須以r+讀寫模式
filesList = f.readlines()
currentPath = os.path.abspath('')
for line in filesList:
  data=line.strip()
  if len(data)!=0:
    filesPath = data.split('|')[0]
    dirPath = filesPath.strip(filesPath.split('\\')[-1])
    makeDirPath = dirPath.strip(filesPath.split('\\')[0])
    if not os.path.isdir(makeDirectory+makeDirPath[:-1]): #如果有相同路徑不建立
      os.makedirs(makeDirectory+makeDirPath[:-1], 493)    
    try:
      #if os.path.isfile(filesPath):
       shutil.copy(filesPath, makeDirectory+makeDirPath[:-1])
    except FileNotFoundError:
      print(filesPath + '此為刪除的檔案')
    except:
      print('不明錯誤')
f.close()
    

#2017-04-02 14:11:53.570550
#filesCompare = open('FilesBackup.txt', 'r', encoding = 'utf8')
#filesCompare.read()

#r_file = open('filesCompare.txt', "r", encoding = 'utf-8')
#lines = r_file.readlines()
#r_file.close()
#for idx, line in enumerate(lines):
#    if line.split():
#        print(line)
#r_file.close()
#print(fileaString)
#print(fileaString)
#filea.next()
#idFilter = '|'         #搜索檔案內特定的文字
#idPosition = fileaString.find(idFilter)  #抓出檔案內特定的文字位置
#print(idPosition)
#print(fileaList)
#print(fileaString[:-idPosition])
#print(idPosition)
#filea.seek(idPosition,0)               #將當前檔案讀寫位置設定到想要改寫的地方
#filea.write("123")
#filea.write('\n')                  #將字串寫入，整數需要先更改成字串
#filea.write('!@#')
#print(fileaString)
#filea.close()                                       #關閉檔案
#filesPath = os.path.abspath('')
#i = 0 
#for line in fileaList:
  
  #line = line.split('\n')
  #print(line)
  #shutil.copy(line[i], filesPath)
  #i = i + 1


#os.chdir('C:\\')

