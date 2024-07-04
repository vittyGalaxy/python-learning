def execute_factorial(a):
    if a == 1:
        return a
    else:
        return a * execute_factorial(a - 1)

if __name__ == '__main__':

    print(execute_factorial(5))