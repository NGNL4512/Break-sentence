import speech_recognition
import pyaudio
import time
import wave
import os

#播放語音檔與轉換成文字
def Voicemp3(printmp3):
    print("轉換語音檔為文字")
    #listen_recording(printmp3)
    e =speech_recognition.Recognizer()
    with speech_recognition.AudioFile(printmp3) as source:
        e.adjust_for_ambient_noise(source,duration=0)
        #audio=e.record(source,offset=9.776,duration=3)
        audio=e.record(source)
    txt=e.recognize_google(audio,language='zh-TW')
    return txt

#麥克風轉換文字    
def speakchinese():
    e =speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("請開始說話")
        #print("五秒內沒說話將判斷麥克風沒收到聲音")
        e.adjust_for_ambient_noise(source) #調整麥克風噪音
        #t=time.time()
        audio = e.listen(source)
        #if time.time()-t >= :
        #txt="麥克風沒收到聲音"
        try:
            txt=e.recognize_google(audio,language='zh-TW')
        except:
            txt="口語清楚點"
        return txt

#聆聽錄音檔
def listen_recording(printmp3):
    CHUNK=1024
    #開啟檔案
    file=wave.open(printmp3,"rb")
    p=pyaudio.PyAudio()
    #開啟串流 open stream
    stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                    channels=file.getnchannels(),
                    rate=file.getframerate(),
                    output=True)
    data=file.readframes(CHUNK)

    while data:
        stream.write(data)
        data=file.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
    
def readfile():
    filepath = "./ReadFile/" #存放音檔的路徑
    filename= os.listdir(filepath) #資料夾下的所有檔案 
    num=0
    for file in range(len(filename)):
        print(num+1, end=".")
        num+=1
        print(filename[file])
    name = input('請輸入檔名：')
    global speakname
    speakname=filename[int(name)-1]
    return filepath+filename[int(name)-1]
    
    print('---------聲音資訊------------') 
def init():
    #儲存路徑
    filename=readfile()
    outtxt = "./speaktxt/"+speakname+".txt" #錄音檔轉成的文字檔(名稱跟錄音檔相同)
    f1=open(outtxt,'w',encoding='UTF-8')
    #開語音檔
    print("播放語音")
    TEXT=Voicemp3(filename)
    print (TEXT)
    f1.write(TEXT+'\n')
    print('\n\n檔案'+outtxt+"已存檔")
# =============================================================================
#     outtxt = "./speaktxt/"+speakname+".txt"
#     f1=open(outtxt,'w',encoding='CP950')
#     TEXT=speakchinese()
#     print (TEXT)
#     f1.write(TEXT+'\n')
#     print('\n\n檔案'+outtxt+"已存檔")
#     f1.close()
# =============================================================================

if __name__ == '__main__':
    init()