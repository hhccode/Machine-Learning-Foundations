import numpy as np
import random

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def target(x1, x2):
    if pow(x1, 2) + pow(x2, 2) - 0.6 > 0:
        return 1
    else:
        return -1

def transform(size, x):
    z = np.zeros((size, 6))

    for i in range(size):
        z[i][0] = 1
        z[i][1] = x[i][1]
        z[i][2] = x[i][2]
        z[i][3] = x[i][1] * x[i][2]
        z[i][4] = pow(x[i][1], 2)
        z[i][5] = pow(x[i][2], 2)

    return z

def date_generate(size):
    x = np.zeros((size, 3))
    y = np.zeros((size, ), dtype=np.int16)

    for i in range(size):
        x[i][0] = 1
        x[i][1] = np.random.uniform(-1, 1)
        x[i][2] = np.random.uniform(-1, 1)
        y[i] = target(x[i][1], x[i][2])

        if np.random.uniform(0.0, 1.0) <= 0.1:
            y[i] = -y[i]  

    trans_x = transform(size, x)

    return np.asmatrix(trans_x), np.asmatrix(y).transpose()

def linear_regression(x, y):
    pinv_x = np.linalg.pinv(x)
    w = pinv_x * y

    return w

def Eout(size, w, x, y):
    error = 0
    for i in range(size):
        if y[i] != sign(x[i] * w):
            error += 1
    
    return error / size

if __name__ == "__main__":
    
    w4 = np.array([[-1], [-0.05], [0.08], [0.13], [1.5], [1.5]])
    
    e_out = 0
    for i in range(1000):
        x, y = date_generate(1000)
        e_out += Eout(1000, w4, x, y)
    
    print(e_out / 1000)
