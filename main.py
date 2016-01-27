
# -*- coding: utf-8 -*-


def entry_numbers(n):
    numbers = []
    count = 0
    if n is None or n < 0:
        raise ValueError
    while count < 3:
        number = input('Input number :')
        numbers.append(number)
        count += 1
    return tuple(numbers)


def test_triangle(numbers):
    s1 = numbers[0]
    s2 = numbers[1]
    s3 = numbers[2]
    if s1 > (s2 + s3) or s2 > (s1 + s3) or s3 > (s1 + s2):
        print 'Not is a triangle'
    elif s1 == s2 and s1 == s3:
        print 'Equilateral'
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print 'Isosceles'
    elif s1 != s2 and s2 != s3 and s2 != s3:
        print 'Scalene'

if __name__ == "__main__":
    entry_numbers((2, 2, 2))
    test_triangle((2, 2, 2))
