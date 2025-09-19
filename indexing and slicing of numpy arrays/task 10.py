'''Problem 10: Negative Slicing in 2D

Using the 3×3 matrix:

Output:

Reverse all rows

Reverse all columns

Sample Output:

[[7 8 9]
 [4 5 6]
 [1 2 3]]
[[3 2 1]
 [6 5 4]
 [9 8 7]]
'''

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[::-1,:])
print(a[:,::-1])
   