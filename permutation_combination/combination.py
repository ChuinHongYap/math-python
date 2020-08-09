import numpy as np
import math

'''
Different combination methods using python
'''

# Using raw mathematics
def comb(n, r):
  num = denom_a = denom_b= 1
  
  # n!
  if n >= 1:
    for i in range (1,n+1):
      num=num*i

  if r < n:
    # r!
    for i in range (1,r+1):
      denom_a=denom_a*i
    
    # (n-r)!
    for i in range (1,n-r+1):
      denom_b=denom_b*i
  
  return num/(denom_a*denom_b)

# Using factorial  
def comb_fact(n, r):
  return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

# Using Stirling Approximation
def comb_stir(n,r):
  def stirling(n):
      return math.sqrt(2*math.pi*n)*(n/math.e)**n
  return stirling(n)/(stirling(r)*stirling(n-r))

# Using list
def comb_list(n, r):
  num_list = []
  denom_a = 1
  denom_list = []

  if n >= 1:
    for i in range (1,n+1):
      num_list.append(i)

  if r < n:
    for i in range (1,r+1):
      denom_a=denom_a*i
    
    for i in range (1,n-r+1):
      denom_list.append(i)

  # or just use math.factorial
  # denom_a = math.factorial(r)

  new_num = [x for x in num_list if x not in denom_list]

  return np.prod(new_num)/denom_a

# Using list (shortened)
def comb_list_v2(n, r):
  num_list = []
  denom_a = 1
  denom_list = []

  if r < n:
    for i in range (1,r+1):
        denom_a=denom_a*i

  if n >= 1:
    for i in range (n-r+1,n+1):
      num_list.append(i)

  # or just use math.factorial
  # denom_a = math.factorial(r)

  return np.prod(num_list)/denom_a