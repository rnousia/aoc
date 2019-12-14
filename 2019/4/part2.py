'''
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''

def check_password(password):
    digit_list = list(str(password))
    # Check: going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if digit_list == sorted(digit_list):
        # Check: two adjacent digits are the same (like 22 in 122345)
        if len(set(digit_list)) < len(digit_list):
            # Check: the two adjacent matching digits are not part of a larger group of matching digits
            counts = [digit_list.count(x) for x in set(digit_list)]
            if 2 in counts:
                return True
    return False


def count_possible_passwords(min, max):
    count = 0
    for number in range(min, max):
        if check_password(number):
            count += 1
    return count


def main():
    print(count_possible_passwords(171309, 643603))


if __name__== "__main__":
    main()

