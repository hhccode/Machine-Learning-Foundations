import math
import numpy as np
from numpy.linalg import inv

def gradient_u(u, v):
    return pow(math.e, u) + v*pow(math.e, u*v) + 2*u - 2*v - 3

def gradient_v(u, v):
    return 2*pow(math.e, v) + u*pow(math.e, u*v) - 2*u + 4*v - 2

def gradient_uu(u, v):
    return pow(math.e, u) + v*v*pow(math.e, u*v) + 2

def gradient_vv(u, v):
    return 4*pow(math.e, 2*v) + u*u*pow(math.e, u*v) + 4

def gradient_uv(u, v):
    return pow(math.e, u*v) + u*v*pow(math.e, u*v) -2

def E(u, v):
    return pow(math.e, u) + pow(math.e, 2*v) + pow(math.e, u*v) + u*u - 2*u*v + 2*v*v - 3*u - 2*v 

if __name__ == "__main__":
    u = 0
    v = 0
    rate = 0.01

    for _ in range(5):
        gu = gradient_u(u, v)
        gv = gradient_v(u, v)
        guu = gradient_uu(u, v)
        gvv = gradient_vv(u, v)
        guv = gradient_uv(u, v)

        hessian = np.array([[guu, guv], [guv, gvv]])
        gradient = np.array([[gu], [gv]])

        u = u - np.matmul(inv(hessian), gradient)[0][0]
        v = v - np.matmul(inv(hessian), gradient)[1][0]
        
    print(E(u, v))