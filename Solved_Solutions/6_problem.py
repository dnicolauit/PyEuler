"""
Project Euler Problem 6 - Sum Square Difference

Answer: 25164150
Elapsed time (seconds): 4.7684e-06

Solved with Python 3.10.12
Author: dnicolauit
"""
import time

max_number = 100

start_time = time.time()

# Gauss formula for sum of natural numbers
squared_sum = int(max_number * (max_number + 1) / 2) ** 2

# Sum of Squares of n Natural Numbers Formula

sum_of_squares = int(max_number * (max_number + 1) * (max_number * 2 + 1) / 6)

solution = squared_sum - sum_of_squares

end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", solution)
print("Elapsed time: ", elapsed_time)
