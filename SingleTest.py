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
		print("--AveragedCrossSpec: __init__ SingleTest--")
		dt = 0.03125

		lc_size = base * (10 ** power)

		final_element = dt * lc_size
		# print("final element:", final_element)
		# print("lc calculated size:", lc_size)

		times1 = np.arange(0,final_element,dt)
		counts1 = np.random.rand(lc_size) * 100

		# times2 = np.arange(final_element, 2*final_element+dt, dt)
		counts2 = np.random.rand(lc_size) * 100


		lc1 = Lightcurve(times1, counts1)
		lc2 = Lightcurve(times1, counts2)

		# print("lc actual size:", len(lc1))

		# segment_size = ceil( lc_size * 0.0002 )
		segment_size = 1
		print("Segment size:", segment_size)
		t0 = time.time()
		av_cs = AveragedCrossspectrum(lc1,lc2, segment_size)
		t1 = time.time()
		print(t1 - t0)
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

	# time.sleep(4)
	# sys.exit()



