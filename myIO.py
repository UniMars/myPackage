'''
Author: your name
Date: 2020-11-01 18:35:16
LastEditTime : 2020-11-06 11:06:55
LastEditors  : UniMars
Description: In User Settings Edit
FilePath: \\python\\myPackage\\myIO.py
'''


import sys

sys.path.append(r'E:/Programs/Code/python')
import myPackage.myEncoding


'''
Description: write in files with your file path && text && encoding && mode in one function
param {str} path
param {str} text
param {*} my_encoding
param {*} mode
return {*}
'''
def my_write(path: str, text: str,my_encoding='utf-8',mode='a+') -> None:
    default_encoding = myPackage.myEncoding.judge_encoding(path)
    if default_encoding != my_encoding:
        myPackage.myEncoding.change_encoding(path, default_encoding, my_encoding)
        default_encoding = my_encoding
    with open(path, mode, encoding=my_encoding) as f:
        f.write(text)
    pass