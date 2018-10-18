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
        self.systemMessage = '1：BackupFiles \n 2：CurrentFiles \n 3:CompareFiles \n 4:CopyFiles \n 5:Exit \n'
        self.backUpFileName = 'BackupFiles.txt'
        self.newFileName = 'CurrentFiles.txt'
        self.compareFileName ='CompareFiles.txt'

        self.backUpFileNameKey = '1'
        self.newFileNameKey = '2'
        self.compareFileNameKey ='3'

        self.inputWording = '請輸入路徑：'

        self.systemLoop = True

    def main(self):
        while self.systemLoop:
            os.system('cls')
            featureSwtich = input(self.systemMessage)

            if featureSwtich == self.backUpFileNameKey:
                path = input(self.inputWording)
                content = self.scanPath(path)

                self.saveFileLog(self.backUpFileName, content)

                if self.checkFileLogIsEmpty(self.backUpFileName):
                    print(self.backUpFileName + '無資料')

            elif featureSwtich == self.newFileNameKey:
                path = input(self.inputWording)
                content = self.scanPath(path)

                self.saveFileLog(self.newFileNameKey, content)

                if self.checkFileLogIsEmpty(self.newFileNameKey):
                    print(self.newFileNameKey + '無資料')
            elif featureSwtich == self.compareFileNameKey:
                self.compareFile()
            elif featureSwtich == '5':
                print('Bye~')
                self.systemLoop = False
            else:
                print('無此功能')

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

    def checkFileLogIsEmpty(self, fileLogName):
        file = open(fileLogName, 'r', encoding='utf8')
        content = file.read()
        file.close()

        if len(content) == 0:
            return True
        return False

    def compareFile(self):
        try:
            backupFile = open(self.backUpFileName, 'r', encoding='utf8')
            newFile = open(self.newFileName, 'r', encoding='utf8')
            diff = set(backupFile).symmetric_difference(newFile)

            diffContent = ''
            for line in diff:
                diffContent = diffContent + line + 'n'

            self.saveFileLog(self.compareFileName, diffContent)

            if self.checkFileLogIsEmpty(self.compareFileName):
                print(self.compareFileName + '無資料')
        except FileNotFoundError:
            print('無' + self.backUpFileName + '、' + self.newFileName + '檔案')

    def copyFile(self):
        try:
            f = open('CompareFiles.txt', 'r+',
                     encoding='utf-8')  # 開啟檔案,須以r+讀寫模式
            filesString = f.read()
            if len(filesString) == 0:
                print('CompareFiles.txt裡無資料')
            f = open('CompareFiles.txt', 'r+', encoding='utf-8')
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

compareTool = CompareTool()
compareTool.main()