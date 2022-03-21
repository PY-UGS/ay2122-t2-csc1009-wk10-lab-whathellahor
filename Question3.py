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


def printOddNum():
    for i in range(102, 66, -1):
        if i % 2 != 0:
            print(i)


code = input("Enter your module code: ")
print("Module name: ", getModule(code))

printOddNum()