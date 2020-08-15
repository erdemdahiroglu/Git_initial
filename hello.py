import random


def calculation_1(s1, s2):
    return (s1 * s2) - (s1 + s2)


def calculation_2(s1, s2):
    return (s1 * s2) - (s2 - s1)


def main():
    print("master")
    n1 = random.randint(5, 9)
    n2 = random.randint(4, 7)

    n3 = calculation_1(n1, n2)
    print(n1, n2, n3)
        
    n4 = calculation_2(n1, n2)
    print(n1, n2, n4)


main()
