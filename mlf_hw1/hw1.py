# Environment: Python 3.7.0 

import re
import random
import matplotlib.pyplot as plt

NUMBER_OF_UPDATE = []

def sign(number):
    
    if number > 0:
        return 1
    else:
        return -1

def data_collect():
    file = open("hw1_7_train.dat", "r")

    res = []
    for i in file:
        # Split each line into numbers
        line = re.split(r"\s", i)

        # Set x0 = 1 and transform the data in list from string into float
        line.insert(0, "1")
        line = [float(num) for num in line[0:6]]

        res.append(line)

    return res

def perceptron_learning_algo(x):
 
    w = [0, 0, 0, 0, 0]

    # Generate pre-determined random sequence of data
    number_of_data = len(x)
    sequence_of_data = random.sample(range(number_of_data), number_of_data)
    
    visit = -1
    finish = 0
    update = 0

    while True:

        if visit == number_of_data-1:
            visit = -1
        visit += 1

        current = sequence_of_data[visit]
        y = x[current][5]
        
        w_dot_x= 0
        for i in range(5):
            w_dot_x += w[i] * x[current][i]

        # If w is changed, set finish to 0
        # Otherwise, finish += 1
        if sign(w_dot_x) != sign(y):
            finish = 0
            update += 1

            for i in range(5):
                w[i] = w[i] + (y * x[current][i])

        else:
            finish += 1
        
        # Until w isn't changed for 400 times continuously, pla can halt
        if finish == number_of_data:
            break

    return update

if __name__ == '__main__':

    data = data_collect()

    total = 0.0
    for i in range(1126):
        res = perceptron_learning_algo(data)
        NUMBER_OF_UPDATE.append(res)
        total += res

    maximum = max(NUMBER_OF_UPDATE)

    print("Average number of updates = %f" % (total/1126))
    plt.hist(NUMBER_OF_UPDATE, maximum, color='r')
    plt.xlabel('Number of updates')
    plt.ylabel('Frequency of the number')
    plt.title('Average number of updates = %f' % (total/1126))
    plt.grid(axis='y')
    plt.show()
