def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



def fizzbuzz(start, end):
    ret_val = ""
    for i in range(start, end+1):
        if i % 3 == 0:
            ret_val += "Fizz"
        if i % 5 == 0:
            ret_val += "Buzz"
        elif is_prime(i):
            print(i)
            continue
        if ret_val != "":
            print(f"{i} {ret_val}")
            ret_val = ""

fizzbuzz(1, 150)