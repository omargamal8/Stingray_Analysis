import numpy as np
import time
import sys

#@profiler
def test():
	test_arg = sys.argv
	base = int(test_arg[1])
	power = int(test_arg[2])

	arr1 = np.arange(0, base *(10 ** power))


	t0 = time.time()
	arr2 = np.arange(0, len(arr1))
	np.allclose(arr1,arr2)
	t1 = time.time()
	print(t1-t0)


	np.array_equal(arr1,arr2)

test()