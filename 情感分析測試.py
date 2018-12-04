from snownlp import sentiment
from snownlp import SnowNLP

analysis='C:/Users/ASUS/Desktop/python/斷詞輸出/斷詞輸出.txt'
ana=open(analysis,'r',encoding='UTF-8')
emotion=ana.read()
print(emotion)
q = SnowNLP(emotion) #分析句子
print('============\n',q.sentiments)
ana.close()