import part1
import unittest
 
class TestDay7Part1(unittest.TestCase):
    """
    Test function execute_sequence_with_settings
    """
 
    def test_execute_sequence_with_settings(self):
		# Test case 1
        sequence = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        result = part1.execute_sequence_with_settings(sequence, [4,3,2,1,0])
        self.assertEqual(result, 43210)
    
      	# Test case 2
        sequence = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        result = part1.execute_sequence_with_settings(sequence, [0,1,2,3,4])
        self.assertEqual(result, 54321)
    
      	# Test case 3
        sequence = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        result = part1.execute_sequence_with_settings(sequence, [1,0,4,3,2])
        self.assertEqual(result, 65210)
 
 
if __name__ == '__main__':
    unittest.main()