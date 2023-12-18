"""
Project Euler Problem 4 - Largest Palindrome Product

Answer: 906609
Elapsed time (seconds): 0.0385

Solved with Python 3.10.12
Author: dnicolauit
""" 

import time

def ispalindrome(number):
    return str(number) == str(number)[::-1]

def max_palindrome_product(max, min):
    max_palindrome = 0
    for i in range(max, min, -1):
        for j in range(max, min, -1):
            if i*j > max_palindrome:
                if ispalindrome(i*j):
                    max_palindrome = i*j
    return max_palindrome

start_time = time.time()
solution = max_palindrome_product(999, 99)
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", solution)
print("Elapsed time: ", elapsed_time) 