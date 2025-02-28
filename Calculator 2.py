num1 = int(input("What is number 1?"))
num2 = int(input("What is number 2?"))
opperator = str(input("Which opperation would you like to use? Enter(Addition/Subtraction/Multiplication/Division)"))
if opperator == "Addition":
    print(num1 + num2)
elif opperator == "Subtraction":
    if num1 > num2:
        print(num1 - num2)
    elif num1 == num2:
        print("0")
    else:
        print(num2 - num1)
elif opperator == "Multiplication":
    print(num1 * num2)
else:
    if num1 == 0:
        print("0")
    elif num2 == 0:
        print(ValueError("You cannot divide a number by 0"))
    elif num2 == 1:
        print(num1)
    else: 
        print(num1 / num2)

