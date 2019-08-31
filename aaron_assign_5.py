def add_two(a, b):
    return a + b


def concat(a, b):
    return str(a) + str(b)


def printer(a, b):
    print(a, '\n', b)


def main():
    while True:
        try:
            a = int(input("Enter Your First Number: "))
            break
        except ValueError:
            print("Sorry that's not a valid number...Try again!")
    while True:
        try:
            b = int(input("Enter Your Second Number: "))
            break
        except ValueError:
            print("Sorry that's not a valid number...Try again!")
    while True:
        try:
            c = str(input("Enter Your First String: "))
            if c.isalpha() == True:
                c = c
            else:
                break
        except TypeError:
            print("Sorry that's not a valid string...Please enter only alpha characters!")
    while True:
         try:
            d = str(input("Enter Your Second String: "))
            if d.isalpha() == True:
                d = d
            else:
                break
         except TypeError:
            print("Sorry that's not a valid string...Please enter only alpha characters!")
    add_result = add_two(a, b)
    concat_result = concat(c, d)
    printer(add_result, concat_result)


if __name__ == "__main__": main()
