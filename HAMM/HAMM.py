#!/usr/binenv python3
"""
Rosalind problem HAMM http://rosalind.info/problems/hamm/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import hamm_dist

s1 = s2 =""
with open(sys.argv[1], "r") as inputfh:
    for l in inputfh:
        if len(s1) == 0:
            s1 = l.strip()
        else:
            s2 = l.strip()

print(str(hamm_dist(s1,s2)))
