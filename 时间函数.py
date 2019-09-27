#时间库常见的三个函数为time()获取当前机器时间戳;
#ctime()为人阅读模式；gmtime()其它函数可调用的格式。
# %Y表示年份，%m表示月份01~12，%B表示月份名称，%b表示月份缩写
#%d表示日期，%A表示星期。%a表示星期缩写。%H表示24小时制，%I表示12小时制
#%P表示上/下午，%M表示分钟，%S表示秒
#strtime()将时间转化为字符串  strptime()将时间字符串转为时间
#perf_counter()返回一个CPU级别的精准时间计数值。两次调取取差值
#sleep() 程序休眠等待n秒

import time

t = time.gmtime()
s = time.strftime("%Y-%m-%d %H:%M:%S",t) #strftime格式化时间
print(s)


scale = 20
print("执行开始".center(scale,"-"))
start = time.perf_counter()
for i in range(scale+1):
	a = "*"*i
	b = '.'*(scale-i)
	c = (i/scale)*100
	dur = time.perf_counter()-start
	print("\r{:^3.0f}%[{}->{}{:.2f}]".format(c,a,b,dur),end="") # ^3表示固定占3行中显示
	time.sleep(0.1)

print("\n"+"执行结束".center(scale,"-"))

