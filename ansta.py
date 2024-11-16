from decimal import Decimal

def code_generator(code_one, code_two):
    joined_one = int("".join(code_one.split("-")))
    joined_two = int("".join(code_two.split("-")))
    for i in range(joined_one,joined_two+1):
        print(str(i)[0:2], "-", str(i)[2:6], sep = "")

code_generator("79-900", "80-155")

def missing_value_finder(n_list,n):
    for i in range(1, n+1):
        if i not in n_list:
            print(i)

missing_value_finder([2,3,7,4,9],10)

def decimal_list():
    for x in range(20, 60, 5):
        print(Decimal(x/10))

decimal_list()
