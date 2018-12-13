import random
import numpy as np
import matplotlib.pyplot as plt

DATA_SIZE = 20
S = [-1, 1]

def sign(num):
    if num < 0:
        return -1
    else:
        return 1 

def data_generate():
    data = np.zeros((DATA_SIZE, 2))
    for i in range(DATA_SIZE):
        data[i][0] = random.uniform(-1, 1)
        if random.uniform(0, 1) <= 0.2:
            data[i][1] = -sign(data[i][0])
        else:
            data[i][1] = sign(data[i][0])    
    
    return data

def E_in_and_E_out(data):
    # sort data by column 0
    data = data[np.argsort(data[:, 0])] # data[:,0] -- get entire column of index 0
    min_e_in = 1.0
    h = {"s": 0, "theta": 0}

    for s in S:
        for i in range(DATA_SIZE + 1):
            if i == 0:
                theta = -1.0
            elif i == DATA_SIZE:
                theta = 1.0
            else:
                theta = (data[i][0] + data[i-1][0]) / 2
            
            error = 0
            for j in range(DATA_SIZE):
                value = s * sign(data[j][0] - theta)
                if value != data[j][1]:
                    error += 1
            
            if min_e_in > (error / DATA_SIZE):
                min_e_in = error / DATA_SIZE
                h["s"] = s
                h["theta"] = theta
                
    e_out = 0.5 + 0.3 * h["s"] * (abs(h["theta"]) - 1)

    return min_e_in, e_out

if __name__ == "__main__":

    total = np.zeros((5000, 2))

    for i in range(5000):
        data = data_generate()
        total[i][0], total[i][1] = E_in_and_E_out(data)
    
    avg_e_in = sum(total[:, 0]) / 5000
    avg_e_out = sum(total[:, 1]) / 5000

    print("Average_e_in = %lf" % avg_e_in)
    print("Average_e_out = %lf" % avg_e_out)
    