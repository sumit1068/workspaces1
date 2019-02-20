# taking input from user
number = int(input("Enter any number: "))

if number > 1:

    if (number % 2) == 0:
        print(number, "is not a prime number")

    else:
        print(number, "is a prime number")

else:

    print(number, "is not a prime number")