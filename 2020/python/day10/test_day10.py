import part2


def test_count_num_arrangements_with_small_dataset():
    test_adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

    assert part2.count_num_arrangements(test_adapters) == 8


def test_count_num_arrangements_with_bigger_dataset():
    test_adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49,
                     45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]

    assert part2.count_num_arrangements(test_adapters) == 19208
