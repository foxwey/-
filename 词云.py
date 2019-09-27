import wordcloud
import jieba
from imageio import imread# 直接引入库中的函数，就不用a.b的结构来使用函数
mask = imread("nanren.png")

f = open("zhizao.txt","r",encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)

w = wordcloud.WordCloud(font_path="msyh.ttc",\
	width=500,height=700,background_color="white",\
	max_words=36,mask=mask)
w.generate(txt)
w.to_file("gongye.jpg")