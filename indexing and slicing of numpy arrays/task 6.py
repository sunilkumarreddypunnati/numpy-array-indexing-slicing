'''Problem 6: 1D Array Slicing

Create an array with values [10, 20, 30, 40, 50, 60].

Output:

Elements from index 1 to 3

Every 2nd element

Array in reverse order

Sample Output:

[20 30 40]
[10 30 50]
[60 50 40 30 20 10]'''

import numpy as np
arr=np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])
print(arr[::2])
print(arr[::-1])