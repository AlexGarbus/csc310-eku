done = False  # establish variables
lines = list()

while not done:  # get user input until error occurs
    try:
        userInput = input("Enter a string: ")  # read input from user
        lines.append(userInput)
    except EOFError as error:
        done = True  # prevent further input
        lines.reverse()  # print lines in reverse
        for line in lines:
            print(line)