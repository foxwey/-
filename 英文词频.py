#------------------------
def getText():
	txt = open("TheThreeMusketeers.txt","r",errors='ignore').read()
	txt = txt.lower()  #字符串全部转为小写
	for ch in '"!@#$%^&*()_+-=|[],./<>?':   #将特殊字符替换为空格，方便切割
	    txt = txt.replace(ch," ")
	return txt
myTxt = getText()
words = myTxt.split()
counts = {}
for word in words:
	counts[word] = counts.get(word,0) + 1 #为键值对赋默认值为0.

items = list(counts.items()) #字典中items函数返回可遍历的（键、值）元组数组
items.sort(key=lambda x:x[1],reverse=True)  #列表中lambda指定哪一列作为比较,默认从大到小
#sort是直接改变列表，sorted是生成一个新的列表，不改变原列表
for i in range(10):
	word,count = items[i]
	print("{:<10}{:>5}".format(word,count))

