import numpy as np

#HPT: AX = b

#Nhập X0
X0 = np.array([[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]])

#Doc A va Doc b tu file => Sau do chung ta tu suy ra D va E
f = open('2_data2.txt')
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

#Ma tran don vi E
E = np.eye(10)

#Số lần lặp
n = 100

#Tinh toan
B = E - D_nghich@A
d= D_nghich@b
chuan = np.linalg.norm(B, ord=np.inf)
for i in range(n):
	saiso = (chuan/(1-chuan))*np.linalg.norm(B@X0 + d - X0, ord=np.inf)
	X0 = B@X0 + d
	print("X" + str(i+1) + " = " + str(X0) + "      Saiso" + str(i+1) + " = " + str(saiso))