from part2 import Computer
import unittest
 
class TestIntcodeComputer(unittest.TestCase):
    """
    Test Intcode computer
    """

    def test_opcode1(self):
        # Test with position mode: value at index 4 + value at index 0 = 4 + 1 = 5
        computer = Computer([1, 4, 0, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 5)

        # Test with position and immediate mode: value at index 4 + value 2 = 4 + 2 = 6
        computer = Computer([1001, 4, 2, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 6)

        # Test with relative base mode: first add 1 to relative base
        # Then calculate: value at index 5 (7 + relative base) + value 2 = 99 + 2 = 101
        computer = Computer([9, 1, 1201, 7, 2, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 101)

    def test_opcode2(self):
        # Test with position mode: value at index 4 * value at index 0 = 4 * 2 = 8
        computer = Computer([2, 4, 0, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 8)

        # Test with position and immediate mode: value at index 4 * value 3 = 4 * 3 = 12
        computer = Computer([1002, 4, 3, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 12)

        # Test with relative base mode: first add 1 to relative base
        # Then calculate: value at index 5 (7 + relative base) + value 2 = 99 * 2 = 101
        computer = Computer([9, 1, 1202, 7, 2, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 198)

    def test_opcode3(self):
        # Test with position mode: save input value to index 0
        computer = Computer([3, 0, 4, 0, 99]).run()
        next(computer)
        # Should output the saved input: 198
        self.assertEqual(computer.send(198), 198)

        # Test with immediate mode: should work the same as first test
        computer = Computer([103, 0, 4, 0, 99]).run()
        next(computer)
        self.assertEqual(computer.send(198), 198)

        # Test with relative base mode: should save input value to index 1  (0 + relative base 1)
        computer = Computer([9, 1, 203, 0, 4, 1, 99]).run()
        next(computer)
        self.assertEqual(computer.send(198), 198)

    def test_opcode4(self):
        # Test with relative base mode: should ouput value from index 2 (0 + relative base 2)
        computer = Computer([9, 1, 204, 0, 99]).run()
        self.assertEqual(next(computer), 1)

    def test_opcode5(self):
        # Test with position mode: if value at index 1 is not 0,
        # set index to value 3 (value at index 4)
        computer = Computer([5, 1, 4, 4, 3, 99]).run()
        self.assertEqual(next(computer), 4)

        # Test with immediate mode: value is 0 -> do nothing
        computer = Computer([105, 0, 4, 4, 0, 99]).run()
        self.assertEqual(next(computer), 105)

    def test_opcode6(self):
        # Test with position mode: if value at index 2 is 0,
        # set index to value 6 (value at index 0)
        computer = Computer([6, 2, 0, -1, -1, -1, 4, 3, 99]).run()
        self.assertEqual(next(computer), -1)

        # Test with immediate mode: value is not 0 -> do nothing
        computer = Computer([106, 1, 4, 4, 0, 99]).run()
        self.assertEqual(next(computer), 106)

    # Opcode 7 is less than: if the first parameter is less than the second parameter,
    # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def test_opcode7(self):
        # Test with position mode: value at index 2 -> 0 is less than value at index 0 -> 7
        # Should store value 1 at index 0 and then print it
        computer = Computer([7, 2, 0, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 1)

        # Test with multiple modes
        computer = Computer([109, 2, 20107, 3, 2, -1, 4, 1, 99]).run()
        self.assertEqual(next(computer), 1)

        # Test with equal parameters -> should return 0
        computer = Computer([1107, 2, 2, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 0)
    
    # Opcode 8 is equals: if the first parameter is equal to the second parameter,
    # it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    def test_opcode8(self):
        # Test with position mode: value at index 2 -> 0 is not equal to value at index 0 -> 7
        # Should store value 0 at index 0 and then print it
        computer = Computer([8, 2, 0, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 0)

        # Test with multiple modes
        computer = Computer([109, 2, 20108, 3, 2, -1, 4, 1, 99]).run()
        self.assertEqual(next(computer), 0)

        # Test with equal parameters -> should return 1
        computer = Computer([1108, 2, 2, 0, 4, 0, 99]).run()
        self.assertEqual(next(computer), 1)

 
if __name__ == '__main__':
    unittest.main()