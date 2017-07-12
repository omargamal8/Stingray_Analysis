from stingray import Lightcurve
import numpy as np
import time
import sys

def calculate_size(number):
	whole = int(number)
	fraction = number%whole


	return int((10 ** whole) * (fraction* 10))




def singleTest(base,power):
	print("--Shift SingleTest--")
	dt = 0.03125
	lc_size = base * (10 ** power)
	final_element = dt * lc_size
	times = np.arange(0,final_element,dt)
	counts = np.random.rand(lc_size) * 100
	lc1 = Lightcurve(times,counts)


	t0 = time.time()
	lc1 = lc1.shift(1.1)
	t1 = time.time()
	
	return t1-t0
# size of the lightcurve to be tested with is equal to |base * 10^pow|

if __name__ == '__main__':
	base = 1
	power = 7      

	test_options = sys.argv
	if(len(test_options) > 1):
		base = int(test_options[1])
		power = int(test_options[2])

	lc_size = base * (10 **power)
	# print(lc_size)

	dt = 0.03125
	final_element = dt * lc_size

	times = np.arange(0, final_element, dt)
	# print("testing size", len(times))

	counts = np.random.rand(lc_size)*100
	# print(len(counts))


	#Lightcurve initialization
	lc1 = Lightcurve(times, counts)	
	print("LightCurve Created")
	# time.sleep(5)
	t0 = time.time()

	lc1 = lc1.shift(1.1)

	t1 = time.time()

	print(t1 - t0)

	if(len(test_options)>3):
			f = open("./TimeProfiles/Snaps_Results.txt", "a")
			strtobewritten = "ten pw " + str(power) + ": " + str(t1-t0)+"\n"
			f.write(strtobewritten)
			f.close()
	# print("Lightcurve initialization took:", t1-t0)

	# time.sleep(4)
	# sys.exit()



