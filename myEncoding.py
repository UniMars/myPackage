'''
Author       : UniMars
Date         : 2020-11-01 22:00:28
LastEditors  : UniMars
LastEditTime : 2020-11-01 22:24:14
Description  : file head
'''
import chardet


def judge_encoding(path: str) -> str:
    with open(path, 'a+') as f:
        f.write('')
    with open(path, 'rb') as f:
        c = chardet.detect(f.read())
    return c['encoding']

def change_encoding(path: str, old_encoding: str, new_encoding: str) -> None:
    with open(path, 'r', encoding=old_encoding) as f:
        text = f.read()
    with open(path, 'w+', encoding=new_encoding) as f:
        f.write(text)
    pass
