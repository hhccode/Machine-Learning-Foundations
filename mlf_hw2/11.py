import numpy as np
import matplotlib.pyplot as plt

def mod(x, y):
    if x < 0:
        while x < 0:
            x += 4
    elif x > 0:
        while x >= 4:
            x -= 4
    
    return x

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

if __name__ == "__main__":
    a = 3.5
    x = np.linspace(0, 16, 1600)
    y = np.linspace(0, 16, 1600)

    for i in range(len(y)):
        tmp = y[i] * a
        y[i] = sign(abs(mod(tmp, 4)-2)-1)
    
    plt.plot(x,y)
    plt.show()