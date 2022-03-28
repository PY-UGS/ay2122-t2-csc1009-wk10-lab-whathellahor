# Function to return the module name based on the module code
def getModule(code):
    match code:  # Similar to switch case in java
        case "CSC1006":  # If the code passed in is CSC1006, returns the following string
            return "Mathematics II"
        case "CSC1007":  # If the code passed in is CSC1007, returns the following string
            return "Operating Systems"
        case "CSC1008":  # If the code passed in is CSC1008, returns the following string
            return "Data Structure and Algorithms"
        case "CSC1009":  # If the code passed in is CSC1009, returns the following string
            return "Object-Oriented Programming"
        case "CSC1010":  # If the code passed in is CSC1010, returns the following string
            return "Computer Networks"


# Function to print out all odd numbers from numbers 102 - 66
def printOddNum():
    for i in range(102, 66, -1):  # For loop to run through the numbers in descending order
        if i % 2 != 0:  # Check only odd numbers and print it
            print(i)


# Takes in user input for the module code
mCode = input("Enter your module code: ")
# Prints the module name based on the module code by calling the function getModule
print("Module name: ", getModule(mCode))

# Calls the function to print out odd numbers ranging from numbers 102-66
printOddNum()
