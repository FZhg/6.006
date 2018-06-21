from dnaseq import *
from kfasta import *

### Testing ###


class TestSubsequenceHashes(unittest.TestCase):
    """Test for SubsequenceHashes"""
    # def test_subqhash1(self):
    #     print("*************** test1 for subsequenceHashes *******************")
    #     seq = FastaSequence("trivial1.fa")
    #     for hash in subsequenceHashes(seq, 2):
    #         print(hash)

    # def test_subqhash2(self):
    #     seq = FastaSequence("trivial3.fa")
    #     hashes = []
    #     for hash in subsequenceHashes(seq, 2):
    #         hashes.append(hash)
    #     self.assertEqual(hashes, [672, 653, 1457, 6787])


class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('CTAGC')
        rh2 = RollingHash('TAGCG')
        rh3 = RollingHash('AGCGT')
        rh1.slide('C', 'G')
        self.assertTrue(rh1.current_hash() == rh2.current_hash())
        rh1.slide('T', 'T')
        self.assertTrue(rh1.current_hash() == rh3.current_hash())


class TestMultidict(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a', 'c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# This test case may break once you add the argument m (skipping).


class TestExactSubmatches(unittest.TestCase):
    def test_two(self):
        print("\n ****************** **************** \n")
        foo = 'yabcabcabcz'
        for hashVal, (pos, subseq) in intervalSubsequenceHashes(iter(foo), 3, 3):
            print(subseq)
            print(pos)
            print(hashVal)


    def test_one(self):
        foo = 'yabcabcabcz'
        bar = 'xxabcxxxx'
        matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 3))
        correct = [(1, 2), (4, 2), (7, 2)]
        print(matches)
        self.assertTrue(len(matches) == len(correct))
        for x in correct:
            self.assertTrue(x in matches)


unittest.main()
