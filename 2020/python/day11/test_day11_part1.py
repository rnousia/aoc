import part1


def test_get_adjacent_seats_first_seat():
    seats = ['L.L.LL', 'LLL.LL']
    assert part1.get_adjacent_seats((0, 0), seats) == ['L.', 'LL']


def test_get_adjacent_seats_last_seat_in_row():
    seats = ['L.L.LL', 'LLL.LL']
    assert part1.get_adjacent_seats((0, 5), seats) == ['LL', 'LL']


def test_get_adjacent_seats_middle_seat():
    seats = ['L.L.LL', 'LLL.LL', 'L.L...']
    assert part1.get_adjacent_seats((1, 1), seats) == ['L.L', 'LLL', 'L.L']


def test_get_adjacent_seats_last_seat():
    seats = ['L.L.LL', 'LLL.LL']
    assert part1.get_adjacent_seats((1, 5), seats) == ['LL', 'LL']


def test_get_adjacent_seats_first_seat_in_last_row():
    seats = ['L.L.LL', 'LLL.LL']
    assert part1.get_adjacent_seats((1, 0), seats) == ['L.', 'LL']
