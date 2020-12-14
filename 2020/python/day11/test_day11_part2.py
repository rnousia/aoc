import part2
import unittest


class TestGetVisibleSeats(unittest.TestCase):

    def test_get_visible_seats_on_left(self):
        seats = ['A.B.X.']
        self.assertEqual(part2.get_visible_seats((0, 4), seats), ['B'])

    def test_get_visible_seats_on_right(self):
        seats = ['...X.A']
        self.assertEqual(part2.get_visible_seats((0, 3), seats), ['A'])

    def test_get_visible_seats_at_front(self):
        seats = ['.A.', '.X.', '...', '...']
        self.assertEqual(part2.get_visible_seats((1, 1), seats), ['A'])

    def test_get_visible_seats_at_back(self):
        seats = ['...', '...', '.X.', '.A.']
        self.assertEqual(part2.get_visible_seats((2, 1), seats), ['A'])

    def test_get_visible_seats_diagonally_front_left(self):
        seats = ['A.B', 'C..', '.X.', '...']
        self.assertEqual(part2.get_visible_seats((2, 1), seats), ['C'])

    def test_get_visible_seats_diagonally_front_right(self):
        seats = ['A.B', '..C', '.X.', '...']
        self.assertEqual(part2.get_visible_seats((2, 1), seats), ['C'])

    def test_get_visible_seats_diagonally_back_left(self):
        seats = ['...', '...', '.X.', 'A..']
        self.assertEqual(part2.get_visible_seats((2, 1), seats), ['A'])

    def test_get_visible_seats_diagonally_back_right(self):
        seats = ['...', '...', '.X.', '..A']
        self.assertEqual(part2.get_visible_seats((2, 1), seats), ['A'])

    def test_get_visible_seats_diagonally_right_corner(self):
        seats = ['..A..', '..B.C', '..D.X', '....E']
        self.assertCountEqual(
            part2.get_visible_seats((2, 4), seats),
            ['A', 'C', 'D', 'E']
        )

    def test_get_visible_seats_diagonally_left_corner(self):
        seats = ['A.B..', 'X...C', 'D...E', '..F..']
        self.assertCountEqual(
            part2.get_visible_seats((1, 0), seats),
            ['A', 'C', 'D', 'F']
        )

    def test_get_visible_seats_multiple_horizontal(self):
        seats = ['..A.', '....', 'BX.C', '...D']
        self.assertCountEqual(
            part2.get_visible_seats((2, 1), seats),
            ['B', 'C']
        )

    def test_get_visible_seats_multiple_vertical(self):
        seats = ['.AB.', '.C..', '.X..', '.D.E']
        self.assertCountEqual(
            part2.get_visible_seats((2, 1), seats),
            ['C', 'D']
        )

    def test_get_visible_seats_multiple_diagonal(self):
        seats = ['...', 'A.B', '.X.', 'C.D']
        self.assertCountEqual(
            part2.get_visible_seats((2, 1), seats),
            ['A', 'B', 'C', 'D']
        )

    def test_get_visible_seats_multiple(self):
        seats = ['.A.B', 'C...', 'DXE.', '.F.G']
        self.assertCountEqual(
            part2.get_visible_seats((2, 1), seats),
            ['A', 'B', 'C', 'D', 'E', 'F']
        )


class TestGetDiagonalSeats(unittest.TestCase):

    def test_get_diagonal_seats_left_to_right(self):
        matrix = ['1234', 'abcd', '5678', 'ABCD']
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (0, 0), False), ['1', 'b', '7', 'D'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (2, 2), False), ['1', 'b', '7', 'D'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (1, 2), False), ['2', 'c', '8'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (0, 3), False), ['4'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (2, 0), False), ['5', 'B'])

    def test_get_diagonal_seats_right_to_left(self):
        matrix = ['1234', 'abcd', '5678', 'ABCD']

        self.assertEqual(part2.get_diagonal_seats(matrix, (0, 0), True), ['1'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (2, 2), True), ['d', '7', 'B'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (1, 2), True), ['4', 'c', '6', 'A'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (0, 3), True), ['4', 'c', '6', 'A'])
        self.assertEqual(part2.get_diagonal_seats(
            matrix, (2, 0), True), ['3', 'b', '5'])
