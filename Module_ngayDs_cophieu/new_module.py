#reference based on "python for finace"
import numpy as np
import matplotlib.pyplot as plt

class porfolio:
    #mean là list các return trung bình của asset
    def __init__(self, n, mean, cov):
        self.n = n
        self.mean = mean  
        self.cov = cov

    def mean_return(self):
        mean = np.array(self.mean)
        cov = np.array(self.cov)
        mean_exp = []
        stdev_exp = []
        for p in range (1500):
            weights = np.random.random(self.n)
            weights /= np.sum(weights)
            mean_exp.append(np.dot(mean ,weights.T)*252)
            stdev_exp.append(np.sqrt(np.dot(weights,np.dot(cov, weights.T)))*np.sqrt(252))
        return np.array(stdev_exp), np.array(mean_exp)
    

