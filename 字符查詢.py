"""
=open(文件,'模式')
r - 讀取(檔案需存在)

w - 新建檔案寫入(檔案可不存在，若存在則清空)

a - 資料附加到舊檔案後面(游標指在EOF)

r+ - 讀取舊資料並寫入(檔案需存在且游標指在開頭)

w+ - 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)

a+ - 資料附加到舊檔案後面(游標指在EOF)，可讀取資料

b - 二進位模式
"""

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
