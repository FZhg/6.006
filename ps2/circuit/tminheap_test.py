import unittest
from circuit import MinHeap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        pass

    def test1_min_heapify(self):
        notMinHeapified = [0, 1, 16, 8, 39, 26, 4, 3, 16]
        MinHeapified = [0, 1, 16, 3, 39, 26, 4, 8, 16]
        heap = MinHeap()
        heap.assign_min_heap_list(notMinHeapified)
        heap.min_heapify(3)
        self.assertEqual(heap.get_min_heap(), MinHeapified)

    def test2_min_heapify(self):
        notMinHeapified = [0, 15, 7, 12, 10, 11, 17]
        MinHeapified = [0, 7, 10, 12, 15, 11, 17]
        heap = MinHeap()
        heap.assign_min_heap_list(notMinHeapified)
        heap.min_heapify(1)
        self.assertEqual(heap.get_min_heap(), MinHeapified)

    def test3_heap_decrease_key(self):
        minHeapified = [0, 7, 10, 12, 15, 11, 17]
        heap = MinHeap()
        heap.assign_min_heap_list(minHeapified)
        heap.heap_decrease_key(6, 5)
        self.assertEqual(heap.get_min_heap(), [0, 5, 10, 7, 15, 11, 12])

    def test4_min_heap_insert(self):
        minHeapified = [0, 7, 10, 12, 15, 11, 17]
        heap = MinHeap()
        heap.assign_min_heap_list(minHeapified)
        heap.min_heap_insert(5)
        self.assertEqual(heap.get_min_heap(), [0, 5, 10, 7, 15, 11, 17, 12])

    def test5_get_min(self):
        minHeapified = [0, 7, 10, 12, 15, 11, 17]
        heap = MinHeap()
        heap.assign_min_heap_list(minHeapified)
        self.assertEqual(heap.get_min(), 7)

    def test6_extract_heap_min(self):
        minHeapified = [0, 7, 10, 12, 15, 11, 17]
        heap = MinHeap()
        heap.assign_min_heap_list(minHeapified)
        self.assertEqual(heap.extract_heap_min(), 7)
        self.assertEqual(heap.get_min_heap(), [0, 10, 11, 12, 15, 17])


if __name__ == '__main__':
    unittest.main()
