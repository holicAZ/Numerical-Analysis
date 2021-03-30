from numpy import array

A = array([[1,2,3],[4,5,6],[7,8,9]])
B = array([[-1,21,4],[5,2,-4],[0,0,2]])

madd = A + B
msub = A - B
mult = A * 10.0
divi = A / 2.0
dots = A.dot(B)
mmt = A * B

print('A+B \n',madd)
print('A-B \n',msub)
print('A*10.0 \n',mult)
print('A/2.0 \n',divi)
print('AdotB \n',dots)
print('A*B \n',mmt)