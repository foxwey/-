#-------序列为基类，字符串、列表、元组都是序列----------
#-------集合的数据为无序且不重复，其它为有序，元组的数据不可更改-------------------------------

#定义空列表lt
lt = []
#向lt新增5个元素
lt += [1,2,3,4,5]
print(lt)
#修改lt中的第2个元素
lt[2] = 6
print(lt)
#向lt中的第2个位置增加一个元素
lt.insert(2,7)
print(lt)
#从lt中的第1个位置删除一个元素
del lt[1]
print(lt)
#删除lt中第1~3位置元素
del lt[1:4]
print(lt)
#判断lt中是否包含数字0
print(    0 in lt   )
#向lt新增数字0
lt.append(0)
print(lt)
#返回数字0所在lt中索引
print(  lt.index(0)   )
#lt的长度
print(    len(lt)   )
#lt中最大元素
print(   max(lt)    )
#清空lt
lt.clear()
print(lt)