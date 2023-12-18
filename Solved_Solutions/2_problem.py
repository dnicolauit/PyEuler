"""
Project Euler Problem 2 - Even Fibonacci Numbers

Answer: 233168
Elapsed time (seconds): 3.7193e-05

Solved with Python 3.10.12
Author: dnicolauit
""" 

import time



n=[0,1]
limit = 4000000

start_time = time.time()
while n[len(n)-1]<=limit:
    n.append(n[len(n)-1]+n[len(n)-2])
    
even = sum(list(filter(lambda x: x%2==0, n)))
end_time = time.time()

elapsed_time = end_time - start_time
print("Solution: ", even)
print("Elapsed time: ", elapsed_time) 

