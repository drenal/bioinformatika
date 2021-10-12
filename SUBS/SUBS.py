#!/usr/bin/env python3
"""
Rosalind problem SUSBS http://rosalind.info/problems/subs/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import search_motif
import re

dna = ""
motif = ""
with open(sys.argv[1], "r") as inputfh:
    for l in inputfh:
        if len(dna) == 0:
            dna = l.strip()
        else:
            motif = l.strip()

# re's algo
print(" ".join([str(m.start()+1) for m in re.finditer('(?=' + motif +')', dna)]))

# own algorithm
print(" ".join(str(i) for i in search_motif(dna,motif)))
