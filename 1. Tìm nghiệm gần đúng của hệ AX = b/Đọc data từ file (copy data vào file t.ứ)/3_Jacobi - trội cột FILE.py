import numpy as np

#HPT: A*X = b <=> Z = B1*Z + b 

#Nhập Z0
Z0 = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

#Doc A va Doc b tu file => Sau do chung ta tu suy ra D va E
f = open('3_data3.txt')
tmp_A = [[], [], [], [], [], [], [], [], [], []] #Khoi tao phu hop voi du lieu trong file 
tmp_b = [[], [], [], [], [], [], [], [], [], []]
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

#Nhap D
D = np.diag([130.75, 156, 89, 140.4286, 114, 81.75, 96.8571, 106.8, 81.1667, 52.0833])
D_nghich = np.linalg.inv(D)
max_aii = 140.4286
min_aii = 52.0833

#Số lần lặp
n = 19

#Ma tran don vi E
E = np.eye(10)

#Ma tran B1
B1 = E - A@D_nghich

#Tinh toan
chuan = np.linalg.norm(B1, ord=1)
for i in range(n):
	saiso = (chuan/(1-chuan))*(max_aii/min_aii)*np.linalg.norm(D_nghich@(B1@Z0 + b) - D_nghich@Z0, ord=1)
	Z0 = B1@Z0 + b
	print("X" + str(i+1) + " = " + str(D_nghich@Z0) + "      Saiso" + str(i+1) + " = " + str(saiso))