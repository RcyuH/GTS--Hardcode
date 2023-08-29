import numpy as np

#DIEU KIEN: A CHEO TROI HANG
#HPT: AX = E
#Doc A tu file, A cheo troi hang nhaaaaa
f = open('2. Jacobi_cheo_troi_cot.txt')
tmp_A = [[], [], [], [], [], [], [], []] #Khoi tao phu hop voi du lieu trong file 
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

#Khoi tao Z0 va E
Z0 = np.zeros((len(A), len(A[0])))

#Tinh toan
B1 = E - A@T
max_aii = abs(T_nghich).max()
min_aii = abs(np.diagonal(T_nghich)).min()
q = np.linalg.norm(B1, ord=1)

#Nhap so lan lap
n = 100

#Lap
for i in range(n):
	sai_so = (q/(1 - q))*(max_aii/min_aii)*np.linalg.norm(T@(B1@Z0 + E) - T@Z0, ord=1)
	Z0 = B1@Z0 + E
	print("X" + str(i+1) + " = ")
	print(T@Z0)
	print("Sai so " + str(i+1) + ": ", end="")
	print(sai_so)
	print()

# #kiem tra
# print("*********************")
# print("Gia tri chinh xac ma tran nghich dao cua A la: ")
# print(np.linalg.inv(A))