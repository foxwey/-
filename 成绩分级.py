#分支结构，循环结构，
#—————————玫瑰数：4位数n的每位上的数字的n次幂等于本身—————————
for i in range(1000,9999):
    s = str(i)
    a = s[0]
    b = s[1]
    c = s[2]
    d = s[3]
    if pow(eval(a),i)+pow(eval(b),i)+pow(eval(c),i)+pow(eval(d),i) ==i:
        print(i)

#-------------成绩分级------------
score = eval(input())
if score >=90:
	grade = "A"
elif score >=80:
	grade = "B"
elif score >=70:
	grade = "C"
elif score >=60:
	grade = "D"
else :
	grade = "E"
print("你的成绩是："+grade)

