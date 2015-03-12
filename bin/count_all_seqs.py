#!/usr/bin/env python

import sys
import os.path
import glob
import seq_utils

if len(sys.argv) != 2:
    sys.exit("Usage: {} <directory name>".format(os.path.basename(sys.argv[0])))

dirname = sys.argv[1]
if not os.path.isdir(dirname):
    sys.exit("{} is not a directory!".format(dirname))

pattern = '*.fasta'
path_pattern = os.path.join(dirname, pattern)
for filepath in sorted(glob.glob(path_pattern)):
    filename = os.path.basename(filepath)
    try:
        input_file = open(filepath)
    except IOError as e:
        print >>sys.stderr, "Failed to open {}: {}".format(filepath, e.strerror)
    else:
        seq_count = seq_utils.count_seqs(input_file)
        print filename, seq_count
