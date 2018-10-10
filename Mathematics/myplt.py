# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
#定義域の指定　以下では-10<=x<=10 を0.1毎に刻んでいる
x = np.arange(-10,10,0.1) 

#y = x^2 + 2x + 1（二次関数）をpythonで書くと下のようになる。
#y = x**2 + 2*x + 1

#y = 標準正規分布
y = (np.exp(-x**2/2)) / np.sqrt(2*np.pi)

#グラフの軸
plt.xlabel('X')
plt.ylabel('Y')

#表示
plt.plot(x,y) 
plt.show()
