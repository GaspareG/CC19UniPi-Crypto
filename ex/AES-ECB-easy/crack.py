#!/bin/env python2.7

from pwn import *
import string

p = process("AES-ECB-easy.py")

flag = p.readline().strip()

def check(st):
  p.sendline("flag{"+st+"}")
  r = p.recvline().strip()
  return "Nice" in r

dic = "0123456789ABCDEF"
res =  util.iters.bruteforce(check, dic, method="fixed", length = 4)

print "FOUND: flag{%s}" % res
