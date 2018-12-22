import math

def gradient_u(u, v):
    return pow(math.e, u) + v*pow(math.e, u*v) + 2*u - 2*v - 3

def gradient_v(u, v):
    return 2*pow(math.e, v) + u*pow(math.e, u*v) - 2*u + 4*v - 2

def E(u, v):
    return pow(math.e, u) + pow(math.e, 2*v) + pow(math.e, u*v) + u*u - 2*u*v + 2*v*v - 3*u - 2*v 

if __name__ == "__main__":
    u = 0
    v = 0
    rate = 0.01

    for _ in range(5):
        new_u = u - rate * gradient_u(u, v)
        new_v = v - rate * gradient_v(u, v)
        u, v = new_u, new_v
    
    print(E(u, v))