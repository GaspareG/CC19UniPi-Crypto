#!/bin/env python2.7

'''
  Choosen prefix attack on AES-ECB
  With one block
'''

from pwn import *
import string
import sys

p = process("AES-ECB-medium.py")

hashed = p.recvline().strip()

print ("f(FLAG) = "+hashed)

def enc(x):
  p.sendline(x)
  blocks = p.recvline()
  if "Nice" in blocks:
    return ["", ""]
  return blocks.strip().split(" ")[1:]


flag = ""

for i in range(0, 16):

  for x in string.ascii_letters+"{}":
    toSend = ""
    toSend += "A" * (16-len(flag)-1) + flag + x
    toSend += "A" * (16-len(flag)-1)

    blocks = enc(toSend)
    print(toSend + " -> " + " ".join(blocks))
    if blocks[0] == blocks[1]:
      print("FOUND " + flag + x)
      flag = flag+x
      break

print("FLAG = " + flag)
