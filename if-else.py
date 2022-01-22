def is_leap(year):
    leap = False

    # Write your logic here

    if year % 4 == 0:
        is_leap = True
    else:
        is_leap = False
        if year % 100 == 0:
            is_leap = True
        else:
            is_leap = False
            if year % 400 == 0:
                is_leap = True

    if is_leap == False:
        is_leap = False
        print("False")
    else:
        is_leap = True
        print("True")


year = int(input())
print (is_leap(year))