'''
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
'''

def check_password(password):
    digit_list = list(str(password))
    # Check: going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if digit_list == sorted(digit_list):
        # Check: Two adjacent digits are the same (like 22 in 122345)
        if len(set(digit_list)) < len(digit_list):
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


if __name__== '__main__':
    main()

