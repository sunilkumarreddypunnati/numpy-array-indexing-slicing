'''Problem 8: 2D Slicing – Columns

Using the same 3×3 array:

Output:

First two columns

Last column only

Sample Output:

[[1 2]
 [4 5]
 [7 8]]
[3 6 9]'''

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a[:,0:2])

print(a[:,2])
