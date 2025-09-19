'''Problem 9: Sub-matrix Extraction

From the 3×3 matrix:

Output:

Top-left 2×2 block

Bottom-right 2×2 block

Sample Output:

[[1 2]
 [4 5]]
[[5 6]
 [8 9]]'''

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0:2,0:2])
print(a[1:3,1:3])