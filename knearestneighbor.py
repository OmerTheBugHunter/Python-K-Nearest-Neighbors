# Setup the KNN and Accuracy algorithms.
import numpy as np
from collections import Counter

# K-Nearest Neighbors Algorithm
def knn(X_train_dataset, X_test_dataset, y_train_dataset, k): 
    def euc_dist(x1, x2):
        dist = np.sqrt((x1 - x2)**2)

        return dist
    
    predicts = []
    
    for i in range(0, len(X_test_dataset)):
        dists = []
        
        for j in range(0, len(X_train_dataset)):
            dist = 0
            value = 0
            
            for col in X_train_dataset.columns:
                value = euc_dist(X_test_dataset.iloc[i][col], X_train_dataset.iloc[j][col])
                dist += value

            dists.append((dist,y_train_dataset.iloc[j]['Class']))

        # We have a list which contains the distances of the i th data of the X_test_dataset. But these distances are not in an order.
        sorted_dists = sorted(dists, key=lambda x: x[0])

        # Pick first k element of the sorted distance list.
        k_dists = [(float(a), int(b)) for a, b in sorted_dists[:k]]

        # Each tuple contains a distance and a class metric in it. Count the number of each class.
        counter = Counter(b for _, b in k_dists)

        # Find the most repeated class.
        most_common_value, _ = counter.most_common(1)[0]

        predicts.append(most_common_value)
        
    return predicts

# Accuracy Calculator 
def accuracy(y_test, y_predict):
    counter = 0
    
    for i in range(0, len(y_test)):
        if y_test[i] == y_predict[i]:
            counter += 1

    score = (counter / len(y_test)) * 100

    return score
