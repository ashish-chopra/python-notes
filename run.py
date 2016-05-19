    
# Testing the neighbors algorithm

#dataset = np.array([[1,2,3],[1,4,6],[2,3,4],[1,2,4]])
#labels = np.array([0,0,1,0])
#inputX = np.array([1,2,3])
#print(kNearestNeighbor(3, dataset, labels, inputX))

from sklearn import datasets

data = datasets.load_iris()

import neighbors
import numpy as np

print(neighbors.kNearestNeighbor(5, data.data, data.target, np.array([4.3,6.5,1.4,0.9])))