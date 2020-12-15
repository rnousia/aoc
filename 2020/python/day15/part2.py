class NumberGame():
    def __init__(self, starting_numbers):
        self.numbers = {}
        for i, number in enumerate(starting_numbers):
            self.add_number(number, i)

    def add_number(self, value, index):
        if value not in self.numbers:
            self.numbers[value] = NumberToPlay(value, index)
        else:
            self.numbers[value].update(index)

        self.current_number = self.numbers[value]
        self.current_index = index

    def play_next_number(self):
        self.current_index += 1
        if self.current_number.count == 1:
            self.add_number(0, self.current_index)
        elif self.current_number.count > 1:
            self.add_number(self.current_number.index_step, self.current_index)


class NumberToPlay():
    def __init__(self, number, index):
        self.value = number
        self.count = 1
        self.current_index = index
        self.index_step = None

    def update(self, new_index):
        self.count += 1
        self.index_step = new_index - self.current_index
        self.current_index = new_index

    def __str__(self):
        return 'Value: {0}, count:{1}, current index:{2}'.format(self.value, self.count, self.current_index)


def main():
    # input
    starting_numbers = [16, 1, 0, 18, 12, 14, 19]
    # starting_numbers = [0, 3, 6]

    game = NumberGame(starting_numbers)

    for i in range(len(starting_numbers), 2020):
        # print(i)
        game.play_next_number()

    print('Part 2 answer: ', game.current_number.value)


if __name__ == '__main__':
    main()
