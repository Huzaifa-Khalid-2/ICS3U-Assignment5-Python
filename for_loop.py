#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This module uses a for loop with user input


def main():
    # this function uses a for loop
    counter = 0
    odd = 0
    even = 0

    # input
    number_as_string = input("How many numbers do you want to add: ")
    print("")

    # process & output
    try:
        number_as_integer = int(number_as_string)
        for counter in range(number_as_integer):
            second_string = input("Enter your number: ")
            print("")
            second_integer = int(second_string)
            if second_integer % 2 == 0:
                even = even + second_integer
            else:
                odd = odd + second_integer
        print("The sum of all even numbers is = {0}.".format(even))
        print("The sum of all odd numbers is = {0}.".format(odd))

    except Exception:
        print("Invalid input, you plonker.")

    print("\nDone.")


if __name__ == "__main__":
    main()
