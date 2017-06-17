import numpy as np
import time

@profiler
def test():
	arr1 = np.arange(0, 10 **8)


	t0 = time.time()
	arr2 = np.arange(0, 10 ** 8)
	np.allclose(arr1,arr2)
	t1 = time.time()
	print(t1-t0)


	np.array_equal(arr1,arr2)

test()