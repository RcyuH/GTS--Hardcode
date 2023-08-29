from sympy import *
t = symbols('t')
from sympy import roots, solve_poly_system
import numpy as np
import cmath
from numpy import linalg as LA

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
	f = open('1_Danielevsky.txt')
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

def format_matrix_1(A, k, StoreM): #Truong hop 1
	M = np.eye(len(A))
	M[k-1] = A[k]
	StoreM = M@StoreM
	return M@A@np.linalg.inv(M), StoreM

def format_matrix_2(A, k, index, StoreM): #Truong hop 2
	C = np.eye(len(A))
	temp = np.copy(C[:, k])
	C[:, k] = C[:, index]
	C[:, index] = temp
	A = C@(A@C)
	StoreM = C@StoreM 
	A, StoreM = format_matrix_1(A, k, StoreM)
	return A, StoreM

def format_matrix_3(A, k): #Truong hop 3 k -> n-1 || 0 -> k-1
	n = len(A)
	tmp1 = A[0:k, 0:k]
	tmp2 = A[k:n, k:n]
	return tmp1, tmp2

def conduct(A, StorePx):
	#GLOBAL VARIABLE
	StoreM = np.eye(len(get_matrix())) #Store Matrix
	for i in range(len(A)-1):
		k = len(A) - 1 - i
		if check(A, k) == -1:
			A, StoreM = format_matrix_1(A, k, StoreM)
		elif check(A, k) == -2:
			A, tmp = format_matrix_3(A, k)
			StorePx.append(tmp)
			conduct(A, StorePx)
		else:
			index = check(A, k)
			A, StoreM = format_matrix_2(A, k, index, StoreM)

	# #Dieu chinh thanh so dep :))
	# for i in range(len(A)):
	# 	for j in range(len(A)):
	# 		A[i][j] = round(A[i][j])

	StorePx.append(A)
	return A, StorePx

def main():
	A = get_matrix()
	StorePx = list()
	A, StorePx = conduct(A, StorePx)	
	a = Px_list(StorePx, t)
	print(a)
	eigValues = solve(a, t)
	print(eigValues)

	A = get_matrix()
	E = np.eye(len(A))

main()

#Kiem tra
print()
print()
A = get_matrix()
x, V = LA.eig(A)
print(x)
print(V)
