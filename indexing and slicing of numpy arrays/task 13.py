'''Problem 13: Mixed Indexing + Slicing

Given:

[[10,20,30,40],
 [50,60,70,80],
 [90,100,110,120]]


Output:

Element at Row 3, Col 2

First two rows & first two columns

Sample Output:

100
[[10 20]
 [50 60]]'''

import numpy as np
a=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(a[2,1])
print(a[0:2,0:2])
