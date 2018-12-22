import numpy as np
import math

learning_rate = 0.001
T = 2000

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def sigmoid(s):
    return (1 / (1 + math.pow(math.e, -s)))

def dot(w, x):
    res = 0

    for i in range(len(w)):
        res += w[i] * x[i]
    
    return res

def data_collect(dest):
    res = []

    with open(dest, "r") as file:
        for line in file:
            line = line.split()
            line.insert(0, "1")
            line = [float(num) for num in line]

            res.append(line)
    
    return np.array(res)

def stochastic_gradient_descent(data):
    N, dimension = data.shape
    dimension -= 1  # dimension = 21
    w = np.array([0.0 for _ in range(dimension)])
    
    for iteration in range(T):
        n = iteration % N
        y = data[n][dimension]
        theta = sigmoid(-y * dot(w, data[n][0:dimension]))

        gradient = np.array([(-y * theta * xi) for xi in data[n][0:dimension]])

        w = w - learning_rate * gradient

    return w

if __name__ == "__main__":
    training_data = data_collect("hw3_train.dat")
    
    weight = stochastic_gradient_descent(training_data)
    
    testing_data = data_collect("hw3_test.dat")
    N, dimension = testing_data.shape
    dimension -= 1  # dimension = 21


    error = 0
    for i in range(N):
        if testing_data[i][dimension] != sign(dot(weight, testing_data[i][0:dimension])):
            error += 1
        
    print(error/N)