import numpy as np

#HPT: AX = b

#Nhập X0
X0 = np.array([[0], [0], [0]])

#Nhập A
A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])

#Nhập b
b = np.array([[12], [13], [14]])

#Nhap D
D = np.diag([10, 10, 10])
D_nghich = np.linalg.inv(D)

#Số lần lặp
n = 10

#Ma tran don vi E
E = np.eye(3)

#Tinh toan
B = E - D_nghich@A
d= D_nghich@b
chuan = np.linalg.norm(B, ord=np.inf)
for i in range(n):
	saiso = (chuan/(1-chuan))*np.linalg.norm(B@X0 + d - X0, ord=np.inf)
	X0 = B@X0 + d
	print("X" + str(i+1) + " = " + str(X0) + "      Saiso" + str(i+1) + " = " + str(saiso))