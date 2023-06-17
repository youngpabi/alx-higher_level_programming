#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    nums = 0
    lasts = 0

    for letter in roman_string:
        for elemt in roman_letters:
            if letter == elemt[0]:
                if lasts == 0 or lasts >= elemt[1]:
                    nums += elemt[1]
                elif lasts < elemt[1]:
                    nums += elemt[1] - (lasts * 2)
                lasts = elemt[1]

    return nums
