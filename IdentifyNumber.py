# Program to input from user and validate

while True:
    try: # try is used to catch any errors for the input validation into float
        num = int(input("Please input a integer between -9999 and 9999: "))
    except ValueError: # ValueError is raised when we are attempting to convert a non numeric string into float.
        print("This is not a valid number, please try again.")
        continue
    else: # should be a number, but check for within range
        if -9999 < num < 9999:
            print("Congrats! You have given a valid number!")
            break
        else:
            print("Enter an integer between -9999 and 9999")
            continue

def valid(n):
    if n >= 0:
        print(n, "is a positive number.")
    else:
        print(n, "is a negative number.")
    if n%2 == 0:
        print(n," is also an even number")
    else:
        print(n, " is also an odd number.")
def prime(n):
    if n > 1:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "is not a prime number")
                print(i, "times", n // i, "is", n)
                break
        else:
            print("and",n, " is also a prime number!")

    # if input number is less than or equal to 1, it is not prime
    else:
        print(n, "is not a prime number.")

valid(num)
prime(num)