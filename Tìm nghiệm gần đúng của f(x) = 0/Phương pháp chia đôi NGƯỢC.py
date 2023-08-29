import math

#nhap ham f(x)
def f(x):
    f = x**x - 10 #nhap tai day nek
    return f

#nhap sai so mong muon
sai_so = 0.00001

#nhap khoang phan ly nghiem (a0, b0)
a0 = 1
b0 = 3

#voi sai so do thi n tuong ung la
n = math.ceil(math.log((b0-a0)*sai_so**(-1), 2))
#print(n) 
#neu can

#tinh sai so tuyet doi
sai_so_cuoi_cung = (1/(2**n))*(b0-a0)

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
print("sai so tuyet doi Δx"+str(n)+" = "+str(sai_so_cuoi_cung))
#x = (a + b)/2
print("Nghiem gan dung: " + str((a0 + b0)/2))
print("So lan lap can lap la: " + str(n))
