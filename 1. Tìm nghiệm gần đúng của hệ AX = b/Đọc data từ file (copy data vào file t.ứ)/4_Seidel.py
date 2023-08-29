import numpy as np 
import cmath
import math
from numpy import linalg as LA
from numpy.linalg import norm

step = 20
delta = 0.0001

def get_matrix(): #Doc ma tran A tu file
	f = open('4_Seidel.txt')
	tmp_A = [[], [], []] #TU KHOI TAO PHU HOP VOI SO HANG VA COT TRONG FILE 
	tmp_b = [[], [], []]
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
	return A, b

def separate(A):
	B1 = np.zeros((len(A), len(A[0])))
	B2 = np.zeros((len(A), len(A[0])))
	for i in range(len(A)):
		for j in range(len(A[0])):
			if i > j: B1[i][j] = A[i][j]
			else: B2[i][j] = A[i][j]
	return B1, B2 

#X = AX + d
def seidel():
	#so lan lap
	lanLap = 1
	#X khoi tao
	X = np.array([[0.], [0.], [0.]])
	A, d = get_matrix()
	B1, B2 = separate(A)
	for k in range(lanLap):
		for i in range(len(X)):
			X[i][0] = B1[i, :]@X + B2[i, :]@X + d[i][0]
	return X

B, d = get_matrix()
if LA.norm(B, ord=np.inf) < 1:
	X = seidel()
	print(X)
else:
	print("Chuan cua A (B) lon hon hoac bang 1 nen khong thoa man dieu kien")

#Kiem tra
print()
print()
A, d = get_matrix()
E = np.eye(len(A))
X = LA.inv(E - A)@d
print(X)
