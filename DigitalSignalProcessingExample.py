#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt


#csv,txtファイルなどからデータ読み取る関数　データの形に合わせて修正する必要ある。
def read():
    y = []
    x = []
    count = 0;
    with open('data.txt', encoding= 'utf-8') as file:
        for line in file:
            Arraytext = line.split(",")
            y.append(float(Arraytext[1]))        
            x.append(count)
            count += 1
    return x,y


#データ取得
x,y = temperature()
#データの表示
plt.plot(x, y)
plt.show()


#スペクトログラムこの関数にxyを渡せばスペクトログラム は表示される
# import matplotlib.pyplot as plt が必要
#参考URL http://ism1000ch.hatenablog.com/entry/2014/07/16/022304
pxx, freq, bins, t = plt.specgram(y,Fs = len(x)*3,scale_by_freq = True)
plt.show()


#音声データでやる場合
import scipy.io.wavfile as wv 
#拡張子が.wavなデータじゃないと多分エラー出る。
wave = "filename.wav"
rate, data = wv.read(wave)
print(rate)
#一次元配列にする
print(data.reshape(-1))
pxx, freq, bins, t = plt.specgram(data.reshape(-1),Fs = rate,scale_by_freq = True)
plt.show()

#おまけ　ランダムを足すことで、高周波成分を追加できると思う
import random
index = 0
for datay in y:
    if index % 5 ==  0:
        y[index] += random.uniform(5, 8)      
    index += 1

