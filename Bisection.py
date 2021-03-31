from numpy import linspace, zeros,sign,array
import matplotlib.pyplot as plt

def f(x):
    return -x**2+6.0*x-5.0
a=-2.0
b=3.0
n=14
c=zeros(n)
error = zeros(n)
xrange = array(range(1,15))
for i in range(n):
    c[i] = (a+b)/2.0
    if(sign(f(c[i]))==sign(f(a))):
        a=c[i]
    else:
        b=c[i]

for i in range(n-1):
    error[i+1]=abs(((c[i+1]-c[i])/c[i+1]))*100

print("%5s %8s %8s" % ('k','c','E'))
for k in range(n):
    print("%5d %9.4f %9.4f" % (k+1,c[k],error[k]))

plt.plot(xrange,c,'k--',label='c')
plt.plot(xrange,error,'ro-',label='E(%)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()