import sys

def permutations(a, l, r):  # Print all possible permutations
    if(l == r):  # base case
        print(a, end='')
        print(", ", end='')
    else:
        for i in range(l, r):  # swap each item with the item at position l
            tmp = a[l]  # initial swap
            a[l] = a[i]
            a[i] = tmp
            permutations(a, l+1, r)  # recursive call
            tmp = a[l]  # swap back to starting position
            a[l] = a[i]
            a[i] = tmp

nums = list()  # establish variables
done = False

while not done:  # get user input until error occurs
    try:
        userInput = int(input("Enter an integer: "))  # read input from user
        nums.append(userInput)
    except ValueError:  # user did not input an int
        print("ERROR: Not an integer.")
    except EOFError as error:
        done = True  # prevent further input
        print("[", end='')  # print permutations
        permutations(nums, 0, len(nums))
        sys.stdout.write("\b");
        sys.stdout.write("\b");
        print("]")