#!/usr/bin/env python3

# Created by: Jonathan
# Created on: May 27, 2021
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of each number from the numbers amount

def main():
    # initialize the counter and sum
    counter = 0
    sum = 0
    #sum_string = ""

    # get the user number as a string
    num_of_nums_string = input("How many numbers do you want to add? ")
    print("")
    try:
        num_of_nums_int = int(num_of_nums_string)
        print("")
    except ValueError:
        print("Please enter a valid number")

    else:
        # calculate the sum of all numbers from 0 to user number
        if (num_of_nums_int < 0):
            print("Please enter a valid number")
        else:
            while (counter < num_of_nums_int):
                counter = counter + 1
                # get the user number as a string
                num_string = input("Enter a number: ")
                # check for any errors
                try:
                    num_int = int(num_string)
                except ValueError:
                    print("Please enter a valid number")
                else:
                    if(num_int <= 0):
                        print("{} is lower than 0, so"
                              "it was skipped". format(num_int))
                        continue
                    # calculate the sum
                    sum = sum + num_int
                finally:
                    print("The sum is {}". format(sum))
                    print("Thank you for your input")


if __name__ == "__main__":
    main()
