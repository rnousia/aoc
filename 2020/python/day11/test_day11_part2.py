import part2


def test_get_visible_seats_on_left():
    seats = ['L.#.L.']
    assert part2.get_visible_seats((0, 4), seats) == ['#']


def test_get_visible_seats_on_right():
    seats = ['...L.#']
    assert part2.get_visible_seats((0, 3), seats) == ['#']


def test_get_visible_seats_at_front():
    seats = ['.#.', '.L.', '...', '...']
    assert part2.get_visible_seats((1, 1), seats) == ['#']


def test_get_visible_seats_at_back():
    seats = ['...', '...', '.L.', '.#.']
    assert part2.get_visible_seats((2, 1), seats) == ['#']


def test_get_visible_seats_diagonally_front_left():
    seats = ['L.L', '#..', '.L.', '...']
    assert part2.get_visible_seats((2, 1), seats) == ['#']


def test_get_visible_seats_diagonally_front_right():
    seats = ['L.L', '..#', '.L.', '...']
    assert part2.get_visible_seats((2, 1), seats) == ['#']


def test_get_visible_seats_diagonally_back_left():
    seats = ['...', '...', '.L.', '#..']
    assert part2.get_visible_seats((2, 1), seats) == ['#']


def test_get_visible_seats_diagonally_back_right():
    seats = ['...', '...', '.L.', '..#']
    assert part2.get_visible_seats((2, 1), seats) == ['#']


def test_get_visible_seats_diagonally_right_corner():
    seats = ['..#..', '..L.#', '..#.L', '....#']
    assert part2.get_visible_seats((2, 4), seats) == ['#', '#', '#', '#']


def test_get_visible_seats_diagonally_left_corner():
    seats = ['#.L..', 'L...#', '#...L', '..#..']
    assert part2.get_visible_seats((1, 0), seats) == ['#', '#', '#', '#']


def test_get_visible_seats_multiple_horizontal():
    seats = ['..L.', '....', '#L.#', '...L']
    assert part2.get_visible_seats((2, 1), seats) == ['#', '#']


def test_get_visible_seats_multiple_vertical():
    seats = ['.LL.', '.#..', '.L..', '.#.L']
    assert part2.get_visible_seats((2, 1), seats) == ['#', '#']


def test_get_visible_seats_multiple_diagonal():
    seats = ['...', '#.#', '.L.', '#.#']
    assert part2.get_visible_seats((2, 1), seats) == ['#', '#', '#', '#']


def test_get_visible_seats_multiple():
    seats = ['.#.#', '#...', '#L#.', '.#.L']
    assert part2.get_visible_seats((2, 1), seats) == [
        '#', '#', '#', '#', '#', '#']


def test_get_diagonal_seats_left_to_right():
    matrix = ['1234', 'abcd', '5678', 'ABCD']
    assert part2.get_diagonal_seats(matrix, (0, 0), False) == '1b7D'
    assert part2.get_diagonal_seats(matrix, (2, 2), False) == '1b7D'
    assert part2.get_diagonal_seats(matrix, (1, 2), False) == '2c8'
    assert part2.get_diagonal_seats(matrix, (0, 3), False) == '4'
    assert part2.get_diagonal_seats(matrix, (2, 0), False) == '5B'


def test_get_diagonal_seats_right_to_left():
    matrix = ['1234', 'abcd', '5678', 'ABCD']

    assert part2.get_diagonal_seats(matrix, (0, 0), True) == '1'
    assert part2.get_diagonal_seats(matrix, (2, 2), True) == 'd7B'
    assert part2.get_diagonal_seats(matrix, (1, 2), True) == '4c6A'
    assert part2.get_diagonal_seats(matrix, (0, 3), True) == '4c6A'
    assert part2.get_diagonal_seats(matrix, (2, 0), True) == '3b5'
