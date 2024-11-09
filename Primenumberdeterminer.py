import math
print("This is a program that determines if a number is a prime number or not.")
number = input("Enter a number: ")
if number.isdigit():
    number = int(number)
    if number < 2:
        print("False")
        quit()
    else:
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                print("False")
                quit()
        print("True")
