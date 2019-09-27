def getNum():
	nums = []
	iNumStr = input("请输入数字（回车键结束）")
	while iNumStr !="":
		nums.append(eval(iNumStr))
		iNumStr = input("请输入数字（回车键结束）")
	return nums
#-------平均数------------
def mean(numbers):
	s = 0.0
	for num in numbers:
		s = s + num
	return s /len(numbers)
#-------方差------------
def dev(numbers,mean):
	sdev = 0.0
	for num in numbers:
		sdev = sdev + (num - mean)**2
	return pow(sdev /(len(numbers)-1),0.5)
#-------中位数------------
def median(numbers):
	sorted(numbers)#列表排序
	size = len(numbers)
	if size%2 ==0:
		med = (numbers[size//2-1] + numbers[size//2])/2
	else:
		med = numbers[size//2]
	return med

n = getNum()
m = mean(n)
print("平均数为：{:.2f}；方差为：{:.2f}；中位数为：{}".format(m,dev(n,m),median(n)))