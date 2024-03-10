import pyperclip3

s = pyperclip3.paste()
t = s.split()
l = [chr(int(u, 16)) for u in t]
flag = ''.join(l)
pyperclip3.copy(flag)
