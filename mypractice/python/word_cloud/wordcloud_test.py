#-*- coding:utf-8 -*-
from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from collections import Counter

files = open('yanjiang.txt',encoding='utf-8',errors='ignore').read()
text_jieba = list(jieba.cut(files))
c = Counter(text_jieba)
common_c = c.most_common(100)
bg_pic = imread('b.png')
wc = WordCloud(font_path = '1.4.ttf',background_color='red',width=1000, height=800,mask=bg_pic,max_words=2000,max_font_size=1000,)
wc.generate_from_frequencies(dict(common_c))
# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file('anne.jpg')
