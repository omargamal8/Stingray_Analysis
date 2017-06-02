from stingray import Lightcurve
import numpy as np
import time

# size of the lightcurve to be tested with 10^test_pow
test_pow = 7        


lc_size = pow(10, test_pow - 5)
dt = 0.03125
exposure = 3125 * lc_size

times = np.arange(0, exposure, dt)
print("testing size", len(times))
signal_1 = 300 * np.sin(2.*np.pi*times/0.5) + 1000 
noisy_1 = np.random.poisson(signal_1*dt)  


#Lightcurve initialization
t0 = time.time()

lc1 = Lightcurve(times, noisy_1)

t1 = time.time()
print("Lightcurve initialization took:", t1-t0)
