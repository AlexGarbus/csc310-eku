class Hamming:
    def __init__(self, x, y):  # Initialize object
        self.x = x
        self.y = y

    def hammingDistance(self):  # Calculate and return the Hamming distance
        binX = list(bin(self.x))  # Create lists of each binary string
        binY = list(bin(self.y))
        del binX[0:2] # Remove '0b' prefix
        del binY[0:2]

        lenDifference = abs(len(binX) - len(binY))  # Make sure both lists are equal in length
        if(len(binX) < len(binY)):
            for i in range(0, lenDifference):
                binX.insert(0, 0)
        else:
            for i in range(0, lenDifference):
                binY.insert(0, 0)

        distance = int(0)  # Go through and check each digit for mismatching integers
        for i in range(0, len(binX)):
            if int(binX[i]) != int(binY[i]):
                distance += 1

        return distance

done = False  # establish variables

while not done:
    try:  # get user input
        x = int(input("Enter first integer: "))
        y = int(input("Enter second integer: "))

        if x >= 0 and y < 2**31:  # Make sure input is within range
            done = True  # prevent further input
        else:
            print("ERROR: Input is not within range.")
    except ValueError:  # user did not input an int
        print("ERROR: Not an integer")

myHamming = Hamming(x, y)  # Create Hamming object and calculate Hamming distance
print("The Hamming distance is " + str(myHamming.hammingDistance()))