import part1
import unittest
 
class TestRunProgram(unittest.TestCase):
    """
    Test function execute_sequence_with_settings
    """
    
    def test_run_program(self):
        # Test case 1 should produce a copy of itself as output
        sequence = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        result = part1.run_program(sequence, input_value=None)
        self.assertListEqual(result, sequence)

        # Test case 2 should output a 16-digit number
        sequence = [1102,34915192,34915192,7,4,7,99,0]
        result = part1.run_program(sequence, input_value=1)
        self.assertEqual(len(str(result)), 16)

        # Test case 3 should output the large number in the middle (1125899906842624)
        sequence = [104,1125899906842624,99]
        result = part1.run_program(sequence, input_value=1)
        self.assertEqual(result, 1125899906842624)

  
if __name__ == '__main__':
    unittest.main()
