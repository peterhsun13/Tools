#!/usr/bin/python
#coding: utf-8
from os import walk
from os.path import join
from datetime import datetime
import os
import time
import shutil
import os
import sys
import os.path
#pyinstaller -F .\hello.py
# mtime = time.ctime(os.stat("D:/datetime.txt").st_mtime) #文件修改時間
# ctime = time.ctime(os.stat("D:/datetime.txt").st_ctime) #文件原始時間

# 指定要列出所有檔案的目錄
loop = True
while loop:
    choose = ''
    choose = input('1：BackupFiles 2：CurrentFiles 3:CompareFiles 4:CopyFiles 5:Exit \n')
    if choose == '1':
        myPathBackup = ''
        myPathBackup = input('請輸入路徑：')  # mypath = "G:\\NEW"
        BackupFiles = open('BackupFiles.txt', 'w+', encoding='utf8')
        for root, dirs, files in walk(myPathBackup):  # 遞迴列出所有檔案的絕對路徑
            for f in files:
                fullPathBackup = join(root, f)
                mtime = str(datetime.fromtimestamp(
                    os.stat(fullPathBackup).st_mtime))  # 文件的修改时间
                # print(fullpath,mtime)
                BackupFiles.write(str(fullPathBackup.encode(
                    'utf-8').decode('utf-8')) + '|' + mtime + '\n')
                #fullpathstr = str(fullpath.encode())
                #print(f'{str(fullpath.encode())}', file = files)
        BackupFiles.close()
    elif choose == '2':
        myPathNew = ''
        myPathNew = input('請輸入路徑：')
    #mypath = "G:\\NEW"
        CurrentFiles = open('CurrentFiles.txt', 'w+', encoding='utf8')
        for root, dirs, files in walk(myPathNew):  # 遞迴列出所有檔案的絕對路徑
            for f in files:
                fullPathCurrent = join(root, f)
                mtime = str(datetime.fromtimestamp(
                    os.stat(fullPathCurrent).st_mtime))  # 文件的修改时间
                # print(fullpath,mtime)
                CurrentFiles.write(str(fullPathCurrent.encode(
                    'utf-8').decode('utf-8')) + '|' + mtime + '\n')
                #fullpathstr = str(fullpath.encode())
                #print(f'{str(fullpath.encode())}', file = files)
        CurrentFiles.close()
    elif choose == '3':
        BackupFiles = open('BackupFiles.txt', 'r', encoding='utf8')
        CurrentFiles = open('CurrentFiles.txt', 'r', encoding='utf8')
        dff = set(BackupFiles).symmetric_difference(CurrentFiles)
        # dff.discard('\n')
        CompareFiles = open('CompareFiles.txt', 'w', encoding='utf8')
        for line in dff:
            CompareFiles.write(line + '\n')
        BackupFiles.close()
        CurrentFiles.close()
        CompareFiles.close()
    elif choose == '4':
        makeDirectory = os.getcwd()
        f = open("CompareFiles.txt", "r+", encoding='utf-8')  # 開啟檔案,須以r+讀寫模式
        filesList = f.readlines()
        currentPath = os.path.abspath('')
        for line in filesList:
            data = line.strip()
            if len(data) != 0:
                filesPath = data.split('|')[0]
                dirPath = filesPath.strip(filesPath.split('\\')[-1])
                makeDirPath = dirPath.strip(filesPath.split('\\')[0])
                # 如果有相同路徑不建立
                if not os.path.isdir(makeDirectory+makeDirPath[:-1]):
                    os.makedirs(makeDirectory+makeDirPath[:-1], 493)
                try:
                    # if os.path.isfile(filesPath):
                    shutil.copy(filesPath, makeDirectory+makeDirPath[:-1])
                except FileNotFoundError:
                    print(filesPath + '此為刪除的檔案')
                except:
                    print('不明錯誤')
        f.close()
    elif choose == '5':
        print('Bye~')
        loop = False
    else:
        print('無此功能')
