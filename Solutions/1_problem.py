"""
Project Euler Problem 1 - Multiples of 3 or 5

Answer: 233168
Elapsed time (seconds): 2.0504e-05 

Solved with Python 3.10.12
"""


import time

start_time = time.time()
y=(sum(list(filter(lambda x: x%3==0 or x%5==0, range(1,100)))))
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", y)
print("Elapsed time: ", elapsed_time) 