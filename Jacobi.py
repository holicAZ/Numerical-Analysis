from numpy import zeros
import matplotlib.pyplot as plt

n=8
x1j = zeros(n)
x2j = zeros(n)
x3j = zeros(n)
it = range(n)
error1 = zeros(n);
error2 = zeros(n);
error3 = zeros(n);

print('%7s %9s %9s %9s %9s %9s %9s' % ('k','x1','x2','x3','e1','e2','e3'))
print('%7d %9.5f %9.5f %9.5f' % (0,x1j[0],x2j[0],x3j[0]))

for k in range(n-1):
    x1j[k+1] = (-1.0 + 2.0 * x2j[k] - 3.0*x3j[k]) / 5.0
    x2j[k+1] = (2.0 + 3.0 * x1j[k] - x3j[k]) / 9.0
    x3j[k+1] = (-3.0 + 2.0 * x1j[k] - x2j[k]) / 7.0
    error1[k + 1] = abs(((x1j[k + 1] - x1j[k]) / x1j[k + 1])) * 100
    error2[k + 1] = abs(((x2j[k + 1] - x2j[k]) / x2j[k + 1])) * 100
    error3[k + 1] = abs(((x3j[k + 1] - x3j[k]) / x3j[k + 1])) * 100
    print('%7d %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' % (k+1,x1j[k+1],x2j[k+1],x3j[k+1],error1[k + 1], error2[k + 1], error3[k + 1]))

plt.subplot(2,1,1)
plt.plot(it,x1j,'ko-',label='x1')
plt.plot(it,x2j,'ro-',label='x2')
plt.plot(it,x3j,'bo-',label='x2')
plt.xlabel('iteration')
plt.ylabel('Approximate Solutions')

plt.subplot(2,1,2)
plt.xlabel('iteation')
plt.ylabel('E(%)')
plt.plot(it,error1,'k-',label='E1')
plt.plot(it,error2,'r-',label='E2')
plt.plot(it,error3,'b-',label='E3')
plt.show()
