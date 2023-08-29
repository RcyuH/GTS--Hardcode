#Su dung cho f(x) la da thuc
import math
#Nhap danh sach he so => Da thuc f(x) tu hinh thanh: a[0]*x^n + a[1]*x^n-1 + .....
heSo = [1, 2, 1] 

def f(x):
    f = 0
    for i in range(len(heSo)):
        f += heSo[i]*x**(len(heSo)-i-1)
    return f

#nhap n: cang lon thi cang chuan
#WARNING: hay can than neu n qua lon => khoang chia qua nho => Python khong xu ly duoc se lam tron try_var thanh 0
N = 4

#Khoang chua tat ca cac nghiem cua f(x) se la: 
heSo_abs = list()
for i in range(len(heSo)):
    if i != 0:
        heSo_abs.append(math.fabs(heSo[i]))
b = 1 + max(heSo_abs)/math.fabs(heSo[0])
a = -b


#tinh toan
i = a
nghiem = list() #ở đây ta chỉ lưu các KPL, còn các nghiệm thì hãy dùng các code khác đã có, cùng với KPL tìm được và hàm ban đầu để tìm nghiệm
cacKPL = list()
while i+1/N < b:
    print(i)
    if f(i)*f(i+1/N) > 0:
        i = i+1/N 
    elif f(i)*f(i+1/N) < 0:
        cacKPL.append((i, i+1/N))
        i = i + 1/N
    else:
        cacKPL.append((i+1/N - 0.00001, i+1/N + 0.00001))
        if i + 2/N < b:
            i = i + 2/N  
        else:
            i = i + 1/N + 0.000001
print(cacKPL)

