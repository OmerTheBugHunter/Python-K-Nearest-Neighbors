# KNN ve Accuracy Hesaplayıcı algoritmalarımızı kuralım.
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
            
            for col in feature_columns:
                value = euc_dist(X_test_dataset.iloc[i][col], X_train_dataset.iloc[j][col])
                dist += value

            dists.append((dist,y_train_dataset.iloc[j]['Class']))

        # Fonksiyonun bu bölümünde elimizde 142 elemanlı bir dists listesi mevcut.
        # Elimizdeki liste X_test_dataset'inin i.datasına ait mesafe ölçümleridir. Ancak mesafeler sıralanmamış durumdadır. Sıralayalım.
        sorted_dists = sorted(dists, key=lambda x: x[0])

        # Şimdi küçükten büyüğe sıralanmış listemizdeki ilk k elemanı alalım.
        k_dists = [(float(a), int(b)) for a, b in sorted_dists[:k]]

        # Elimizde k elemanlı bir tuple listesi mevcut. 
        # Her bir tuple'ın ilk elemanı mesafeyi, ikinci eleman da bu mesafe uzaklıktaki noktanın ait olduğu class'ı gösteriyor.
        counter = Counter(b for _, b in k_dists)

        # En çok tekrar eden değeri bulalım.
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