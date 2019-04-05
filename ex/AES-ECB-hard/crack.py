#!/bin/env python2.7

'''
  Choosen prefix attack on AES-ECB
  With more than one block
'''

from pwn import *
import string
import sys

p = process("AES-ECB-hard.py")

hashed = p.recvline().strip()

print ("f(FLAG) = "+hashed)

def enc(x):
  p.sendline(x)
  blocks = p.recvline()
  if "Nice" in blocks:
    print(blocks)
    sys.exit(0)
  return blocks.strip().split(" ")[1:]


flag = ""

for i in range(0, 80):

  for x in string.ascii_letters+"{}":
    toSend = ""
    toSend += "A" * (80-len(flag)-1) + flag + x
    assert(len(toSend) == 80)
    toSend += "A" * (80-len(flag)-1)

    blocks = enc(toSend)
    print(toSend + " -> ")
    print("\t" + " ".join(blocks[:5]))
    print("\t" + " ".join(blocks[5:10]))
    print("")
    if blocks[:5] == blocks[5:10]:
      print("FOUND " + flag + x)
      flag = flag+x
      break
    enc(flag)
	
print("")
print("FLAG = " + flag)
