#!/usr/bin/env python3

def sqrt(x):
    if x < 0:
        raise ValueError(
        "cannot compute sqr of"
        f" negative number {x}"
        )
    guess = x
    i=0
    while guess*guess!=x and i<20:
        guess = (guess+x / guess)/2.0
        i += 1
    return guess

def main():
    num=input("Number :")
    try:
        print(sqrt(int(num)))
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(3)-5)
        print(sqrt(-5))
        print("this is never printed")
    except ValueError as e:
        print(e)
    print("program is going on....")

if __name__ == '__main__':
    main()
