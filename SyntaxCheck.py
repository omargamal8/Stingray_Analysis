import stingray_parallel
import numpy as np
import time
def summation(arr):
	sum = 0
	for number in arr:
		sum+= number
	return sum

def avg(arr):
	return summation(arr)/len(arr)

def sum_avg(arr):
	sum 	= summation(arr)
	av 	= avg(arr)
	return sum, av
# arr = np.arange(3 * 10**8)
arr = np.arange(9)
t0 = time.time()
# print(stingray_parallel.execute_parallel(summation, [], arr))
print(stingray_parallel.execute_parallel(sum_avg, [summation, avg], arr))
t1 = time.time()

print("Dask:", t1-t0)

t0 = time.time()
print(summation(arr))
print(avg(arr))
t1 = time.time()

print("Raw:", t1 - t0)