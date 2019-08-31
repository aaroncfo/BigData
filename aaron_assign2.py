# Question B
def full_name(a, b):
    ls = [str(a), str(b)]
    return 'Your full name is ' + ls[0] + ' ' + ls[1] + '.'

# Question C
def sub_str(a, b):
    a = str(a)
    return '\n' + \
           'The first 4 characters of your first name are ' + a[:4] + '.' + \
           '\n' + 'The proper casing for your name is ' + a[:1].upper() + a[1:] + ' ' + b[:1].upper() + b[1:] + '.' + \
           '\n' + 'Your name in lower case is ' + a.lower() + ' ' + b.lower() + '.' + \
           '\n' + 'Your name in upper case is ' + a.upper() + ' ' + b.upper() + '.'

# Question D
def list_ops(a):
    lst = list(a)
    dc = {}
    dc['The length of the list is '] = len(lst)
    for i in lst:
        txt = 'The square of ' + str(i) + ' is '
        dc[txt] = i**3

    return dc


def printer(a, b, c):
    print(a, '\n', b, '\n', c)


def main():
    a = str(input("Enter Your First Name: "))
    b = str(input("Enter Your Last Name: "))
    scores = [10, 20, 30, 40, 50]
    your_name = full_name(a, b)
    str_results = sub_str(a, b)
    list_results = list_ops(scores)
    printer(your_name, str_results, list_results)


if __name__ == "__main__": main()
