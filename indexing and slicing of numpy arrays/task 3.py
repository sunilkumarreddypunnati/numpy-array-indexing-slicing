'''Problem 3: 3D Array Indexing

Create a 3D array of shape (2×2×3) with values 1 to 12.

Input: None
Output:

Element at Block 2, Row 1, Col 3

Last element (using negative indexing)

Sample Output:

9
12'''

import numpy as np
a=np.arange(1,13)
arr=a.reshape(2,2,3)
print(arr)
print(arr[1,0,2])
print(arr[-1,-1,-1])