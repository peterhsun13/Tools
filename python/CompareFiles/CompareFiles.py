#!/usr/bin/python
#coding: utf-8
from os import walk
from os.path import join
from datetime import datetime
import os, time

#mtime = time.ctime(os.stat("D:/datetime.txt").st_mtime) #文件修改時間 
#ctime = time.ctime(os.stat("D:/datetime.txt").st_ctime) #文件原始時間

# 指定要列出所有檔案的目錄
loop = True
while loop:
  choose = ''
  choose = input('1：FilesBackup 2：FilesNew 3:FilesCompare 4:Exit \n')
  if choose == '1':
    myPathBackup = ''
    myPathBackup = input('請輸入路徑：')    #mypath = "G:\\NEW"
    filesBackup = open('FilesBackup.txt', 'w+', encoding = 'utf8')
    for root, dirs, files in walk(myPathBackup): # 遞迴列出所有檔案的絕對路徑
      for f in files:
        fullPathBackup = join(root, f)
        mtime = str(datetime.fromtimestamp(os.stat(fullPathBackup).st_mtime)) #文件的修改时间
        #print(fullpath,mtime)
        filesBackup.write(str(fullPathBackup.encode('utf-8').decode('utf-8')) + '|' + mtime + '\n')
        #fullpathstr = str(fullpath.encode())
        #print(f'{str(fullpath.encode())}', file = files)
    filesBackup.close()
  elif choose == '2':
    myPathNew = ''
    myPathNew = input('請輸入路徑：')
  #mypath = "G:\\NEW"
    filesNew = open('FilesNew.txt', 'w+', encoding = 'utf8')
    for root, dirs, files in walk(myPathNew): # 遞迴列出所有檔案的絕對路徑
      for f in files:
        fullPathNew = join(root, f)
        mtime = str(datetime.fromtimestamp(os.stat(fullPathNew).st_mtime)) #文件的修改时间 
        #print(fullpath,mtime)
        filesNew.write(str(fullPathNew.encode('utf-8').decode('utf-8')) + '|' + mtime + '\n')
        #fullpathstr = str(fullpath.encode())
        #print(f'{str(fullpath.encode())}', file = files)
    filesNew.close()
  elif choose == '3':
    filesBackup = open('FilesBackup.txt', 'r', encoding = 'utf8')
    filesNew = open('FilesNew.txt', 'r', encoding = 'utf8')
    dff = set(filesBackup).symmetric_difference(filesNew)
    #dff.discard('\n')
    filesCompare = open('FilesCompare.txt', 'w', encoding = 'utf8')
    for line in dff:
      filesCompare.write(line + '\n')
    filesBackup.close()
    filesNew.close()
    filesCompare.close()
  elif choose == '4':
    print('Bye~')
    loop = False
  else :
    print('無此功能')