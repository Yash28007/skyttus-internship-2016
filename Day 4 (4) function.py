def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def simple_interest(p, r, t):
    return (p * r * t) / 100

def is_palindrome(word):
    return word == word[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def merge_lists(list1, list2):
    return list1 + list2

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def area_of_rectangle(length, breadth):
    return length * breadth

def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == number
