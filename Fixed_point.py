from numpy import linspace, zeros,sign,array,cos
import matplotlib.pyplot as plt

def g(x):
    return (cos(x)+1)/3

n =10
x = zeros(n)
error = zeros(n)
x0=0.0
x[0] = x0
xrange = array(range(0,10))

for i in range(n-1):
    x[i+1] = g(x[i])
    error[i + 1] = abs(((x[i + 1] - x[i]) / x[i + 1])) * 100

print("%5s %8s %8s" % ('k','x','E'))
for k in range(n):
    print("%5d %9.4f %9.4f" % (k+1,x[k],error[k]))

plt.plot(xrange,x,'k--',label='x')
plt.plot(xrange,error,'ro-',label='E(%)')
plt.legend()
plt.show()