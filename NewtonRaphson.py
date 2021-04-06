from numpy import zeros, array, cos, sin
import matplotlib.pyplot as plt

def f(x):
    return 3.0*x-cos(x)-1.0
def df(x):
    return 3.0+sin(x)

n=7
x= zeros(n)
x[0]= 10
error = zeros(n)
itl = range(0,7)
it = array(itl)

for i in range(n-1):
    x[i+1] = x[i] - f(x[i]) / df(x[i])

for i in range(n-1):
    error[i + 1] = abs(((x[i + 1] - x[i]) / x[i + 1])) * 100

print("%5s %8s %8s" % ('k','x','E'))
for k in range(n):
    print("%4d %9.4f %9.4f" % (k+1,x[k],error[k]))

plt.plot(it,x,'k--',label='c')
plt.plot(it,error,'ro-',label='E(%)')
plt.legend()
plt.show()
