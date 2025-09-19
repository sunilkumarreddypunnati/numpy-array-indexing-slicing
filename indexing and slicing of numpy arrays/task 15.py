'''Problem 15: Advanced 3D Mixed

Create a 3D array of shape (3×3×3) with values 1–27.

Output:

Middle block

First row of the last block

All elements greater than 20

Sample Output:

[[[10 11 12]
  [13 14 15]
  [16 17 18]]]
[[25 26 27]]
[21 22 23 24 25 26 27]'''

import numpy as np
a=np.arange(1,28)
b=a.reshape(3,3,3)
print(b[1:2])
print(b[-1,2:3,:])
print(b[b>20])