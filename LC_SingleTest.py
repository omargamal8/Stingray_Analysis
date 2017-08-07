from stingray import Lightcurve, AveragedCrossspectrum
import numpy as np
import time
import sys
from math import ceil

def calculate_size(number):
	whole = int(number)
	fraction = number%whole


	return int((10 ** whole) * (fraction* 10))




def singleTest(base,power):
	# try:
		print("--Lightcurve: __init__ SingleTest--")
		dt = 0.03125

		lc_size = base * (10 ** power)


		final_element = dt * lc_size

		times1 = np.arange(0,final_element,dt)
		counts1 = np.random.rand(lc_size) * 100

		times2 = np.arange(final_element, 2*final_element, dt)
		counts2 = np.random.rand(lc_size) * 100



		# times1 = np.arange(1,17)
		# counts1 = np.arange(1,17)
		# print(times1)
		# print(counts1)

        #
		# times2 = np.arange(8,24)
		# counts2 = np.concatenate([np.arange(12,21), np.arange(17,24)])
		# print(times2)
		# print(counts2)

		t0 = time.time()
		lc1 = Lightcurve(times1, counts1)
		t1 = time.time()
		lc2 = Lightcurve(times2, counts2)
		print("LightCurve took:",t1-t0)


		t0 = time.time()
		lc3 = lc1.join(lc2)
		t1 = time.time()
		# print(t1 - t0)
		# print(lc3.time[0], lc3.counts[0])
		# print(lc3.time)
		# print(lc3.counts)
		# print(len(lc3.counts))
		return t1-t0
	# except Exception as e:
		# print("exception:", e)

# size of the lightcurve to be tested with is equal to |base * 10^pow|



if __name__ == '__main__':
	base = 1
	power = 7      

	test_options = sys.argv
	if(len(test_options) > 1):
		base = int(test_options[1])
		power = int(test_options[2])
	else:
		base = int(input("Base:"))
		power = int(input("Power:"))

	result = singleTest(base, power)

	# print("Lightcurve initialization took:", t1-t0)

	print(result)
	# time.sleep(4)
	# sys.exit()



