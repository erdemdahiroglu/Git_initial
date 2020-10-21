import random


def calculation_1(s1, s2):
    return (s1 * s2) - (s1 + s2)


def calculation_2(s1, s2):
    return (s1 * s2) - (s2 - s1) / 20


def main():
    print("Version 1")
    n1 = random.randint(4, 9)
    n2 = random.randint(3, 7)

    n3 = calculation_1(n1, n2)
    print(n1, n2, n3)
        
    n5 = calculation_2(n1, n2)
    print(n1, n2, n5)


main()
