'''Problem 12: 3D Slicing – Rows & Columns

Using the same array:

Output:

First row of each block

Last column of each block

Sample Output:

[[[1 2 3]]
 [[7 8 9]]]
[[3 6]
 [9 12]]'''

import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a[:,0:1,:])
print(a[:,:,-1])



