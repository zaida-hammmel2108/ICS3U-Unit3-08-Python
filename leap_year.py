#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program determines if a year is a leap year.

import random


def main():
    # this function determines if your year is a leap year.

    # input
    str_year = input("Enter a year: ")

    # process
    try:
        int_year = int(str_year)
        if int_year < 0:
            print("Invalid year")
        else:
            if int_year % 4 == 0 or int_year % 400 == 0:
                if int_year % 100 == 0 and int_year % 400 != 0:
                    print("This year is not a leap year")
                else:
                    print("This year is a leap year.")
            else:
                print("This year is not leap year.")
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thank you for playing!")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
