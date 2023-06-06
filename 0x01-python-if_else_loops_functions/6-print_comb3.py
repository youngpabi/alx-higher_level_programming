#!/usr/bin/python3
for num0 in range(0, 10):
    for num1 in range(num0 + 1, 10):
        if num0 == 8 and num1 == 9:
            print("{}{}".format(num0, num1))
        else:
            print("{}{}".format(num0, num1), end=", ")
