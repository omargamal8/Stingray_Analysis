from stingray import Lightcurve, AveragedCrossspectrum
import numpy as np
import time
from math import ceil





def singleTest():

		print("--AveragedCrossSpec: __init__ SingleTest--")

		# times = np.arange(1,17)
		# counts = np.arange(10,170,10)

		# counts2 = np.arange(0.1, 1.7, 0.1)

		times = np.arange(10 ** 6)
		counts = np.arange(10 ** 6)
		counts2 = np.arange(10 ** 6)
		lc1 = Lightcurve(times, counts)
		lc2 = Lightcurve(times, counts2)



		# segment_size = ceil( lc_size * 0.0002 )
		segment_size = 100
		print("Segment size:", segment_size)
		t0 = time.time()
		av_cs = AveragedCrossspectrum(lc1,lc2, segment_size)
		# av_cs.coherence()
		t1 = time.time()
		print(t1 - t0)
		return t1-t0




if __name__ == '__main__':
	result = singleTest()





