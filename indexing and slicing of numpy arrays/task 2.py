'''Problem 2: 2D Array Indexing

Create a 3×3 NumPy array with values from 1 to 9.

Input: None
Output:

Element at Row 2, Col 3

Element at Row 1, Col 1 (using negative indexing)

Sample Output:

6
1'''

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1,2])
print(arr[-3,-3])