from stingray import Lightcurve, AveragedPowerspectrum, Powerspectrum
import numpy as np
import time as btime

def test_leahy_correct_for_multiple():

        n = 100
        lc_all = []
        t1 = btime.time()
        gcounts = np.random.poisson(1000, size=100000)

        for i in range(n):
            time = np.arange(0.0, 10.0, 10./100000)
            counts = gcounts[:]
            lc = Lightcurve(time, counts)
            lc_all.append(lc)
        t2 = btime.time()

        ps = AveragedPowerspectrum(lc_all, 10.0, norm="leahy")


        assert np.isclose(np.mean(ps.power), 2.0, atol=1e-3, rtol=1e-3)
        assert np.isclose(np.std(ps.power), 2.0/np.sqrt(n), atol=0.1, rtol=0.1)
        print(t2-t1)
# times = np.arange(0,2,0.5)
# counts = np.random.rand(len(times))*100
# lc1 = Lightcurve(times,counts)
# pc = 
test_leahy_correct_for_multiple()