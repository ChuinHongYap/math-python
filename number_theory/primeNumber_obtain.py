"""
Algorithms to obtain prime numbers.

Note: Methods implemented are based on wikipedia
"""

import math

# Loop Method
def primeLoopMethod_range(lower, upper):
  output_list = []
  for num in range(lower, upper + 1):
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
          output_list.append(num)
  return output_list
 
def primeLoopMethod(limit):
  output_list = []
  for num in range(2, limit + 1):
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      output_list.append(num)
  return output_list

# Sieve of Eratosthenes
def sieveOfEratosthenes(limit):
  multiples = []
  output_list = []
  for i in range(2, limit+1):
      if i not in multiples:
        output_list.append(i)
          for j in range(i*i, limit+1, i):
            multiples.append(j)
  return output_list
  
# Sieve of Sundaram
def sieveOfSundaram(limit):
  k = int((limit - 1) / 2)
  integers_list = [0] * (k + 1)
  for i in range(1, k + 1):
    j= i
    # Mark all numbers of the form i + j + 2ij as true where 1 <= i <= j 
    while (i+j+2*i*j <= k):
      integers_list[i+j+2*i*j] = 1
      j+= 1
  if limit > 2:
    output_list = [2]
  for i in range(1, k + 1):
    if integers_list[i]==0:
      output_list.append(2 * i + 1)
  return output_list
  
# Sieve of Atkin
# Source: https://stackoverflow.com/a/27215801
def sieveOfAtkin(limit):
  limit+=1
  P = [2,3]
  sieve=[False]*(limit+1)
  for x in range(1,int(math.sqrt(limit))+1):
    for y in range(1,int(math.sqrt(limit))+1):
      n = 4*x**2 + y**2
      if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
      n = 3*x**2+y**2
      if n<= limit and n%12==7 : sieve[n] = not sieve[n]
      n = 3*x**2 - y**2
      if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
  for x in range(5,int(math.sqrt(limit))):
    if sieve[x]:
      for y in range(x**2,limit+1,x**2):
        sieve[y] = False
  for p in range(5,limit):
    if sieve[p] : P.append(p)
  return P