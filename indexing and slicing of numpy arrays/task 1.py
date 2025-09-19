'''Problem 1: 1D Array Indexing

Create a 1D NumPy array with numbers from 10 to 100 with step 10.

Input: None (array created inside program)
Output:
First element
Third element
Last element (using negative indexing)

Sample Output:

10
30
100'''

import numpy as np
arr=np.arange(10,110,10)
print("full array:\n",arr)
print("first element:",arr[0])
print("third element:",arr[2])
print("last element:",arr[-1])
