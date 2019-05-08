def oddProduct(numList):  # Return True if any 2 integers have an odd product; otherwise return False
    numList.sort()  # sort the list of integers
    for i in numList:  # outer loop
        for j in numList:  # inner loop
            if i != j and (i*j)%2 != 0:  # Check if i & j are different and if they have an odd product
                return True
    return False

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
        print(oddProduct(nums))