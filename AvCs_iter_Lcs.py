from stingray import Lightcurve, AveragedCrossspectrum
import numpy as np
from time import time as ttime
class test:
    def __init__(self):
        # self.time = np.arange(1,17)
        # self.counts = np.arange(10,170,10)

        # self.counts2 = np.arange(0.1, 1.7, 0.1)

        self.time = np.arange(10 ** 6)
        self.counts = np.arange(10 ** 6)
        self.counts2 = np.arange(10**6, 2*10**6)
        print(len(self.time),len(self.counts2),len(self.counts))
        self.lc1 = Lightcurve(self.time, self.counts)
        self.lc2 = Lightcurve(self.time, self.counts2)

    def test_with_iterable_of_lightcurves(self):
        def iter_lc(lc, n):
            "Generator of n parts of lc."
            t0 = int(len(lc) / n)
            t = t0
            i = 0
            while(True):
                lc_seg = lc[i:t]
                yield lc_seg
                if t + t0 > len(lc):
                    break
                else:
                    i, t = t, t + t0
        t0 = ttime()
        cs = AveragedCrossspectrum(iter_lc(self.lc1, 1), iter_lc(self.lc2, 1),
                                   segment_size=2000)
        print(ttime()-t0)

test1 = test()
test1.test_with_iterable_of_lightcurves()
