def intro():
    return int(input("Please enter a number to determine the nth Fibonacci number: "))


def return_nth_fib_number(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return return_nth_fib_number(num - 1) + return_nth_fib_number(num - 2)


def main():
    fib_num = intro()
    nth_fib = return_nth_fib_number(fib_num)
    print(f"The {fib_num}th Fibonacci number is: {nth_fib}")


if __name__ == "__main__":
    main()
