import numpy as np
import matplotlib.pyplot as plt

mean = 1
stdev = 0.5

x = np.random.normal(loc=mean, scale=stdev,size=(10000))

plt.figure()
plt.title("Normal Distribution (mean= "+ str(mean)+ ", stdev= "+ str(stdev)+ ")")
plt.hist(x)

####################################################################################
n = 10
p = 0.5

y = np.random.binomial(n=n, p=p, size=1000)

plt.figure()
plt.title("Binomial Distribution (n= "+ str(n) + ", p= "+ str(p)+ ")")
plt.hist(y)