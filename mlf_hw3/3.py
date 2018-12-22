import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10)

def sign(x_):
    if x_ > 0:
        return 1
    else:
        return -1

def a_():
    y = []

    for xi in x:
        if sign(xi) != 1:
            y.append(1)
        else:
            y.append(0)
    
    plt.plot(x, y, color='blue', label='a')

def b_():
    y = []

    for xi in x:
        if sign(xi) >= 1:
            y.append(1)
        else:
            y.append(0)
    
    plt.plot(x, y, color='red', label='b')

def c_():
    y = []

    for xi in x:
        y.append(0.5 * pow(math.e, -xi))
    
    plt.plot(x, y, color='green', label='c')

def d_():
    y = []

    for xi in x:
        y.append(max(0, 1-xi))
    
    plt.plot(x, y, color='black', label='d')

def e_():
    y = []

    for xi in x:
        y.append(max(0, -xi))
    
    plt.plot(x, y, color='yellow', label='e')

if __name__ == "__main__":
    plt.figure(1)
    plt.ylim(-2, 2)
    a_()
    b_()
    c_()
    d_()
    e_()
    plt.legend()
    plt.show()