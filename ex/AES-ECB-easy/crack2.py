from pwn import *
import string

p = process("AES-ECB-easy.py")

def check(x):
  flag = "flag{" + x + "}"
  p.sendline(flag)
  r = p.recvline()
  return "Nice" in r

flag_c = p.recvline()

print "FLAG CIFRATA " + flag_c

dic = "0123456789ABCDEF"
flag = util.iters.bruteforce(check, dic, 4, method="fixed")

print flag

p.interactive()
