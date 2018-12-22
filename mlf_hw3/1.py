
if __name__ == "__main__":
    sigma = 0.1
    d = 8
    
    N = [10, 25, 100, 500, 1000]
    for n in N:
        print(n, pow(sigma, 2) * (1 - (d+1) / n))
    
