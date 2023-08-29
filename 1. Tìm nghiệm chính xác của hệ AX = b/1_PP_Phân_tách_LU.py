import numpy as np

#HPT: AX = b
#Doc A va Doc b tu file => Sau do chung ta tu suy ra D va E
f = open('data1.txt')
tmp_A = [[], [], [], [], [], [], []] #Khoi tao phu hop voi du lieu trong file 
tmp_b = [[], [], [], [], [], [], []]
i = 0
j = 0
for line in f:
	number_array = line.split()
	if len(number_array) == 2:
		SoHang = float(number_array[0])
		SoCot = float(number_array[1])
	elif len(number_array) == 1:
		tmp_b[j].append(float(number_array[0]))
		j += 1
	else:
		for number in number_array:
			tmp_A[i].append(float(number))
		i += 1
A = np.array(tmp_A)
b = np.array(tmp_b)

#Khoi tao L va U:
L = np.zeros((len(A), len(A[0]))) #tam giac duoi i >= j
U = np.eye(len(A)) #tam giac tren i <= j
L[0] = A.T[0]
U[0] = A[0]/A[0][0]
for k in range(1, len(A)):
	L[k] = A.T[k]
	for t in range(k):
		L[k] -= U[t][k]*L[t]
	U[k] = A[k]
	for t in range(k):
		U[k] -= L.T[k][t]*U[t]
	U[k] = U[k]/L[k][k]
L = L.T

#Qua trinh nghich
y = np.linalg.inv(L)@b 
X = np.linalg.inv(U)@y
print("Vay nghiem dung cua he phuong trinh AX = b la: ")
print(X)