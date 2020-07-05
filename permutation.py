import numpy as np
import math

'''
Different permutation methods using python
'''

# Using raw mathematics
def perm(n, r):
  num = denom = 1
  
  if n >= 1:
    for i in range (1,n+1):
      num=num*i

  if r < n:
    for i in range (1,n-r+1):
      denom=denom*i
  
  return num/denom

# Using factorial  
def perm_fact(n, r):
  return math.factorial(n)/math.factorial(n-r)

# Using Stirling Approximation
def perm_stir(n,r):
  def stirling(n):
      return math.sqrt(2*math.pi*n)*(n/math.e)**n
  return stirling(n)/stirling(n-r)

# Using list
def perm_list(n, r):
  num_list = []
  denom_list = []

  if n >= 1:
    for i in range (1,n+1):
      num_list.append(i)

  if r < n:
    for i in range (1,n-r+1):
      denom_list.append(i)

  new_num = [x for x in num_list if x not in denom_list]

  return np.prod(new_num)

# Using list (shortened)
def perm_list_v2(n, r):
  num_list = []
  denom_list = []

  if n >= 1:
    for i in range (n-r+1,n+1):
      num_list.append(i)

  return np.prod(num_list)