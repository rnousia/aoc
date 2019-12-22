import part2
import unittest
 
class TestDay7Part2(unittest.TestCase):
    """
    Test function execute_sequence_with_settings
    """

    def test_execute_sequence_with_settings(self):
		# Test case 1
        sequence = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        result = part2.execute_sequence_with_settings(sequence, [9,8,7,6,5])
        self.assertEqual(result, 139629729)
    
      	# Test case 2
        sequence = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
        result = part2.execute_sequence_with_settings(sequence, [9,7,8,5,6])
        self.assertEqual(result, 18216)
 
 
if __name__ == '__main__':
    unittest.main()