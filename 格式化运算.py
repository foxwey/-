num = 190
money = 3000
newmoney = 4000 #格式化需严格对应

mystr = "王铁柱的女神有%d个备胎，他花了%.2f元买了个手机，\
女生说他是好人；另一个备胎花了%.2f元租了辆奔驰，睡了女神。"%(num,money,newmoney)

print(mystr)

print("王铁柱的女生是%s"%("凤姐"))

print("王铁柱的女神有{}个备胎".format(num))

#表示固定占10个字符宽度，居中对齐。>表示左对齐，<表示右对齐。
print("{:^10}\n{:^10}\n{:^10}".format(num,money,newmoney)) 
#分号：左侧可以加0，1，2这样序号，也可以直接省略

#对齐，默认右对齐，-表示左对齐，0表示填充0
print("%-10.2f %f"%(1.23,1234))
print("%-10.2f %f"%(1.2345,3.133))
print("%-10.2f %f"%(1.2323,1.234))

print("%010.2f %f"%(211.2345,3.133))
print("%010.2f %f"%(1.2323,1.234))
#------------平方根格式化--------------
a = eval(input("请输入一个整数"))
print("{0:+>30.3f}".format(pow(a,0.5))) #30的宽度，>表示右对齐，以+号填充 

scale = 20
print("执行开始".center(scale,"-"))
for i in range(scale+1):
	a = "*"*i
	b = '.'*(scale-i)
	c = (i/scale)*100
	print("{:^3.0f}%[{}->{}]".format(c,a,b)) #  ^3表示固定占3行中显示

print("执行结束".center(scale,"-"))

for i in range(101):
	print("\r{:3}%".format(i),end='')
	time.sleep(0.1)