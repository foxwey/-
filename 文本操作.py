#字符串常见的八个方法：
#str.lower()  str.upper()返回字符串的副本，全大写或全小写
#str.split(sep==None) 返回一个列表，由str根据sep分割组成
#str.count(sub) 返回子串sub在str中出现的次数
#str.replace(old,new)替换
#str.center(width,fillchar)居中
#str.strip(char)从str中去除其左右两侧的特定字符
#char.join(str)在str的每个元素中插入一个特定字符。

mystr="A1092934 # 123442144 # ww.efdfssdfv.com"
mylist=mystr.split(" # ")#切割，生成列表
print(mylist)

mystr="8848  n小姐 女 22 162"
mylist=mystr.split(" ")
print(mylist)

mystr="8848 n小姐 女 22 162"
mylist=mystr.split(" ",2)#识别前两个标志切割
print(mylist)

#三个引号能输出字符中的单双引号。
mystr="""
十年生死两茫茫，不思量，自难忘。
千里孤坟，无处话凄凉。
纵使相逢应不识，尘满面，鬓如霜。 
"""
mylist=mystr.splitlines()#值为Ture，则保留换行，实际换行两次
for data in mylist:
	print(data)

mystr = "零一二三四五六七八九十"
print(mystr[:3])#切片操作
print(mystr[3:])
print(2*mystr[:3])#字符串重复
print(mystr[:8:2])#步长为2的切片操作
print(mystr[::-1])#倒序

for i in range(12):
	print(chr(9800+i),end="")#统一字符编码包含世界所有语言，输出星座对应的符号

print("-".join("asdfasdg"))
print("---".join("asdf asdg"))
print(len("asdfasdg"))

mystr="hello 123 hello 123"
print(mystr.replace("123","python")) 
print(mystr)
print(mystr.replace(" ","")) 


print("  ab c ".strip())#去除前后的空格
print("  ab c ".rstrip())#去除后的空格
print("  ab c ".lstrip())#去除前的空格

mystr = input("请输入几个词，以-分割")
mylist = mystr.split("-")
print(mylist[0]+"+"+mylist[-1])
