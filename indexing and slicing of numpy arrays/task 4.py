'''Problem 4: Fancy Indexing (1D)

Given an array:

[5, 10, 15, 20, 25, 30]


Extract elements at indices [0, 2, 4] and [1, 3, 5].

Sample Output:

[ 5 15 25]
[10 20 30]
'''
import numpy as np
arr=np.array([5,10,15,20,25,30])
print(arr[[0,2,4]])
print(arr[[1,3,5]])