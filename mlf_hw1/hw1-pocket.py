# Environment: Python 3.7.0 

import re
import random
import matplotlib.pyplot as plt


def sign(number):
    
    if number > 0:
        return 1
    else:
        return -1

def data_collect(input):
    file = open(input, "r")

    res = []
    for i in file:
        # Split each line into numbers
        line = re.split(r"\s", i)

        # Set x0 = 1 and transform the data in list from string into float
        line.insert(0, "1")
        line = [float(num) for num in line[0:6]]

        res.append(line)

    return res

def check_error(w, x, num):

	error = 0

	for i in range(num):

		y = x[i][5]

		w_dot_x = 0
		for j in range(5):
			w_dot_x += w[j] * x[i][j]

		if sign(w_dot_x) != sign(y):
			error += 1

	error_rate = error / num
	return error_rate

def pocket_PLA(x):
    
    pocket = [0, 0, 0, 0, 0]
    w = [0, 0, 0, 0, 0]

 	# Generate pre-determined random sequence of data
    number_of_data = len(x)
    sequence_of_data = random.sample(range(number_of_data), number_of_data)
    
    pocket_error = check_error(pocket, x, number_of_data)
    visit = -1

    for t in range(50):

        if visit == number_of_data-1:
            visit = -1
        visit += 1

        current = sequence_of_data[visit]
        y = x[current][5]
        
        w_dot_x = 0
        for i in range(5):
            w_dot_x += w[i] * x[current][i]

        if sign(w_dot_x) != sign(y):
            for i in range(5):
                w[i] = w[i] + (y * x[current][i])

        w_error = check_error(w, x, number_of_data)
        
        if  w_error < pocket_error:
        	pocket_error = w_error
        	for i in range(5):
        		pocket[i] = w[i]

    return pocket

if __name__ == '__main__':

    train_data = data_collect("hw1_18_train.dat")
    test_data = data_collect("hw1_18_test.dat")

    total = 0
    for i in range(2000):
        pocket = pocket_PLA(train_data)

        total += check_error(pocket, test_data, len(test_data))
       
    print(total/2000)

