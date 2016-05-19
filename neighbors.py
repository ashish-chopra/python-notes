"""
    File: neighbors.py
    Date: 18 may, 2016
    Author: Ashish Chopra
    
    
    neighbors.py is an implementation of K-nearest neighbor algorithm.
    It performs supervised learning on the given dataset and label an 
    unseen data point.
    
    k--value of parameter 'k' of KNN definition.
    dataset--(n x c) numpy array of training data consists of 
              'n' training samples of 'c' features.
    labels-- (n x 1) vector of labels for each training sample.
    inputX-- (1 x c) an unseen sample to be classified.
    
"""

import numpy as np
import operator

def kNearestNeighbor(k, dataset, labels, inputX):
    """
        checks the pre-condition of the arguments
        identify n_samples, n_classes, n_features in the input
        compute euclidean distance of the dataset from inputX
        pick top 'k' and identify the most frequent class in it.
    """
    # checks to see if the dataset and labels are of same dimensions to operate 
    
    n_samples, n_features = dataset.shape
    n_classes = np.unique(labels).shape[0]
    
    if (n_features != inputX.shape[0]):
        return "Error, dimensions mismatch for training samples, labels, inputX"
    
    dist_vector = compute_euclidean_distance(dataset, inputX)
    temp_list = dist_vector.argsort()
    
    class_votes = {}
    for i in temp_list[:k]:
        key = labels[i]
        if key in class_votes:
            class_votes[key] = class_votes[key] + 1
        else:
            class_votes[key] = 1
    predicted_class = max(class_votes.items(), key=operator.itemgetter(1))
    return predicted_class[0]


def compute_euclidean_distance(dataset, inputX):
    n_size = dataset.shape[0]
    mat = np.tile(inputX, (n_size, 1)) - dataset
    mat = np.square(mat)
    vec = np.sum(mat, axis=1)
    vec = np.sqrt(vec)
    return vec