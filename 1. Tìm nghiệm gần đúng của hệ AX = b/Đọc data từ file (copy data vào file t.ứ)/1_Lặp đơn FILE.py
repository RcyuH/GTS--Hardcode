import numpy as np

#HPT: X = BX + d => Ta cần tự đưa về dạng này

#Nhập X0
X0 = np.array([[0], [0], [0], [0], [0], [0], [0]])

#Doc B va Doc d tu file
f = open('1_data1.txt')
tmp_B = [[], [], [], [], [], [], []] #Khoi tao phu hop voi du lieu trong file 
tmp_d = [[], [], [], [], [], [], []]
i = 0
j = 0
for line in f:
	number_array = line.split()
	if len(number_array) == 2:
		SoHang = float(number_array[0])
		SoCot = float(number_array[1])
	elif len(number_array) == 1:
		tmp_d[j].append(float(number_array[0]))
		j += 1
	else:
		for number in number_array:
			tmp_B[i].append(float(number))
		i += 1
B = np.array(tmp_B)
d = np.array(tmp_d)

#Số lần lặp
n = 50

#Chuan cua B
chuanhang = np.linalg.norm(B, ord=np.inf)
chuancot = np.linalg.norm(B, ord=1)
print("Chuan hang cua B la: " + str(chuanhang))
print("Chuan cot cua B la: " + str(chuancot))
if chuanhang < 1: 
	chuan = chuanhang
	print("Ta tinh toan theo chuan hang")
	flag = 2
elif chuancot < 1: 
	chuan = chuancot
	print("Ta tinh toan theo chuan cot")
	flag = 1
else: 
	print("Khong co chuan nao thoa man nho hon 1")
	flag = 0


#Tinh toan
if flag == 2: 
	for i in range(n):
		saiso = (chuan/(1-chuan))*np.linalg.norm(B@X0 + d - X0, ord=np.inf)
		X0 = B@X0 + d
		print("X" + str(i+1) + " = " + str(X0) + "      Saiso" + str(i+1) + " = " + str(saiso))
elif flag == 1: 
	for i in range(n):
		saiso = (chuan/(1-chuan))*np.linalg.norm(B@X0 + d - X0, ord=1)
		X0 = B@X0 + d
		print("X" + str(i+1) + " = " + str(X0) + "      Saiso" + str(i+1) + " = " + str(saiso))
else:
	print("ERROR")