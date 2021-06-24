# Program to input from user and validate

while True:
    try: # try is used to catch any errors for the input validation into float
        num = float(input("Please input a number: "))
    except ValueError: # ValueError is raised when we are attempting to convert a non numeric string into float.
        print("This is not a valid number, please try again.")
        continue
    else: # should be a number, but check for within range
        if -9999 < num < 9999:
            print("Congrats! You have given a valid number!")
            break
        else:
            print("Enter a number between -9999 and 9999")
            continue
