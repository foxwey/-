import jieba
txt = open("三国演义.txt","r",encoding="gbk").read()
#排除非人名的，靠前的词语。
excludes = {"却说","二人","不可","荆州","不能","如此","如何","商议",\
"军士","主公","军马","左右","引兵","次日","大喜","天下","东吴","于是","今日"\
,"不敢","魏兵","人马","不知","陛下","一人","都督","众将","汉中"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) ==1:
        continue
    elif word == "孔明曰" or word =="诸葛亮":#出现人物别名时，也要统计
    	rword = "孔明"     
    elif word == "关公"or word =="云长":
    	rword = "关羽"
    elif word == "玄德" or word =="玄德曰":
    	rword = "刘备"
    elif word == "孟德" or word =="丞相曰" or word =="丞相" :
    	rword = "曹操"
    else:
    	rword = word
   
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
	del counts[word]
items = list(counts.items())#获取字段生成元组，强制转换成列表；其实可以直接元组。
items.sort(key=lambda x:x[1],reverse=True)# 元组/列表的X【0】是键，【1】是值；
#sort（可迭代对象，key=函数名，reverse=False/True） key是排序的依据,一般自定义一个函数。
#lambda是简略版函数定义。x是传入参数，冒号是函数表达式；返回的是一个函数。
for i in range(10):
	word,count = items[i]
	print("{:<10}{:>5}".format(word,count))