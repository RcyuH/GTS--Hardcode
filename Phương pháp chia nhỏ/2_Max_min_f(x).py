#Su dung cho f(x) bat ki tren doan [a, b] 
#WARNING: Sai so khong qua chinh xac??
import math

#Nhap ham f(x)
def f(x):
    f = x**2 - 3*x + 2
    return f

#Nhap dao ham cua f(x)
def f_dh(x):
    f_dh = 2*x - 3
    return f_dh

#nhap n: cang lon thi cang chuan
#WARNING: hay can than neu n qua lon => khoang chia qua nho => Python khong xu ly duoc se lam tron try_var thanh 0
N = 1000

#Nhap doan [a, b]
a = -10
b =  10

#tinh toan cac KPL cua f'(x) => Cac noi la diem cuc tri
i = a
nghiem = list() #ở đây ta chỉ lưu các KPL, còn các nghiệm/diem cuc tri neu muon tinh chinh xac thì hãy dùng các code khác đã có, cùng với KPL tìm được và hàm ban đầu để tìm nghiệm
cacKPL = list()
while i+1/N < b:
    if f_dh(i)*f_dh(i+1/N) > 0:
        i = i+1/N 
    elif f_dh(i)*f_dh(i+1/N) < 0:
        cacKPL.append((i, i+1/N))
        i = i + 1/N
    else:
        if i + 2/N < b:
            i = i + 2/N 
            if f_dh(i) == 0:
                i = i - 1/N 
print("Cac khoang phan ly cua f'(x) la: ")
print(cacKPL)
print()

#Cuc tri gan dung 
list_diem_kha_nghi = [a, b]
list_gia_tri_kha_nghi = [f(a), f(b)]
list_delta = [0, 0] #Vi neu max/min = f(a) hay f(b) thi sai so se = 0
for i in cacKPL:
    list_diem_kha_nghi.append(i[0])
    list_gia_tri_kha_nghi.append(f(i[0]))
    list_delta.append(math.fabs(i[1] - i[0]))
print("Cac diem kha nghi la: ")
print(list_diem_kha_nghi)
print()
print("Cac gia tri kha nghi tuong ung la: ")
print(list_gia_tri_kha_nghi)
print()
max_f = max(list_gia_tri_kha_nghi)
min_f = min(list_gia_tri_kha_nghi)
for i in range(len(list_gia_tri_kha_nghi)):
    if list_gia_tri_kha_nghi[i] == max_f:
        diem_max = list_diem_kha_nghi[i]
        delta_max = list_delta[i]
    if list_gia_tri_kha_nghi[i] == min_f:
        diem_min = list_diem_kha_nghi[i]
        delta_min = list_delta[i]
print("MAX[a, b] f(x) = ", end="")
print(max_f, end="")
print(" tai x = ", end="")
print(diem_max)
print("MIN[a, b] f(x) = ", end="")
print(min_f, end="")
print(" tai x = ", end="")
print(diem_min)
print()

#Sai so
saiso_max = delta_max*math.fabs(f_dh(diem_max))
print("Sai so cho gia tri max cua ham f(x) la: ", end="")
print(saiso_max)
saiso_min = delta_min*math.fabs(f_dh(diem_min))
print("Sai so cho gia tri min cua ham f(x) la: ", end="")
print(saiso_min)
