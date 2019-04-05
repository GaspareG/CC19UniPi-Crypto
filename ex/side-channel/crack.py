#!/usr/bin/python2.7

'''
  time-based side-channel attack
'''

from __future__ import print_function
from pwn import *
import time

p = process("side-channel.py")

dic = string.ascii_letters + "{}"
flag = ""

for i in range(16):
  mt = 0
  mc = 0

  for x in dic:
    p.sendline(flag+x)
    t0 = time.time()
    p.recvline(20)
    t1 = time.time()
    print(flag+x, " = ", t1-t0)
    if t1-t0 > mt:
      mt = t1-t0
      mc = x
	
  flag += mc
  print("FLAG = "+flag)
