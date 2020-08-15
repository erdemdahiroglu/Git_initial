import random


def calculation_1(s1, s2):
    return (s1 * s2) - (s1 + s2)


def calculation_2(s1, s2):
    return (s1 * s2) - (s2 - s1) / 25


def main():
    print("Version 1")
    n1 = random.randint(5, 9)
    n2 = random.randint(4, 7)

    n4 = calculation_1(n1, n2)
    print(n1, n2, n4)
        
    n5 = calculation_2(n1, n2)
    print(n1, n2, n5)


main()
