#!/usr/bin/env python

import sys
import seq_utils
import os
import os.path

if len(sys.argv) < 2:
   exit ('specify sequence')

directory = sys.argv[1]
#filename = 'python.fasta'
for filenames in os.listdir(directory):
    input_file = open(os.path.join(directory, filenames))
    seq_count = seq_utils.count_seqs(input_file)
    print filenames, seq_count


