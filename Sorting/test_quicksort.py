import unittest
from quicksort import quicksort  # Import the quicksort function

class TestQuicksort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])
    
    def test_single_element(self):
        self.assertEqual(quicksort([1]), [1])
    
    def test_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_list(self):
        self.assertEqual(quicksort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_unsorted_list(self):
        self.assertEqual(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), 
                         sorted([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    
    def test_list_with_duplicates(self):
        self.assertEqual(quicksort([4, 2, 4, 3, 4]), [2, 3, 4, 4, 4])
    
    def test_negative_numbers(self):
        self.assertEqual(quicksort([-3, -1, -4, -2, 0, -5]), 
                         sorted([-3, -1, -4, -2, 0, -5]))
    
    def test_mixed_numbers(self):
        self.assertEqual(quicksort([3, -1, 0, 5, -5, 2]), 
                         sorted([3, -1, 0, 5, -5, 2]))

if __name__ == "__main__":
    unittest.main()
