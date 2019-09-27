import random

def genpwd(length):
    a = 10**(length-1)
    b = 10**length-1
    return "{}".format(random.randint(a,b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))

#-------------求取输入数据后面的5个连续质数------------------------
#获取质数
def prime(m):
    flag = 0
    for i in range(2,m):
        if m%i==0:
           return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_<n else n_  #向上取整，没用math库中的ceil函数
#------连续5个质数----------
counter = 5
while counter >0:
	if prime(n_):
	    if counter>1:
	        print(n_,end=",") #用逗号连接输出，最后一位后不带逗号
	    else:
	        print(n_,end="")
	    counter -= 1
	n_ +=1
