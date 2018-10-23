
# =============================================================================
# from snownlp import
#  SnowNLPs = SnowNLP(u'一次满意的购物')s.words
# 1) s.words        词语
# 2) s.sentences   句子
# 3) s.sentiments 情感偏向,0-1之间的浮点数，越靠近1越积极
# 4) s.pinyin         转为拼音
# 5) s.han             转为简体
# 6) s.keywords(n) 提取关键字,n默认为5
# 7) s.summary(n)  提取摘要,n默认为5
# 8) s.tf                   计算term frequency词频
# 9) s.idf                 计算inverse document frequency逆向文件频率
# 10) s.sim(doc,index)          计算相似度
# =============================================================================

from snownlp import sentiment
#需要UTF-8編碼
Negative='D:/Anaconda3/envs/py3.6/Lib/site-packages/snownlp/sentiment/neg1.txt'
positive='D:/Anaconda3/envs/py3.6/Lib/site-packages/snownlp/sentiment/pos1.txt'

sentiment.train(Negative,positive) #負面和正面

sentiment.save('sentiment2.marshal')
print("已存檔")