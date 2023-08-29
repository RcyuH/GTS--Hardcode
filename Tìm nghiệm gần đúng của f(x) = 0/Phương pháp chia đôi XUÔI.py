import math

#nhap ham f(x)
def f(x):
    f = x**4 + 3*x**2 - 10 #nhap tai day nek
    return f

#nhap so lan lap
n = 50

#nhap khoang phan ly nghiem (a0, b0)
a0 = 1.399999999999978
b0 = 1.499999999999978

#tinh sai so tuyet doi
sai_so = (1/(2**n))*(b0-a0)

for i in range(n):
    c0 = (1/2)*(a0+b0)
    if f(c0) == 0:
        print("x* = " + str(c0))
    else:
        if f(a0)*f(c0) < 0:
        	b0 = c0
        else:
        	a0 = c0
    print("(a"+str(i+1)+", b"+str(i+1)+") = ("+str(a0)+", "+str(b0)+")") 
print("sai so tuyet doi Δx"+str(n)+" = "+str(sai_so))
#x = (a + b)/2
print("Nghiem gan dung: " + str((a0 + b0)/2))
