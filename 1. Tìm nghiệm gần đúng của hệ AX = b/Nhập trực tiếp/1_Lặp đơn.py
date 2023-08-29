import numpy as np

#HPT: X = BX + d => Ta cần tự đưa về dạng này

#Nhập X0
X0 = np.array([[0], [0], [0]])

#Nhập B
B = np.array([[0, -0.1, -0.1], [-0.2, 0, -0.1], [-0.2, -0.2, 0]])

#Nhập d 
d = np.array([[1.2], [1.3], [1.4]])

#Số lần lặp
n = 10

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