import part2


def test_has_valid_format():
    assert part2.has_valid_format('1234', r'^\d{4}$') == True
    assert part2.has_valid_format('123', r'^\d{4}$') == False
    assert part2.has_valid_format('1234', None) == True


def test_is_in_range():
    assert part2.is_in_range(1, [0,10]) == True
    assert part2.is_in_range(0, [0,10]) == True
    assert part2.is_in_range('5', [0,10]) == True
    assert part2.is_in_range(-1, [0,10]) == False
    assert part2.is_in_range(11, [0,10]) == False
    assert part2.is_in_range(11, None) == True


def test_is_in_values():
    assert part2.is_in_values(1, [1,2,3]) == True
    assert part2.is_in_values('1', ['1','2','3']) == True
    assert part2.is_in_values(0, [1,2,3]) == False
    assert part2.is_in_values(5, [1,2,3]) == False
    assert part2.is_in_range(1, None) == True


def test_is_valid_passport():
    invalid_passport1 = part2.parse_passpord('eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'.split(' '))
    assert part2.is_valid_passport(invalid_passport1) == False

    invalid_passport2 = part2.parse_passpord('iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946'.split(' '))
    assert part2.is_valid_passport(invalid_passport2) == False

    invalid_passport3 = part2.parse_passpord('hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277'.split(' '))
    assert part2.is_valid_passport(invalid_passport3) == False

    invalid_passport4 = part2.parse_passpord('hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007'.split(' '))
    assert part2.is_valid_passport(invalid_passport4) == False

    valid_passport1 = part2.parse_passpord('pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f'.split(' '))
    assert part2.is_valid_passport(valid_passport1) == True

    valid_passport2 = part2.parse_passpord('eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm'.split(' '))
    assert part2.is_valid_passport(valid_passport2) == True

    valid_passport3 = part2.parse_passpord('hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022'.split(' '))
    assert part2.is_valid_passport(valid_passport3) == True

    valid_passport4 = part2.parse_passpord('iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'.split(' '))
    assert part2.is_valid_passport(valid_passport4) == True