#!/usr/bin/env python3
"""
DNA problem: http://rosalind.info/problems/dna/
"""
import sys
import os
sys.path.append(os.path.abspath(".."))

from utils import read_in_file_as_string, count_letters

s = read_in_file_as_string(sys.argv[1])
counts = count_letters(s)
print("{} {} {} {}".format(counts["A"], counts["C"], counts["G"], counts["T"]))


