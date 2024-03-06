import re
import os
import pyperclip3

def find_flag_in_file(filename: str):
    '''
    從文字檔中找尋 flag ，將找到的結果回複製到剪貼簿
    '''
    with open(filename, 'r') as f:   
        text = f.read()
        if 'picoCTF' in text:
            matches = re.findall(r'picoCTF\{.*?\}', text)
            pyperclip3.copy(matches[0])
        else:
            print('not found')

def find_flag_in_dir(directory_path: str):
    '''
    從資料夾中所有檔案找尋 flag
    '''
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            find_flag_in_file(file_path)

