import numpy as np
import math
import matplotlib.pyplot as plt

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

    with open(dest, "r") as f:
        for line in f:
            line = line.split()
            line.insert(0, "1")
            line = [float(num) for num in line]

            res.append(line)
    
    return np.array(res)

def E_in(w, data):
    N, dimension = data.shape
    dimension -= 1  # dimension = 21
    Ein = 0

    for n in range(N):
        y = data[n][dimension]
        Ein += math.log(1 + math.pow(math.e, -y * dot(w, data[n][0:dimension])))

    return Ein / N

def E_out(w, data):
    N, dimension = data.shape
    dimension -= 1  # dimension = 21

    Eout = 0
    for n in range(N):
        if data[n][dimension] != sign(dot(w, data[n][0:dimension])):
            Eout += 1
        
    return Eout / N

def gradient_descent(data, learning_rate):
    N, dimension = data.shape
    dimension -= 1  # dimension = 21
    w = np.array([0.0 for _ in range(dimension)])
    wlist = [w]

    for _ in range(T):
        
        gradient = np.array([0.0 for _ in range(dimension)])

        for n in range(N):
            y = data[n][dimension]
            theta = sigmoid(-y * dot(w, data[n][0:dimension]))

            gradient += [(-y * theta * xi) for xi in data[n][0:dimension]]

        gradient /= N
        w = w - learning_rate * gradient
        wlist.append(w)

    return wlist

def stochastic_gradient_descent(data, learning_rate):
    N, dimension = data.shape
    dimension -= 1  # dimension = 21
    w = np.array([0.0 for _ in range(dimension)])
    wlist = [w]

    for iteration in range(T):

        n = iteration % N
        y = data[n][dimension]
        theta = sigmoid(-y * dot(w, data[n][0:dimension]))

        gradient = np.array([(-y * theta * xi) for xi in data[n][0:dimension]])

        w = w - learning_rate * gradient
        wlist.append(w)

    return wlist

if __name__ == "__main__":
    training_data = data_collect("hw3_train.dat")
    testing_data = data_collect("hw3_test.dat")
    
    GD_wlist_19 = gradient_descent(training_data, 0.01)

    GD_Ein_19 = []
    for w in GD_wlist_19:
        GD_Ein_19.append(E_in(w, training_data))
       
    SGD_wlist_20 = stochastic_gradient_descent(training_data, 0.001)

    SGD_Ein_20 = []
    for w in SGD_wlist_20:
        SGD_Ein_20.append(E_in(w, training_data))
    
    plt.figure(1)
    plt.title('Ein')
    plt.xlabel('Iteration')
    plt.ylabel('Ein')
    plt.plot(range(T+1), GD_Ein_19, color='blue', label='Gradient descent')
    plt.plot(range(T+1), SGD_Ein_20, color='red', label='SGD')
    plt.legend(loc='upper right')

    
    
    GD_Eout_19 = []
    for w in GD_wlist_19:
        GD_Eout_19.append(E_out(w, testing_data))

    SGD_Eout_20 = []
    for w in SGD_wlist_20:
        SGD_Eout_20.append(E_out(w, testing_data))
    
    plt.figure(2)
    plt.title('Eout')
    plt.xlabel('Iteration')
    plt.ylabel('Eout')
    plt.plot(range(T+1), GD_Eout_19, color='blue', label='Gradient descent')
    plt.plot(range(T+1), SGD_Eout_20, color='red', label='SGD')
    plt.legend(loc='upper right')
    
    plt.show()
    
