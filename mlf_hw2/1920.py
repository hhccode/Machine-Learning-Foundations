import numpy as np

S = [-1, 1]

def sign(num):
    if num < 0:
        return -1
    else:
        return 1 

def data_collect(path):
    file = open(path, "r")
    count = 0

    for i in file:
        count += 1
        line = i.split()
        line = [float(num) for num in line]

        if count == 1:
            data = np.array(line)
        else:
            data = np.vstack((data, line))

    return data, count

def train(data, N):
    dimension = data.shape[1]
    e_ins = []
    hs = []

    for d in range(dimension - 1):
        data = data[np.argsort(data[:, d])]
        e_in = 1.0
        h = {"s": 0, "theta": 0}

        for s in S:
            for i in range(N + 1):
                if i == 0:
                    theta = data[i][d] - 1.0
                elif i == N:
                    theta = data[i-1][d] + 1.0
                else:
                    theta = (data[i][d] + data[i-1][d]) / 2

                error = 0
                for j in range(N):
                    value = s * sign(data[j][d] - theta)
                    if value != data[j][dimension-1]:
                        error += 1
                        
                if e_in > (error / N):
                    e_in = error / N
                    h["s"] = s
                    h["theta"] = theta

        e_ins.append(e_in)
        hs.append(h)

    print("E_in = %lf" % min(e_ins))
    hypo= hs[e_ins.index(min(e_ins))]
    
    return hypo

def test(hypo):
    data, N = data_collect("hw2_test.dat")

    dimension = data.shape[1]
    e_out = []

    for d in range(dimension - 1):
        data = data[np.argsort(data[:, d])]
        error = 0
        for i in range(N):
            value = hypo["s"] * sign(data[i][d] - hypo["theta"])
            if value != data[i][dimension-1]:
                error += 1
        
        e_out.append(error / N)

    print("E_out = %lf" % min(e_out))  

    return

if __name__ == "__main__":

    data, data_size = data_collect("hw2_train.dat")
    hypothese = train(data, data_size)
    test(hypothese)
