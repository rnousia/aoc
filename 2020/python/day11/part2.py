import os


def fill_seats(seat_map):
    filled_seats = [[c for c in row] for row in seat_map.copy()]
    for i, seat_row in enumerate(seat_map):
        for j, seat in enumerate(seat_row):
            if is_seat(seat):
                visible_seats = get_visible_seats((i, j), seat_map)
                if is_vacant_seat(seat) and count_occupied_seats(visible_seats) == 0:
                    filled_seats[i][j] = '#'
                elif not is_vacant_seat(seat) and count_occupied_seats(visible_seats) >= 5:

                    filled_seats[i][j] = 'L'

    return [''.join(seats) for seats in filled_seats]


def is_seat(seat):
    return True if seat in ('L', '#') else False


def get_visible_seats(current_seat_index, seat_map):
    row, col = current_seat_index

    seats_left_to_right = seat_map[row]
    seats_front_to_back = ''.join([row[col] for row in seat_map])

    seats_diagonally_left_to_right = get_diagonal_seats(
        seat_map, current_seat_index)
    seats_diagonally_right_to_left = get_diagonal_seats(
        seat_map, current_seat_index, right_to_left=True)

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
        return ''.join([
            row[-i-offset] for i, row in enumerate(matrix) if 0 <= -i-offset < len(row)])
    return ''.join([
        row[i+offset] for i, row in enumerate(matrix) if 0 <= i+offset < len(row)])


def find_first_seat(seats, start_at, reverse=False):
    if len(seats) > 1:
        seats_to_check = seats
        if reverse:
            start_at = len(seats_to_check) - start_at - 1
            seats_to_check = seats[::-1]

        for seat in seats_to_check[start_at+1:]:
            if seat == '#' or seat == 'L':
                return seat
    return None


def is_vacant_seat(seat):
    return True if seat == 'L' else False


def count_occupied_seats(seat_map):
    return [seat for seat_row in seat_map for seat in seat_row].count('#')


def main():
    with open('{0}/input.txt'.format(os.path.dirname(os.path.realpath(__file__)))) as f:
        seat_map = f.read().splitlines()

    current_seat_map = seat_map.copy()
    previous_seat_map = []
    count = 0

    while ''.join(current_seat_map) != ''.join(previous_seat_map):
        previous_seat_map = current_seat_map.copy()
        current_seat_map = fill_seats(previous_seat_map)
        count += 1

    print('Part 2 answer: ', count_occupied_seats(current_seat_map))


if __name__ == '__main__':
    main()
