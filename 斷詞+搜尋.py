import jieba
import os
#切換繁體詞庫
jieba.set_dictionary('dict1.txt')
#jieba.add_word('增加') 手動增加詞庫
def cutword(filename):
    cutin=filename #放進去段詞的文章
    outtxt='./斷詞輸出/斷詞輸出.txt'

    f=open(cutin,'r')
    out=open(outtxt,'w',encoding='UTF-8')

    w=f.read()

    seg_list = jieba.cut(w)  # 默认是精确模式

    out.write("/".join(seg_list))
    f.close()
    out.close()

def searchkey():
    outtxt='C://Users/ASUS/Desktop/python/斷詞輸出/斷詞輸出.txt'

    keytxt='C://Users/ASUS/Desktop/python/keyword.txt'

    fl=open(outtxt,'r+',encoding='UTF-8')
    f=open(keytxt,'r')
    w=fl.read()
    lines = f.readlines()
    keyword = []  ## 空列表, 将第i行数据存入list中
    for i in range(0,lines.__len__(),1):
        for word in lines[i].split('，'):
            keyword.append(word) 
    f.close()
    
    allkey=[]
            
    for j in range(0,len(keyword),1):
        a=0
        while True:
            idkey=w.find(keyword[j],a)
            if idkey==-1:
                break
            else:
                a=idkey+1
                allkey.append(keyword[j])
                        
    if allkey==[]:
        print("沒有關鍵字")
    else:
        sum=0
        allkey.sort()
        allkeyset=set(allkey)
        for item in allkeyset:
            print (item,":",allkey.count(item),"次")
            sum+=allkey.count(item)
        print("所有關鍵字總共出現",sum,"次")
    fl.close()
    
def readfile():
    filepath = "./speaktxt/" #存放文字檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    num=0
    for file in range(len(filename)):
        print(num+1, end=".")
        num+=1
        print(filename[file])
    name = input('請輸入檔名：')
    return filepath+filename[int(name)-1]
def init():
    filename=readfile()
    cutword(filename)
    searchkey()
if __name__ == '__main__':
    init()