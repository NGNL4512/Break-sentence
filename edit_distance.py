import os

def editDistance(s1, s2):
    if len(s1) > len(s2):#長度比較
        s1, s2 = s2, s1

    distances = range(len(s1) + 1) #從[0,1,2,......,s1+1]
    for i2, c2 in enumerate(s2): #迭代index,item
        distances_ = [i2+1]
        #print(i2,c2)
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def sentence_cut(sent):
    sentence=[]
    f=open(sent,'r+')
    w=f.read()
    for word in w.split('\n'):
        sentence.append(word)
    f.close()
    return sentence
    
def similar_score(s1):
    filepath = "./sentence/" #存放文字檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    bignum=100000
    for file in range(len(filename)):
        s2=sentence_cut(filepath+filename[file])
        for i in range(0,s2.__len__(),1):
            distance=editDistance(s1, s2[i])
            if distance < bignum:
                bignum=distance
                text=s2[i]
                osfile=filename[file]
    osfile=osfile.replace(".txt","")
    return bignum,text,osfile
if __name__=='__main__':
    s1=input("請輸入單字或句子:")
    distance,text,mood=similar_score(s1)
    print("跟",s1,"\n差距最短的是",text,"\n距離為",distance,"\n情緒歸類在",mood)
    
