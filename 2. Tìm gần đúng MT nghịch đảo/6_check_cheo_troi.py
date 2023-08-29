import numpy as np 
import cmath
import math
from numpy import linalg as LA
from numpy.linalg import norm

def get_matrix(): #Doc ma tran A tu file
	f = open('6_check_cheo_troi.txt')
	tmp_A = [[], [], [], [], [], [], [], []] #TU KHOI TAO PHU HOP VOI SO HANG VA COT TRONG FILE 
	tmp_b = [[], [], [], [], [], [], [], []]
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

def check_troi_hang(A):
	for i in range(len(A)):
		tmp1 = math.fabs(A[i][i])
		tmp2 = 0
		for j in range(len(A)):
			if j != i: tmp2 += math.fabs(A[i][j])
		if tmp2 >= tmp1: return False
	return True

def check_troi_cot(A):
	for j in range(len(A)):
		tmp1 = math.fabs(A[j][j])
		tmp2 = 0
		for i in range(len(A)):
			if i != j: tmp2 += math.fabs(A[i][j])
		if tmp2 >= tmp1: return False
	return True

A = get_matrix()
print(check_troi_hang(A))
print(check_troi_cot(A))