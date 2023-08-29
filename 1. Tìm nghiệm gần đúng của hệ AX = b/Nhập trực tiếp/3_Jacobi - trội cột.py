import numpy as np

#HPT: A*X = b <=> Z = B1*Z + b 

#Nhập Z0
Z0 = np.array([[0], [0], [0]])

#Nhập A
A = np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]])

#Nhập b
b = np.array([[12], [13], [14]])

#Nhap D
D = np.diag([10, 10, 10])
D_nghich = np.linalg.inv(D)
max_aii = 10
min_aii = 10

#Số lần lặp
n = 10

#Ma tran don vi E
E = np.eye(3)

#Ma tran B1
B1 = E - A@D_nghich

#Tinh toan
chuan = np.linalg.norm(B1, ord=1)
for i in range(n):
	saiso = (chuan/(1-chuan))*(max_aii/min_aii)*np.linalg.norm(D_nghich@(B1@Z0 + b) - D_nghich@Z0, ord=1)
	Z0 = B1@Z0 + b
	print("X" + str(i+1) + " = " + str(D_nghich@Z0) + "      Saiso" + str(i+1) + " = " + str(saiso))