'''Problem 5: Boolean Indexing (1D)

Given an array:

[10, 21, 32, 43, 54, 65]


Output:

All elements greater than 30

All even numbers

Sample Output:

[32 43 54 65]
[10 32 54]
'''

import numpy as np
arr=np.array([10, 21, 32, 43, 54, 65])
print(arr[arr>30])
print(arr[arr%2==0])