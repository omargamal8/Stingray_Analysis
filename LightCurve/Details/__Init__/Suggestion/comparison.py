import numpy as np 
import time

arr1 = np.arange(10 ** 8)
arr2 = np.arange(10 ** 8)

time.sleep(2)

#allclose
t0 = time.time()
np.allclose(arr1,arr2)
t1 = time.time()

print(t1-t0)
time.sleep(2)

#.all
t0 = time.time()
np.all(np.absolute(arr1-arr2) > 0 )
t1 = time.time()

print(t1-t0)
time.sleep(3)