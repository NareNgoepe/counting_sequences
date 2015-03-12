#!/usr/bin/env python

def count_seqs(input_file):
    count = 0
    for line in input_file:
        line = line.lstrip() # strip leading spaces, if any
        if line.startswith('>'):
            count += 1
    return count
