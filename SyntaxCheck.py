import stingray.parallel
import numpy as np
import time

def summation(arr):
	sum = 0
	for number in arr:
		sum+= number
	for number in arr:
		sum+= number
	for number in arr:
		sum+= number
	return sum

def avg(arr):
	return summation(arr)/len(arr)

def sum_avg(arr, que = None):
	sum 	= summation(arr)
	av 	= avg(arr)
	if(que != None):
		que.put([sum,av])
	return sum, av

arr = np.arange(10 ** 8)

t0 = time.time()
print(stingray.parallel.execute_parallel(sum_avg, [summation, avg], arr))
t1 = time.time()

print("Dask:", t1-t0)

t0 = time.time()
# print(summation(arr))
# print(avg(arr))
sum_avg(arr)
t1 = time.time()

print("Raw:", t1 - t0)