#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program uses a while loop to do exponential functions


def main():
    # this function uses a while loop
    counter = 0
    sum_number = 0

    # input
    number_as_string = input("Enter a integer >= 0: ")
    # process & output
    print("")
    try:
        number_as_int = int(number_as_string)
        if number_as_int < 0:
            print(
                "The number can't be {0}. Positive numbers only".format(
                    number_as_string
                )
            )
        else:
            for counter in range(number_as_int + 1):
                sum_number = counter**2
                print("{0}² = {1}".format(counter, sum_number))
    except Exception:
        print("¯\(°_o)/¯ invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
