# Machine Learning Foundation Hw2

使用 Python3 來實作，並利用 python 套件 `matplotlib` 來畫出各個更新次數出現頻率的 Histogram。

## Prerequisites

```
Python: 3.7.1
matplotlib: 3.0.2
numpy: 1.15.4
```

## Execute

```
python3 hw2.py
```

## Result

會產生出 Histogram，橫軸為 Ein - Eout 的值，縱軸為出現次數
![](https://i.imgur.com/1Miq1sK.png)

## Find out

大部分的 Ein - Eout 都落在 -0.2 ~ 0.0 之間，證實了 Hoeffding inequality，也就是發生壞事情的機率很低。
