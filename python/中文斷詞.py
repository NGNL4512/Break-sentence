import jieba
#切換繁體詞庫
jieba.set_dictionary('D:/Anaconda3/envs/py3.6/Lib/site-packages/jieba/dict1.txt')
#jieba.add_word('錢標') 手動增加詞庫
cutin='C:/Users/ASUS/Desktop/python/voice.txt'
outtxt='C:/Users/ASUS/Desktop/python/斷詞輸出/斷詞輸出.txt'

f=open(cutin,'r')
out=open(outtxt,'w',encoding='UTF-8')

w=f.read()

seg_list = jieba.cut(w)  # 默认是精确模式

out.write("/".join(seg_list))
print('\n\n檔案'+outtxt+"已存檔")
f.close()
out.close()
