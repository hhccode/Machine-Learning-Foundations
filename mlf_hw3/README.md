# Machine Learning Foundation Hw3

使用 Python3 來實作，並利用 python 套件 `matplotlib` 來畫出 Ein 和 Eout 變化的折線圖。

## Prerequisites

```
Python: 3.6.5
matplotlib: 2.2.2
numpy: 1.14.3
```

## Execute

```
python3 hw3.py
```

## Result

### Question3

會產生出折線圖，縱軸為 Ein 的值，橫軸為 iteration 次數。
其中 Gradient descent 的 learning rate 為 `0.01`，而 SGD 的 learning rate 為 `0.001`。
![](https://i.imgur.com/5wNS8jX.png)

### Question4

會產生出折線圖，縱軸為 Eout 的值，橫軸為 iteration 次數。
其中 Gradient descent 的 learning rate 為 `0.01`，而 SGD 的 learning rate 為 `0.001`。
![](https://i.imgur.com/0sLwtv9.png)



## Find out

### Question3

因為 SGD 的 learning rate 比較小的關係，所以 SGD 的 Ein 下降的速度會比 Gradient descent 還要的慢，而且 SGD 每次是隨機選一筆 data 來計算 gradient，所以會較為不精準，可能會使得 Ein 上升，但整體的 Ein 趨勢是下降的。

### Question4

SGD 所選出的 w 雖然可以有效的使得 Ein 下降，但是在 Eout 上的表現卻沒有像 Gradient descent 表現得那麼好，可以想像雖然 SGD 相對於 Gradient descent 減少了大量的計算時間，但是卻是用準確率所付出的代價。

