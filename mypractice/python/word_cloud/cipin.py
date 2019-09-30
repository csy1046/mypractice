import jieba
from collections import Counter

text = open('yanjiang.txt',encoding='utf-8',errors='ignore').read()
text_jieba = list(jieba.cut(text))
c = Counter(text_jieba)
common_c = c.most_common(100)
for i in common_c:
    print(i)
