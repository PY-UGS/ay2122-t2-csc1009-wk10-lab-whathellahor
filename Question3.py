# Function to return the module name based on the module code
def getModule(code):
    match code:
        case "CSC1006":
            return "Mathematics II"
        case "CSC1007":
            return "Operating Systems"
        case "CSC1008":
            return "Data Structure and Algorithms"
        case "CSC1009":
            return "Object-Oriented Programming"
        case "CSC1010":
            return "Computer Networks"


# Function to print out all odd numbers from numbers 102 - 66
def printOddNum():
    for i in range(102, 66, -1):
        if i % 2 != 0:
            print(i)


# Takes in user input for the module code
mCode = input("Enter your module code: ")
# Prints the module name based on the module code by calling the function getModule
print("Module name: ", getModule(mCode))

# Calls the function to print out odd numbers ranging from numbers 102-66
printOddNum()