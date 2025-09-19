'''Problem 14: Boolean + Slicing

Given array:

[5, 10, 15, 20, 25, 30, 35, 40]


Output:

All elements greater than 20

Even numbers only

Last 3 elements using slicing

Sample Output:

[25 30 35 40]
[10 20 30 40]
[30 35 40]'''

import numpy as np
a=np.array([5, 10, 15, 20, 25, 30, 35, 40])
print(a[a>20])
print(a[a%2==0])
print(a[-3::])