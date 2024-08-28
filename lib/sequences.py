#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    print_fibonacci = []

    for i in range(length):
        if i == 0:
            print_fibonacci.append(0)
        elif i == 1:
            print_fibonacci.append(1)
        else:
            next_number = print_fibonacci[i - 1] + print_fibonacci[i - 2]
            print_fibonacci.append(next_number)

    print(print_fibonacci[:length])