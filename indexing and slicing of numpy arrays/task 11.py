'''Problem 11: 3D Slicing – Blocks

Create a 3D array of shape (2×2×3) with values 1–12.

Output:

First block

Second block

Sample Output:

[[[1 2 3]
  [4 5 6]]]
[[[ 7  8  9]
  [10 11 12]]]'''

import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a[0:1])
print(a[1:2])
