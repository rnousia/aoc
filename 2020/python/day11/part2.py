import os

SEAT_STATES = {'vacant': 'L', 'occupied': '#'}
FLOOR = '.'


class Seat():
    def __init__(self, state, position, seat_position_map):
        self.state = state
        self.row = position[0]
        self.col = position[1]
        self.visible_seat_positions = get_visible_seats(
            position, seat_position_map)

    def update_state(self, seat_map):
        visible_seats = [seat_map[i][j]
                         for i, j in self.visible_seat_positions]
        if is_vacant_seat(self.state) and count_occupied_seats(visible_seats) == 0:
            self.state = SEAT_STATES['occupied']
        elif not is_vacant_seat(self.state) and count_occupied_seats(visible_seats) >= 5:
            self.state = SEAT_STATES['vacant']


def is_vacant_seat(seat):
    return True if seat == SEAT_STATES['vacant'] else False


def count_occupied_seats(seat_map):
    return [seat for seat_row in seat_map for seat in seat_row].count(SEAT_STATES['occupied'])


def get_visible_seats(position, seat_position_map):
    row, col = position

    seats_left_to_right = seat_position_map[row]
    seats_front_to_back = [row[col] for row in seat_position_map]

    seats_diagonally_left_to_right = get_diagonal_seats(
        seat_position_map, position)
    seats_diagonally_right_to_left = get_diagonal_seats(
        seat_position_map, position, right_to_left=True)

    pos_on_diagonal = row
    if row - col > 0:
        pos_on_diagonal = col

    pos_on_rev_diagonal = row
    if (len(seats_left_to_right) - col - 1) - row < 0:
        pos_on_rev_diagonal = len(seats_left_to_right) - col - 1

    visible_seats = [
        find_first_seat(seats_left_to_right, col,
                        reverse=True),  # seat at left
        find_first_seat(seats_left_to_right, col),  # seat at right
        find_first_seat(seats_front_to_back, row,
                        reverse=True),  # seat at front
        find_first_seat(
            seats_front_to_back, row),  # seat at back
        find_first_seat(
            seats_diagonally_left_to_right, pos_on_diagonal, reverse=True),  # seat at front left
        find_first_seat(
            seats_diagonally_left_to_right, pos_on_diagonal),  # seat at back right
        find_first_seat(
            seats_diagonally_right_to_left, pos_on_rev_diagonal, reverse=True),  # seat at front right
        find_first_seat(seats_diagonally_right_to_left,
                        pos_on_rev_diagonal)  # seat at back left
    ]

    return [seat for seat in visible_seats if seat]


def get_diagonal_seats(matrix, position, right_to_left=False):
    col, row = position
    offset = row - col
    if right_to_left:
        offset = - row - col
        return [
            row[-i-offset] for i, row in enumerate(matrix) if 0 <= -i-offset < len(row)]
    return [
        row[i+offset] for i, row in enumerate(matrix) if 0 <= i+offset < len(row)]


def find_first_seat(seats, start_at, reverse=False):
    if len(seats) > 1:
        seats_to_check = seats
        if reverse:
            start_at = len(seats_to_check) - start_at - 1
            seats_to_check = seats[::-1]

        for seat in seats_to_check[start_at+1:]:
            if seat != FLOOR:
                return seat
    return None


def initialize_seats(seat_map):
    seats = []
    # Replace seats with their position as other seats vacancy is not important at init stage
    position_map = [[c for c in row] for row in seat_map]
    for i, seat_row in enumerate(seat_map):
        for j, seat_state in enumerate(seat_row):
            if is_seat(seat_state):
                position_map[i][j] = (i, j)

    # Initialize seat objects
    for i, seat_row in enumerate(seat_map):
        for j, seat_state in enumerate(seat_row):
            if is_seat(seat_state):
                seats.append(Seat(seat_state, (i, j), position_map))

    return seats


def is_seat(seat_state):
    return True if seat_state in SEAT_STATES.values() else False


def fill_seats(seats, seat_map):
    new_seat_map = [[c for c in row] for row in seat_map]
    for seat in seats:
        seat.update_state(seat_map)
        new_seat_map[seat.row][seat.col] = seat.state

    return [''.join(item) for item in new_seat_map]


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        seat_map = f.read().splitlines()

    seats = initialize_seats(seat_map)

    current_seat_map = seat_map.copy()
    previous_seat_map = []
    count = 0

    while ''.join(current_seat_map) != ''.join(previous_seat_map):
        previous_seat_map = current_seat_map.copy()
        current_seat_map = fill_seats(seats, previous_seat_map)
        count += 1

    print('Part 2 answer: ', count_occupied_seats(current_seat_map))


if __name__ == '__main__':
    main()
