# Python-K-Nearest-Neighbors
This repository includes the codes to implement the "K-Nearest Neighbors Algorithm" without scikit-learn package.

K-Nearest-Neighbors Algorithm:
1) Picks one point from the test dataset. (Output of that point does not known.)
2) Using that point; for each point at the train dataset, calculates the total distance of all features.
3) Creates a list containing that distance values and sorts it.
4) Holds the first k point and eliminates the rest.
5) Counts the numbers of outputs of these points.
6) Returns the highest numbered output as prediction.
7) Applies the same procedure to the other points at the test dataset.

Accuracy:
Counts the number of true predictions and finds the percentage.
