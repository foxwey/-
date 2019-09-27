#----------升级版：数字线段有间隙，加年月日，颜色-----------------
import turtle,time
def drawGap():
	turtle.penup()
	turtle.fd(5)
def drawLine(draw):
	drawGap()
	turtle.pendown() if draw else turtle.penup()
	turtle.fd(40)
	drawGap()
	turtle.right(90)
def drawDigit(digit):
	drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,6,8,] else drawLine(False)
	turtle.left(90) #抵消drawLine函数中的右转向，纠正划线方向
	drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
	drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
	drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
	turtle.left(180) #调整方向，水平向右。每次最后箭头的方向都要考虑drawLine中的右转90
	turtle.penup()  #抬起向右移动
	turtle.fd(20) 
def drawDate(date):
	turtle.pencolor("red")
	for i in date:
		if i =="-":
			turtle.write("年",font=("Arial","16","normal"))
			turtle.pencolor("green")
			turtle.fd(40)
		elif i == "+":
			turtle.write("月",font=("Arial","16","normal"))
			turtle.pencolor("blue")
			turtle.fd(40)
		elif i == "=":
			turtle.write("日",font=("Arial","16","normal"))
		else:
			drawDigit(eval(i))		
def main():
	turtle.setup(800,350,200,200)  #定义画布大小及位置
	turtle.penup()
	turtle.fd(-300)  #定义起始位置靠左
	turtle.pensize(5)
	drawDate(time.strftime("%Y-%m+%d=",time.gmtime())) #格式化时间time.strftime（“”，t）
	turtle.hideturtle() #隐藏箭头
	turtle.done() #停住画布，用户手动关闭
main()