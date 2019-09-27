#方法一为科学计算方法，方法二为蒙特卡罗算法：通过随机撒点计算落在方形中扇形的比例。
pi = 0
n = 100
for k in range(n):
	pi +=1/pow(16,k)*(\
		4/(8*k+1)-2/(8*k+4)-\
		1/(8*k+5)-1/(8*k+6))
print("圆周率值是：{}".format(pi))


#---------------蒙特卡洛撒点方法--------------------
from random import random
from time import perf_counter
darts = 1000*1000
hits = 0 
start = perf_counter()
for i in range(1,darts+1):
	x,y=random(),random()
	dist = pow(x**2+y**2,0.5)
	if dist <= 1.0:
		hits = hits + 1
pi = 4 * (hits/darts)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}".format(perf_counter()-start))
