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

class CompareTool():
    def __init__(self):
        self.systemMessage = '1：BackupFiles \n 2：CurrentFiles \n 3:CompareFiles \n 4:CopyFiles 5:Exit \n'
        self.backUpFileName = 'BackupFiles.txt'
        self.newFileName = 'CurrentFiles.txt'
        self.compareFileName ='CompareFiles.txt'
        self.inputWording = '請輸入路徑：'

    def scanPath(self, filePath):
        content = ''
        for root, dirs, files in walk(filePath):  # 遞迴列出所有檔案的絕對路徑
            for f in files:
                fullPathBackup = join(root, f)
                fileModifyTime = str(datetime.fromtimestamp(os.stat(fullPathBackup).st_mtime))
                content = content + str(fullPathBackup.encode('utf-8').decode('utf-8')) + '|' + fileModifyTime + '\n'
        return content

    def saveFileLog(self, fileLogName, content):
        file = open(fileLogName, 'w+', encoding='utf8')
        file.write(content)
        file.close()


loop = True
while loop:
    choose = ''
    choose = input(
        '1：BackupFiles 2：CurrentFiles 3:CompareFiles 4:CopyFiles 5:Exit \n')
    if choose == '1':
        myPathBackup = ''
        myPathBackup = input('請輸入路徑：')
        backupFiles = open('BackupFiles.txt', 'w+', encoding='utf8')
        for root, dirs, files in walk(myPathBackup):  # 遞迴列出所有檔案的絕對路徑
            for f in files:
                fullPathBackup = join(root, f)
                mtime = str(datetime.fromtimestamp(
                    os.stat(fullPathBackup).st_mtime))

                backupFiles.write(str(fullPathBackup.encode(
                    'utf-8').decode('utf-8')) + '|' + mtime + '\n')

        backupFiles = open('BackupFiles.txt', 'r', encoding='utf8')
        backupString = backupFiles.read()
        backupFiles.close()
        if len(backupString) == 0:
            print('BackupFiles.txt裡無資料')
    elif choose == '2':
        myPathNew = ''
        myPathNew = input('請輸入路徑：')  # mypath = "G:\\NEW"
        currentFiles = open('CurrentFiles.txt', 'w+', encoding='utf8')
        for root, dirs, files in walk(myPathNew):  # 遞迴列出所有檔案的絕對路徑
            for f in files:
                fullPathCurrent = join(root, f)
                mtime = str(datetime.fromtimestamp(
                    os.stat(fullPathCurrent).st_mtime))  # 文件的修改时间
                currentFiles.write(str(fullPathCurrent.encode(
                    'utf-8').decode('utf-8')) + '|' + mtime + '\n')

        currentFiles = open('CurrentFiles.txt', 'r', encoding='utf8')
        currentString = currentFiles.read()
        currentFiles.close()
        if len(currentString) == 0:
            print('CurrentFiles.txt裡無資料')
    elif choose == '3':
        try:
            backupFiles = open('BackupFiles.txt', 'r', encoding='utf8')
            currentFiles = open('CurrentFiles.txt', 'r', encoding='utf8')
            dff = set(backupFiles).symmetric_difference(currentFiles)
            compareFiles = open('CompareFiles.txt', 'w', encoding='utf8')
            for line in dff:
                compareFiles.write(line + '\n')
            backupFiles.close()
            currentFiles.close()
            compareFiles = open('CompareFiles.txt', 'r', encoding='utf8')
            compareString = compareFiles.read()
            compareFiles.close()
            if len(compareString) == 0:
                print('CompareFiles.txt裡無資料')
        except FileNotFoundError:
            print('無BackupFiles.txt、CurrentFiles.txt檔案')
    elif choose == '4':
        try:
            f = open('CompareFiles.txt', 'r+',
                     encoding='utf-8')  # 開啟檔案,須以r+讀寫模式
            filesString = f.read()
            if len(filesString) == 0:
                print('CompareFiles.txt裡無資料')
            f = open('CompareFiles.txt', 'r+',
                     encoding='utf-8')
            filesList = f.readlines()
            makeDirectory = os.getcwd()
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
                        shutil.copy(filesPath, makeDirectory+makeDirPath[:-1])
                    except FileNotFoundError:
                        print(filesPath + '此為刪除的檔案')
                    except:
                        print('不明錯誤')
            f.close()
        except FileNotFoundError:
            print('無CopareFiles.txt')
        except NameError:
            print('無CopareFiles.txt')
    elif choose == '5':
        print('Bye~')
        loop = False
    else:
        print('無此功能')
