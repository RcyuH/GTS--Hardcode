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
E = np.eye(len(A))

def case1(A):
	#Tim A
	n = len(A)
	Q = np.zeros((n, n), dtype=complex) #tam giac tren
	Q[0][0] = cmath.sqrt(A[0][0])
	for j in range(1, n):
		Q[0][j] = A[0][j]/Q[0][0]
	for i in range(1, n):
		Q[i][i] = A[i][i]
		for t in range(i):
			Q[i][i] -= Q[t][i]**2
		Q[i][i] = cmath.sqrt(Q[i][i])
		for j in range(i+1, n):
			Q[i][j] = A[i][j]
			for t in range(i):
				Q[i][j] -= Q[t][i]*Q[t][j]
			Q[i][j] = Q[i][j]/Q[i][i]

	#Qua trinh nghich
	Y = np.linalg.inv(Q.T)@E
	X = np.linalg.inv(Q)@Y 
	return X 				#A nghich dao

# (A==A.T).all(): CHECK XEM ma tran A co doi xung khong
if (A==A.T).all() and np.linalg.det(A) > 0:
	X = case1(A)
else:
	M = A.T@A 
	M_nghich = case1(M)
	X = M_nghich@A.T
print(X)
#print(np.linalg.inv(A))