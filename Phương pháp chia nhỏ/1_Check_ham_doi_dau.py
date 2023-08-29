#Su dung cho f(x) bat ky
import math

#nhap ham f(x)
def f(x):
    f = 2 #nhap tai day nek
    return f

#nhap n: cang lon thi cang chuan
#WARNING: hay can than neu n qua lon => khoang chi qua nho => Python khong xu ly duoc se lam tron try_var thanh 0
n = 10000

#nhap doan can xet [a, b], dung chon dau mut a, b la diem f(a) va f(b) = 0
a = 1
b = 10

#Start
i = a
try_var = f(a)*f(i+1/n)
while try_var > 0 and i <= b:
    i += 1/n
    try_var *= f(a)*f(i)
    if try_var < 0:
        print("Ham f(x) doi dau tren doan [" + str(a) + ", " + str(b) + "]")
        exit()
    if try_var == 0:
        try_var = f(a)*f(i+1/n)
print("Ham f(x) giu nguyen dau tren doan [" + str(a) + ", " + str(b) + "]")

