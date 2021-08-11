num = []

for i in range (0,3):
    try:  # try is used to catch any errors for the input validation into float
        n = int(input("Please input an integer between -9999 and 9999: "))
    except ValueError:  # ValueError is raised when we are attempting to convert a non numeric string into float.
        print("This is not a valid integer, please try again.")
        continue
    else:  # should be a number, but check for within range
        if -9999 < n < 9999:
            num.append(n)

        else:
            print("Enter an integer between -9999 and 9999")
            continue


num.sort()
print("Smallest Number;", num[0])
print("Biggest Number;", num[2])
