'''
Author: your name
Date: 2020-11-01 18:35:16
LastEditTime : 2020-11-03 12:09:59
LastEditors  : UniMars
Description: In User Settings Edit
FilePath: \\python\\myPackage\\myIO.py
'''


import sys

sys.path.append(r'E:/Programs/Code/python')
import myPackage.myEncoding


def my_write(path: str, text: str,encoding: str) -> None:
    encoding = myPackage.myEncoding.judge_encoding(path)
    if encoding != encoding:
        myPackage.myEncoding.change_encoding(path, encoding, encoding)
        encoding = encoding
    with open(path, 'a+', encoding=encoding) as f:
        f.write(text)
    pass