#!/usr/bin/env python2.7

import unittest
from dnaseqlib import *

### Utility classes ###

# Maps integer keys to a set of arbitrary values.


class Multidict:
    # Initializes a new multi-value dictionary, and adds any key-value
    # 2-tuples in the iterable sequence pairs to the data structure.
    def __init__(self, pairs=[]):
        self.multidict = {}
        for pair in pairs:
            self.put(pair[0], pair[1])
    # Associates the value v with the key k.

    def put(self, k, v):
        if k in self.multidict.keys():
            self.multidict[k] += [v]
        else:
            self.multidict[k] = [v]

    # Gets any values that have been associated with the key k; or, if
    # none have been, returns an empty sequence.

    def get(self, k):
        if k in self.multidict.keys():
            return self.multidict[k]
        else:
            return []

# Given a sequence of nucleotides, return all k-length subsequences
# and their hashes.  (What else do you need to know about each
# subsequence?)


def subsequenceHashes(seq, k):
    assert k > 0
    try:
        subseq = ''
        while len(subseq) < k:
            subseq += seq.next()
        subseqHash = RollingHash(subseq)
        pos = 0
        while True:
            yield (subseqHash.current_hash(), (pos, subseq))
            previtm = subseq[0]
            subseq = subseq[1:] + seq.next()
            subseqHash.slide(previtm, subseq[-1])
            pos += 1
    except StopIteration:
        return

# Similar to subsequenceHashes(), but returns one k-length subsequence
# every m nucleotides.  (This will be useful when you try to use two
# whole data files.)


def intervalSubsequenceHashes(seq, k, m):
    assert m >= k
    try:
        pos = 0
        while True:
            subseq = ''
            while len(subseq) < k:
                subseq += seq.next()
            subseqHash = RollingHash(subseq)
            yield(subseqHash.current_hash(), (pos, subseq))
            for i in range(0, m - k):
                seq.next()
            pos += m
    except StopIteration:
        return

# Searches for commonalities between sequences a and b by comparing
# subsequences of length k.  The sequences a and b should be iterators
# that return nucleotides.  The table is built by computing one hash
# every m nucleotides (for m >= k).


def getExactSubmatches(a, b, k, m):
    try:
        print("Building hashing table for sequence A ....")
        hashTableA = Multidict(intervalSubsequenceHashes(a, k, m))
        print(".... Done building hash table.")
        for hashB, (posB, subseqB) in subsequenceHashes(b, k):
            for posA, subseqA in hashTableA.get(hashB):
                if subseqA != subseqB:
                    continue
                yield(posA, posB)
    except StopIteration:
        return


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print 'Usage: {0} [file_a.fa] [file_b.fa] [output.png]'.format(sys.argv[0])
        sys.exit(1)

    # The arguments are, in order: 1) Your getExactSubmatches
    # function, 2) the filename to which the image should be written,
    # 3) a tuple giving the width and height of the image, 4) the
    # filename of sequence A, 5) the filename of sequence B, 6) k, the
    # subsequence size, and 7) m, the sampling interval for sequence
    # A.
    compareSequences(getExactSubmatches, sys.argv[3], (500, 500), sys.argv[1], sys.argv[2], 8, 100)
