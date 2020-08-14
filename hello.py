import random


def adding(s1, s2):
    return s1 + s2


def main():
    n1 = random.randint(5, 9)
    n2 = random.randint(4, 7)
    n3 = adding(n1, n2)
    print(n1, n2, n3)


main()
