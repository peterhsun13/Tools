#!/usr/bin/python
# -*- coding: UTF-8 -*-

import shutil, os
#2017-04-02 14:11:53.570550
#filesCompare = open('FilesBackup.txt', 'r', encoding = 'utf8')
#filesCompare.read()
filea = open("filesCompare.txt", "r+", encoding = 'utf-8')          #開啟檔案,須以r+讀寫模式
filea2 = open("filesCompare2.txt", "w+", encoding = 'utf-8')
fileaString = filea.readlines()                    #將檔案讀成字串
#print(fileaString)
#filea.next()
#idFilter = '|'         #搜索檔案內特定的文字
#idPosition = fileaString.find(idFilter)  #抓出檔案內特定的文字位置
#print(idPosition)
#filea.seek(idPosition,0)               #將當前檔案讀寫位置設定到想要改寫的地方
#filea.write('\n')                  #將字串寫入，整數需要先更改成字串
#filea.write('!@#')
#print(fileaString)
#filea.close()                                       #關閉檔案
filesPath = os.path.abspath('')
i = 0 
for line in fileaString:
  line = line.split('\n')
  shutil.copy(line[i], filesPath)
  i = i + 1


#os.chdir('C:\\')

