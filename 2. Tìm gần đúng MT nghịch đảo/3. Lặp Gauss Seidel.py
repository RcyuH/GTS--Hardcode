import numpy as np

#DIEU KIEN: A CHEO TROI HANG
#HPT: AX = E
#Doc A tu file, A cheo troi hang nhaaaaa
f = open('3. data Lặp Gauss Seidel.txt')
tmp_A = [[], [], []] #Khoi tao phu hop voi du lieu trong file 
i = 0
j = 0
for line in f:
	number_array = line.split()
	if len(number_array) == 2:
		SoHang = float(number_array[0])
		SoCot = float(number_array[1])
	else:
		for number in number_array:
			tmp_A[i].append(float(number))
		i += 1
A = np.array(tmp_A)
E = np.eye(len(A))
T = np.array(tmp_A)
for i in range(len(T)):
	for j in range(len(T[0])):
		if i == j: T[i][j] = 1/T[i][j]
		else: T[i][j] = 0
T_nghich = np.linalg.inv(T)

#Khoi tao X0
X0 = np.zeros((len(A), len(A[0])))
X1 = np.zeros((len(A), len(A[0])))

#Tinh toan
B = E - T@A

#Nhap so lan lap
n = 100

#Tach B thanh ma tran L + U
L = np.zeros((len(A), len(A[0]))) #tam giac duoi i >= j
U = np.zeros((len(A), len(A[0]))) #tam giac tren i <= j
for i in range(len(A)):
	for j in range(len(A)):
		if i >= j: L[i][j] = B[i][j]
		else: U[i][j] = B[i][j]

#Lap
for m in range(n):
	for i in range(len(A)):
		X1[i] = L[i]@X1 + U[i]@X0 + T[i]
	X0 = X1

#In ra man hinh:
print(X1)

# #Kiem tra
# print()
# print(np.linalg.inv(A))