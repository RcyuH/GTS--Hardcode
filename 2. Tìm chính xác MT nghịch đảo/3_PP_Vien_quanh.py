import numpy as np
import cmath

#HPT: AX = E
#Doc A tu file
f = open('1_Cholesky.txt')
tmp_A = [[], [], [], [], []] #TU KHOI TAO PHU HOP VOI SO HANG VA COT TRONG FILE 
tmp_b = [[], [], [], [], []]
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

def Ai_inv(Ai, A_inv_before):
	#phan tich
	n = len(Ai)
	U = Ai[n-1:n, 0:n-1]
	V = Ai[0:n-1, n-1:n]
	a = A[n-1][n-1]

	E = np.eye(n-1)
	Ai_nghich = np.zeros((n, n))

	#tinh toan
	X21 = np.linalg.inv(U@A_inv_before@V - a)@U@A_inv_before
	X11 = A_inv_before@(E - V@X21)
	x22 = -np.linalg.inv(U@A_inv_before@V - a)
	X12 = A_inv_before@(-V*x22)
	
	#gan
	Ai_nghich[n-1:n, 0:n-1] = X21
	Ai_nghich[0:n-1, n-1:n] = X12
	Ai_nghich[n-1][n-1] = x22
	Ai_nghich[0:n-1, 0:n-1] = X11

	return Ai_nghich	

A_inv_before = np.linalg.inv(A[0:2, 0:2])
for i in range(3, len(A)+1):
	Ai = A[0:i, 0:i]
	A_inv_before = Ai_inv(Ai, A_inv_before)
	print("Buoc" + str(i-2))
	print(A_inv_before)

# #check
# print(np.linalg.inv(A))
