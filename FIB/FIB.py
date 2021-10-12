#!/usr/bin/env python3
"""
Rosalind problem FIB: http://rosalind.info/problems/fib/
"""
import os
import sys
sys.path.append(os.path.abspath(".."))

from utils import fibonacci

n=int(sys.argv[1])
k=int(sys.argv[2])

F = [1,1]
F = fibonacci(F, 2, n, k)

print(F[-1])

