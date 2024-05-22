# task 1

number_1 = int(input("Enter your first number"))
number_2 = int(input("Enter your second number"))
number_3 = int(input("Enter your third number"))

if number_1 > number_2 and number_1 > number_3:
    print(f"The greatest number is {number_1}")
elif number_2 > number_1 and number_2 > number_3:
    print(f"The greatest number is {number_2}")
elif number_3 > number_1 and number_3 >number_2:
    print(f"The greatest number is {number_3}")

if number_1 < number_2 and number_1 < number_3:
    print(f"The smallest number is {number_1}")
elif number_2 < number_1 and number_2 < number_3:
    print(f"The smallest number is {number_2}")
elif number_3 < number_1 and number_3 < number_2:
    print(f"The smallest number is {number_3}")

if number_1 == number_2 and number_1 == number_3:
    print("All numbers are equal.")
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print("Two numbers are equal.")

