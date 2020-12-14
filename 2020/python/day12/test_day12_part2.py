import part2
import unittest


class TestCalculateDistance(unittest.TestCase):

    def test_calculate_distance1(self):
        x = 0
        y = 10
        self.assertEqual(part2.calculate_distance(x, y), 10)
        self.assertEqual(part2.calculate_distance(x, -y), 10)

    def test_calculate_distance2(self):
        x = 10
        y = 0
        self.assertEqual(part2.calculate_distance(x, y), 10)
        self.assertEqual(part2.calculate_distance(-x, y), 10)

    def test_calculate_distance3(self):
        x = 10
        y = 4
        self.assertEqual(
            round(part2.calculate_distance(x, y), 2), 10.77)
        self.assertEqual(
            round(part2.calculate_distance(-x, -y), 2), 10.77)
        self.assertEqual(
            round(part2.calculate_distance(x, -y), 2), 10.77)
        self.assertEqual(
            round(part2.calculate_distance(-x, y), 2), 10.77)


class TestCalculateAngle(unittest.TestCase):

    def test_calculate_angle(self):
        x = 4
        y = 1
        self.assertEqual(round(part2.calculate_angle(x, y)), 14)
        self.assertEqual(round(part2.calculate_angle(-x, y)), 166)
        self.assertEqual(round(part2.calculate_angle(-x, -y)), -166)
        self.assertEqual(round(part2.calculate_angle(x, -y)), -14)

    def test_calculate_angle_x_0(self):
        x = 0
        y = 4
        self.assertEqual(part2.calculate_angle(x, y), 90)
        self.assertEqual(part2.calculate_angle(x, -y), -90)

    def test_calculate_angle_y_0(self):
        x = 4
        y = 0
        self.assertEqual(part2.calculate_angle(x, y), 0)
        self.assertEqual(part2.calculate_angle(-x, y), 180)


class TestFerry(unittest.TestCase):
    def test_move_waypoint_right_from_right(self):
        ferry = part2.Ferry(4, 0)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, 0)
        self.assertEqual(ferry.waypoint.y, -4)
        self.assertEqual(ferry.waypoint.angle, -90)

    def test_move_waypoint_left_from_right(self):
        ferry = part2.Ferry(4, 0)
        ferry.apply_instruction('L', 180)
        self.assertEqual(ferry.waypoint.x, -4)
        self.assertEqual(ferry.waypoint.y, 0)
        self.assertEqual(ferry.waypoint.angle, 180)

    def test_move_waypoint_right_from_up_right(self):
        ferry = part2.Ferry(4, 1)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, 1)
        self.assertEqual(ferry.waypoint.y, -4)
        self.assertEqual(round(ferry.waypoint.angle), -76)

    def test_move_waypoint_left_from_up_right(self):
        ferry = part2.Ferry(4, 1)
        ferry.apply_instruction('L', 180)
        self.assertEqual(ferry.waypoint.x, -4)
        self.assertEqual(ferry.waypoint.y, -1)
        self.assertEqual(round(ferry.waypoint.angle), 194)

    def test_move_waypoint_left_from_up(self):
        ferry = part2.Ferry(0, 4)
        ferry.apply_instruction('L', 90)
        self.assertEqual(ferry.waypoint.x, -4)
        self.assertEqual(ferry.waypoint.y, 0)
        self.assertEqual(ferry.waypoint.angle, 180)

    def test_move_waypoint_right_from_up(self):
        ferry = part2.Ferry(0, 4)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, 4)
        self.assertEqual(ferry.waypoint.y, 0)
        self.assertEqual(ferry.waypoint.angle, 0)

    def test_move_waypoint_right_from_up_left(self):
        ferry = part2.Ferry(-4, 1)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, 1)
        self.assertEqual(ferry.waypoint.y, 4)
        self.assertEqual(round(ferry.waypoint.angle), 76)

    def test_move_waypoint_left_from_up_left(self):
        ferry = part2.Ferry(-4, 1)
        ferry.apply_instruction('L', 90)
        self.assertEqual(ferry.waypoint.x, -1)
        self.assertEqual(ferry.waypoint.y, -4)
        self.assertEqual(round(ferry.waypoint.angle), 256)

    def test_move_waypoint_right_from_left(self):
        ferry = part2.Ferry(-4, 0)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, 0)
        self.assertEqual(ferry.waypoint.y, 4)
        self.assertEqual(ferry.waypoint.angle, 90)

    def test_move_waypoint_left_from_left(self):
        ferry = part2.Ferry(-4, 0)
        ferry.apply_instruction('L', 90)
        self.assertEqual(ferry.waypoint.x, 0)
        self.assertEqual(ferry.waypoint.y, -4)
        self.assertEqual(ferry.waypoint.angle, 270)

    def test_move_waypoint_right_from_down_left(self):
        ferry = part2.Ferry(-1, -4)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, -4)
        self.assertEqual(ferry.waypoint.y, 1)
        self.assertEqual(round(ferry.waypoint.angle), -194)

    def test_move_waypoint_left_from_down_left(self):
        ferry = part2.Ferry(-1, -4)
        ferry.apply_instruction('L', 90)
        self.assertEqual(ferry.waypoint.x, 4)
        self.assertEqual(ferry.waypoint.y, -1)
        self.assertEqual(round(ferry.waypoint.angle), -14)

    def test_move_waypoint_left_from_down(self):
        ferry = part2.Ferry(0, -4)
        ferry.apply_instruction('L', 90)
        self.assertEqual(ferry.waypoint.x, 4)
        self.assertEqual(ferry.waypoint.y, 0)
        self.assertEqual(ferry.waypoint.angle, 0)

    def test_move_waypoint_right_from_down(self):
        ferry = part2.Ferry(0, -4)
        ferry.apply_instruction('R', 90)
        self.assertEqual(ferry.waypoint.x, -4)
        self.assertEqual(ferry.waypoint.y, 0)
        self.assertEqual(ferry.waypoint.angle, -180)
