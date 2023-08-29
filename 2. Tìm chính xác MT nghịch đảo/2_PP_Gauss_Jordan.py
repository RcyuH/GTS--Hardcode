import numpy as np
import cmath

#HPT: AX = E
#Doc A tu file
f = open('2_Gauss Jordan.txt')
tmp_A = [[], [], [], [], [], [], []] #TU KHOI TAO PHU HOP VOI SO HANG VA COT TRONG FILE 
tmp_b = [[], [], [], [], [], [], []]
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

#Ma tran B = A|E
B = np.zeros((len(A), len(A) + len(E)))
for i in range(len(B)):
	for j in range(len(B[0])):
		if j <= len(A)-1:
			B[i][j] = A[i][j]
		else:
			B[i][j] = E[i][j-len(A)]

print(B)

#Tinh toan:
for i in range(len(B)):
	for j in range(len(B)):
		if j != i:
			B[j] = B[j] - B[i]*(B[j][i]/B[i][i])
	B[i] = B[i]/B[i][i]
print()
print(B)

#Chi in ra ma tran nghich dao
print()
for i in range(len(B)):
	for j in range(len(B[0])):
		if j > len(A)-1:
			print(B[i][j], end=" ")
	print()

# Kiem tra
print()
print()
print(np.linalg.inv(A))