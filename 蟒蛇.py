import turtle

turtle.setup(650,350,200,200)#绘图窗口在屏幕的位置，长宽。
turtle.penup()
turtle.fd(-250)#同.forward作用一样
turtle.pendown()
turtle.pensize(25)#同.width作用一样
turtle.color("purple")
turtle.seth(-40)#设置角度，同.setheading和.left和.right作用相同

for i in range(4): #迭代次数为4；i在下面可以引用，也可以不用。
	turtle.circle(40,80)#第二个参数弧形角度，默认为360度
	turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()#手工关闭窗口，如果不加则自动关闭窗口