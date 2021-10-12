#!/usr/bin/env python3

def revc(dna):
    reverse_dna = dna[::-1]
    reverse_complementer_dna = ""
    for n in reverse_dna:
        n = n.strip()
        if n == "A":
            n = "T"
        elif n == "T":
            n = "A"
        elif n == "C":
            n = "G"
        elif n == "G":
            n = "C"
        reverse_complementer_dna += n            
    return reverse_complementer_dna


def read_in_file_as_string(filename):
    content = ""
    with open(filename, "r") as inputfh:
        content = inputfh.read()
    return content


def count_letters(s):
    counts = {}
    for letter in s:
        counts.setdefault(letter, 0)
        counts[letter] += 1
    return counts

def count_letter_percentages(s):
    counts = count_letters(s)
    percentages = {}
    for c in counts:
        percentages[c] = counts[c] / len(s)
    return percentages

def dna_to_rna(dna):
    rna = ""
    for n in dna:
        n = n.strip()
        if n == "T":
            rna += "U"
        else:
            rna += n
    return rna
        

def read_fasta(filename):
    sequences = {}

    with open(filename, "r") as inputfh:
        current_sequence_name = ""
        current_sequence = ""
        for l in inputfh:
            line = l.strip()
            
            if line[0] == '>':
                if len(current_sequence_name) > 0:
                    sequences[current_sequence_name] = current_sequence
                    current_sequence_name=""
                    current_sequence=""
                current_sequence_name = line[1:]
            else:
                current_sequence += line
        sequences[current_sequence_name] = current_sequence
    return sequences

def fibonacci(F, i, n, k):
    if i < n:
        F.append(F[i-1] + k * F[i-2])
        F = fibonacci(F, i+1, n, k)
    return F

def codon_to_aa(codon):
    rna_codon_table = {
            "UUU": "F",   "CUU": "L",   "AUU": "I",   "GUU": "V",
            "UUC": "F",   "CUC": "L",   "AUC": "I",   "GUC": "V",
            "UUA": "L",   "CUA": "L",   "AUA": "I",   "GUA": "V",
            "UUG": "L",   "CUG": "L",   "AUG": "M",   "GUG": "V",
            "UCU": "S",   "CCU": "P",   "ACU": "T",   "GCU": "A",
            "UCC": "S",   "CCC": "P",   "ACC": "T",   "GCC": "A",
            "UCA": "S",   "CCA": "P",   "ACA": "T",   "GCA": "A",
            "UCG": "S",   "CCG": "P",   "ACG": "T",   "GCG": "A",
            "UAU": "Y",   "CAU": "H",   "AAU": "N",   "GAU": "D",
            "UAC": "Y",   "CAC": "H",   "AAC": "N",   "GAC": "D",
            "UAA": "Stop","CAA": "Q",   "AAA": "K",   "GAA": "E",
            "UAG": "Stop","CAG": "Q",   "AAG": "K",   "GAG": "E",
            "UGU": "C",   "CGU": "R",   "AGU": "S",   "GGU": "G",
            "UGC": "C",   "CGC": "R",   "AGC": "S",   "GGC": "G",
            "UGA": "Stop","CGA": "R",   "AGA": "R",   "GGA": "G",
            "UGG": "W",   "CGG": "R",   "AGG": "R",   "GGG": "G"   
    }
    return rna_codon_table.get(codon, " ")

def rna_to_prot(rna):
    codon = ""
    aa = ""
    for r in rna:
        if len(codon) == 3:
            trans = codon_to_aa(codon)
            if trans == "Stop":
                break
            else:
                aa += trans
            codon = r
        else:
            codon += r
    return aa

def search_motif(s, m):
    positions = []
    buf = ""
    i = 0
    while True: 
        if buf == m:
            buf = ""
            positions.append(i - len(m) + 1)
            i = i - len(m) + 1

        c = s[i]

        if len(buf) == 0:
            if c == m[0]:
                buf += c
            else:
                buf = ""
        else:
            if c == m[len(buf)]:
                buf += c
            else:
                # roll back to the beginning
                # of the anticipated
                # but then failed trial of match
                i = i - len(buf)
                buf = ""
        i += 1
        if i >= len(s):
            break
    
    if buf == m:
        positions.append(i - len(m) + 1)

    return positions


def hamm_dist(s1, s2):
    dist = 0
    for i,c in enumerate(s1):
        if s1[i] != s2[i]:
            dist += 1
    return dist
