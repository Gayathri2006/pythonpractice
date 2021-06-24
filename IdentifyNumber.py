# Program to input from user and validate




while True:
    while True:
        try:
            num = float(input("Type a number:"))
        except ValueError:
            print("This is not a number.")
            continue
        else:
            break
    if -9999 < num < 9999:
        print("valid")
        break
    else:
     print("Enter a number between -9999 and 9999")
