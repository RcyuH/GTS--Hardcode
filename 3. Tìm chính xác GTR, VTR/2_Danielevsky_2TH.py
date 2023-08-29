from sympy import *
t = symbols('t')
from sympy import roots, solve_poly_system
import numpy as np
import cmath
import math
from numpy import linalg as LA

Store_Matrix = list()
delta = 0.00000000001

#HPT: AX = λX (dat x = λ cho de viet)

def Px(matrix_tmp, x):
	r = len(matrix_tmp[0])
	f = ((-1)**r)*(x**r)
	for j in range(r):
		f = f - ((-1)**r)*matrix_tmp[0][j]*(x**(r-j-1))
	return f

def Px_list(list_matrix_tmp, x):
	f = 1
	for matrix_tmp in list_matrix_tmp:
		f = f*Px(matrix_tmp, x)
	return f

def get_matrix(): #Doc ma tran A tu file
	f = open('2_Danielevsky_2TH.txt')
	tmp_A = [[], [], [], []] #TU KHOI TAO PHU HOP VOI SO HANG VA COT TRONG FILE 
	tmp_b = [[], [], [], []]
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
	return A

def check(A, k): #Kiem tra xem ma tran A hien thoi thuoc case nao
	n = len(A)-1
	if A[k][k-1] != 0: return -1
	else:
		for j in range(k):
			if A[k][j] != 0: return j #Tra ve dia chi cua cot chua phan tu khac 0 tren hang k
		return -2

def format_matrix_1(A, k): #Truong hop 1
	M = np.eye(len(A))
	M[k-1] = A[k]
	Store_Matrix.append(M)
	return M@A@np.linalg.inv(M)

def format_matrix_2(A, k, index): #Truong hop 2
	C = np.eye(len(A))
	temp = np.copy(C[:, k])
	C[:, k] = C[:, index]
	C[:, index] = temp
	A = C@(A@C)
	Store_Matrix.append(C)
	A = format_matrix_1(A, k)
	return A

def format_matrix_3(A, k): #Truong hop 3 k -> n-1 || 0 -> k-1
	n = len(A)
	tmp1 = A[0:k, 0:k]
	tmp2 = A[k:n, k:n]
	return tmp1, tmp2

def conduct(A):
	for i in range(len(A)-1):
		k = len(A) - 1 - i
		if check(A, k) == -1:
			A = format_matrix_1(A, k)
		elif check(A, k) == -2:
			print("TH3")
			return 0
		else:
			index = check(A, k)
			A = format_matrix_2(A, k, index)
	return A

def get_eigVectors(A, eigValues):
	eigVectors = list()
	tmp = np.eye(len(A))
	for i in Store_Matrix:
		tmp = i@tmp
	tmp = np.linalg.inv(tmp)
	tmp1 = np.zeros((len(A), 1))
	for eigValue in eigValues:
		for i in range(len(A)):
			tmp1[i, :] = eigValue**(len(A) - i - 1)
		eigVectors.append((tmp@tmp1)/LA.norm(tmp@tmp1))
	return eigVectors

	
def main():
	A = get_matrix()
	P = conduct(A)

	# #Dieu chinh thanh so dep :))
	# for i in range(len(A)):
	# 	for j in range(len(A)):
	# 		A[i][j] = round(A[i][j])

	PTDT = Px(P, t) #phuong trinh dac trung
	eigValues = solve(PTDT, t)
	for i in range(len(eigValues)):
		eigValues[i] = complex(eigValues[i])
		if math.fabs(eigValues[i].imag) < delta:
			eigValues[i] = eigValues[i].real 
	print(eigValues)

	try: 
		eigVectors = get_eigVectors(A, eigValues)
		print(eigVectors)
	except: print("GTR co so phuc => Chua lam duoc voi so phuc")

main()

#Kiem tra
print()
print()
A = get_matrix()
x, V = LA.eig(A)
print(x)
print(V)
