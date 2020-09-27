#   This Program is my first attempt at a Calculator.

userInput1 = 0
userInput2 = 0
userInput3 = " "
output = 0

#   Ask user to input both numbers.

userInput1 = int(input("Enter number now."))

#   Ask user what mathmatic function to use. E.G. Add/Sub/Mult/Div
#   If the user inputs "1", the first two inputs will be added.
#   If the user inputs "2", the first two inputs will be subtracted.
#   If the user inputs "3", the first two inputs will be multiplied.
#   If the user inputs "4", the first two inputs will be divided.

userInput3 = input("Enter + for addition, - for subtraction, * for multiplication or / for division.")
userInput2 = int(input("Enter number now."))

if userInput3 == "+":
    output = userInput1 + userInput2

elif userInput3 == "-":
    output = userInput1 - userInput2

elif userInput3 == "*":
    output = userInput1 * userInput2

elif userInput3 == "/":
    if userInput2 == 0:
        print("Cannot divide by Zero.")
    else:
        output = userInput1 / userInput2

else:
    print("Error")

print(output)



    







