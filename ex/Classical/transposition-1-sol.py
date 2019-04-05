#!/usr/bin/python2.7

import random
import itertools

msg2 = "L{NTP#AGLCSF.#OAR4A#STOL11__}PYCCTO1N#RS.S"
for perm in itertools.permutations(range(7)):
    msg = msg2
    for i in xrange(100):
        msg = msg[1:] + msg[:1]
        msg = msg[0::2] + msg[1::2]
        msg = msg[1:] + msg[:1]
        res = ""
        for j in xrange(0, len(msg), 7):
            for k in xrange(7):
                res += msg[j:j+7][perm[k]]
        msg = res
        if "FLAG" in msg:
            print(msg)
