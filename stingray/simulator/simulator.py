<<<<<<< HEAD

=======
from __future__ import division, print_function, absolute_import
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
import numpy as np
import numbers
from scipy import signal
import astropy.modeling.models

from stingray import Lightcurve, AveragedPowerspectrum, io, utils
import stingray.simulator.models as models

<<<<<<< HEAD
=======

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
class Simulator(object):

    def __init__(self, dt=1, N=1024, mean=0, rms=1, red_noise=1,
                 random_state=None):
        """
        Methods to simulate and visualize light curves.

        Parameters
        ----------
<<<<<<< HEAD
        dt: int, default 1
            time resolution of simulated light curve
        N: int, default 1024
            bins count of simulated light curve
        mean: float, default 0
            mean value of the simulated light curve
        rms: float, default 1
            fractional rms of the simulated light curve,
            actual rms is calculated by mean*rms
        red_noise: int, default 1
            multiple of real length of light curve, by
            which to simulate, to avoid red noise leakage
        seed: int, default None
=======
        dt : int, default 1
            time resolution of simulated light curve
        N : int, default 1024
            bins count of simulated light curve
        mean : float, default 0
            mean value of the simulated light curve
        rms : float, default 1
            fractional rms of the simulated light curve,
            actual rms is calculated by mean*rms
        red_noise : int, default 1
            multiple of real length of light curve, by
            which to simulate, to avoid red noise leakage
        seed : int, default None
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            seed value for random processes
        """

        self.dt = dt
        self.N = N
        self.mean = mean
        self.rms = rms
        self.red_noise = red_noise
        self.time = dt*np.arange(N)

        # Initialize a tuple of energy ranges with corresponding light curves
        self.channels = []

        self.random_state = utils.get_random_state(random_state)

        assert rms<=1, 'Fractional rms must be less than 1.'
        assert dt>0, 'Time resolution must be greater than 0'

    def simulate(self, *args):
        """
        Simulate light curve generation using power spectrum or
        impulse response.

        Examples
        --------
        - x = simulate(beta)
            For generating a light curve using power law spectrum.

            Parameters
            ----------
<<<<<<< HEAD
            beta: int
                Defines the shape of spectrum

            Returns
            -------
            lightCurve: `LightCurve` object

=======
            beta : float
                Defines the shape of spectrum

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        - x = simulate(s)
            For generating a light curve from user-provided spectrum.

            Parameters
            ----------
<<<<<<< HEAD
            s: array-like
                power spectrum

            Returns
            -------
            lightCurve: `LightCurve` object

=======
            s : array-like
                power spectrum

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        - x = simulate(model)
            For generating a light curve from pre-defined model

            Parameters
            ----------
<<<<<<< HEAD
            model: astropy.modeling.Model
                the pre-defined model

            Returns
            -------
            lightCurve: `LightCurve` object

=======
            model : astropy.modeling.Model
                the pre-defined model

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        - x = simulate('model', params)
            For generating a light curve from pre-defined model

            Parameters
            ----------
<<<<<<< HEAD
            model: string
                the pre-defined model
            params: list iterable or dict
                the parameters for the pre-defined model

            Returns
            -------
            lightCurve: `LightCurve` object

=======
            model : string
                the pre-defined model
            params : list iterable or dict
                the parameters for the pre-defined model

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        - x = simulate(s, h)
            For generating a light curve using impulse response.

            Parameters
            ----------
<<<<<<< HEAD
            s: array-like
                Underlying variability signal
            h: array-like
                Impulse response

            Returns
            -------
            lightCurve: `LightCurve` object

=======
            s : array-like
                Underlying variability signal
            h : array-like
                Impulse response

>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        - x = simulate(s, h, 'same')
            For generating a light curve of same length as input
            signal, using impulse response.

            Parameters
            ----------
<<<<<<< HEAD
            s: array-like
                Underlying variability signal
            h: array-like
                Impulse response
            mode: str
=======
            s : array-like
                Underlying variability signal
            h : array-like
                Impulse response
            mode : str
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
                mode can be 'same', 'filtered, or 'full'.
                'same' indicates that the length of output light
                curve is same as that of input signal.
                'filtered' means that length of output light curve
                is len(s) - lag_delay
                'full' indicates that the length of output light
                curve is len(s) + len(h) -1

<<<<<<< HEAD
        Returns
            -------
            lightCurve: `LightCurve` object
        """

        if isinstance(args[0], numbers.Integral) and len(args) == 1:
=======
        Parameters
        ----------
        args
            See examples below.

        Returns
        -------
        lightCurve : `LightCurve` object

        """

        if isinstance(args[0], (numbers.Integral, float)) and len(args) == 1:
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            return  self._simulate_power_law(args[0])

        elif isinstance(args[0], astropy.modeling.Model) and len(args) == 1:
            return self._simulate_model(args[0])

        elif utils.is_string(args[0]) and len(args) == 2:
            return self._simulate_model_string(args[0], args[1])

        elif len(args) == 1:
            return self._simulate_power_spectrum(args[0])

        elif len(args) == 2:
            return self._simulate_impulse_response(args[0], args[1])

        elif len(args) == 3:
            return self._simulate_impulse_response(args[0], args[1], args[2])

        else:
            raise ValueError("Length of arguments must be 1, 2 or 3.")


    def simulate_channel(self, channel, *args):
        """
        Simulate a lightcurve and add it to corresponding energy
        channel.

        Parameters
        ----------
<<<<<<< HEAD
        channel: str
            range of energy channel (e.g., 3.5-4.5)

        *args:
=======
        channel : str
            range of energy channel (e.g., 3.5-4.5)

        *args
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            see description of simulate() for details

        Returns
        -------
<<<<<<< HEAD
            lightCurve: `LightCurve` object
=======
            lightCurve : `LightCurve` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        # Check that channel name does not already exist.
        if channel not in [lc[0] for lc in self.channels]:
            self.channels.append((channel, self.simulate(*args)))

        else:
            raise KeyError('A channel with this name already exists.')

    def get_channel(self, channel):
        """
        Get lightcurve belonging to the energy channel.
        """

        return [lc[1] for lc in self.channels if lc[0] == channel][0]

    def get_channels(self, channels):
        """
        Get multiple light curves belonging to the energy channels.
        """

        return [lc[1] for lc in self.channels if lc[0] in channels]

    def get_all_channels(self):
        """
        Get lightcurves belonging to all channels.
        """

        return [lc[1] for lc in self.channels]

    def delete_channel(self, channel):
        """
        Delete an energy channel.
        """

        channel = [lc for lc in self.channels if lc[0] == channel]

        if len(channel) == 0:
<<<<<<< HEAD
            raise KeyError('This channel does not exist or has already been deleted.')
=======
            raise KeyError('This channel does not exist or has already been '
                           'deleted.')
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        else:
            index = self.channels.index(channel[0])
            del self.channels[index]

    def delete_channels(self, channels):
        """
        Delete multiple energy channels.
        """
        n = len(channels)
        channels = [lc for lc in self.channels if lc[0] in channels]

        if len(channels) != n:
<<<<<<< HEAD
            raise KeyError('One of more of the channels do not exist or have already been'
                'deleted.')
=======
            raise KeyError('One of more of the channels do not exist or have '
                           'already been deleted.')
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        else:
            indices = [self.channels.index(channel) for channel in channels]
            for i in sorted(indices, reverse=True):
                del self.channels[i]

    def count_channels(self):
        """
        Return total number of energy channels.
        """

        return len(self.channels)

    def simple_ir(self, start=0, width=1000, intensity=1):
        """
        Construct a simple impulse response using start time,
        width and scaling intensity.
        To create a delta impulse response, set width to 1.

        Parameters
        ----------
<<<<<<< HEAD
        start: int
            start time of impulse response
        width: int
            width of impulse response
        intensity: float
=======
        start : int
            start time of impulse response
        width : int
            width of impulse response
        intensity : float
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            scaling parameter to set the intensity of delayed emission
            corresponding to direct emission.

        Returns
        -------
<<<<<<< HEAD
        h: numpy.ndarray
=======
        h : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Constructed impulse response
        """

        # Fill in 0 entries until the start time
        h_zeros = np.zeros(int(start/self.dt))

        # Define constant impulse response
        h_ones = np.ones(int(width/self.dt)) * intensity

        return np.append(h_zeros, h_ones)

<<<<<<< HEAD
    def relativistic_ir(self, t1=3, t2=4, t3=10, p1=1, p2=1.4, rise=0.6, decay=0.1):
=======
    def relativistic_ir(self, t1=3, t2=4, t3=10, p1=1, p2=1.4, rise=0.6,
                        decay=0.1):
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """
        Construct a realistic impulse response considering the relativistic
        effects.

        Parameters
        ----------
<<<<<<< HEAD
        t1: int
            primary peak time
        t2: int
            secondary peak time
        t3: int
            end time
        p1: float
            value of primary peak
        p2: float
            value of secondary peak
        rise: float
            slope of rising exponential from primary peak to secondary peak
        decay: float
=======
        t1 : int
            primary peak time
        t2 : int
            secondary peak time
        t3 : int
            end time
        p1 : float
            value of primary peak
        p2 : float
            value of secondary peak
        rise : float
            slope of rising exponential from primary peak to secondary peak
        decay : float
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            slope of decaying exponential from secondary peak to end time

        Returns
        -------
<<<<<<< HEAD
        h: numpy.ndarray
=======
        h : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Constructed impulse response
        """

        dt = self.dt

        assert t2>t1, 'Secondary peak must be after primary peak.'
        assert t3>t2, 'End time must be after secondary peak.'
        assert p2>p1, 'Secondary peak must be greater than primary peak.'

        # Append zeros before start time
        h_primary = np.append(np.zeros(int(t1/dt)), p1)

        # Create a rising exponential of user-provided slope
        x = np.linspace(t1/dt, t2/dt, (t2-t1)/dt)
        h_rise = np.exp(rise*x)

        # Evaluate a factor for scaling exponential
        factor = np.max(h_rise)/(p2-p1)
        h_secondary = (h_rise/factor) + p1

        # Create a decaying exponential until the end time
        x = np.linspace(t2/dt, t3/dt, (t3-t2)/dt)
        h_decay = (np.exp((-decay)*(x-4/dt)))

        # Add the three responses
        h = np.append(h_primary, h_secondary)
        h = np.append(h, h_decay)

        return h

    def _simulate_power_law(self, B):
        """
        Generate LightCurve from a power law spectrum.

        Parameters
        ----------
<<<<<<< HEAD
        B: int
=======
        B : int
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Defines the shape of power law spectrum.

        Returns
        -------
<<<<<<< HEAD
        lightCurve: array-like
=======
        lightCurve : array-like
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        # Define frequencies at which to compute PSD
        w = np.fft.rfftfreq(self.red_noise*self.N, d=self.dt)[1:]

        # Draw two set of 'N' guassian distributed numbers
        a1 = self.random_state.normal(size=len(w))
        a2 = self.random_state.normal(size=len(w))

        # Multiply by (1/w)^B to get real and imaginary parts
        real = a1 * np.power((1/w),B/2)
        imaginary = a2 * np.power((1/w),B/2)

        # Obtain time series
        long_lc = self._find_inverse(real, imaginary)
        lc = Lightcurve(self.time, self._extract_and_scale(long_lc),
                        err_dist='gauss', dt=self.dt)

        return lc

    def _simulate_power_spectrum(self, s):
        """
        Generate a light curve from user-provided spectrum.

        Parameters
        ----------
<<<<<<< HEAD
        s: array-like
=======
        s : array-like
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            power spectrum

        Returns
        -------
<<<<<<< HEAD
        lightCurve: `LightCurve` object
=======
        lightCurve : `LightCurve` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        # Cast spectrum as numpy array
        s = np.array(s)

        self.red_noise = 1

        # Draw two set of 'N' guassian distributed numbers
        a1 = self.random_state.normal(size=len(s))
        a2 = self.random_state.normal(size=len(s))

        lc = self._find_inverse(a1*s, a2*s)
        lc = Lightcurve(self.time, self._extract_and_scale(lc),
                        err_dist='gauss', dt=self.dt)

        return lc


    def _simulate_model(self, model):
        """
        For generating a light curve from a pre-defined model

        Parameters
        ----------
<<<<<<< HEAD
        model: astropy.modeling.Model derived function
            the pre-defined model
            (library-based, available in astropy.modeling.models or custom-defined)

        Returns
        -------
        lightCurve: `LightCurve` object
=======
        model : astropy.modeling.Model derived function
            the pre-defined model
            (library-based, available in astropy.modeling.models or
            custom-defined)

        Returns
        -------
        lightCurve : `LightCurve` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        # Frequencies at which the PSD is to be computed
        # (only positive frequencies, since the signal is real)
        nbins = self.red_noise*self.N
        simfreq = np.fft.rfftfreq(nbins, d=self.dt)[1:]

        # Compute PSD from model
        simpsd = model(simfreq)

        fac = np.sqrt(simpsd/2.)
        pos_real   = self.random_state.normal(size=nbins//2)*fac
        pos_imag   = self.random_state.normal(size=nbins//2)*fac

<<<<<<< HEAD
        pos_freq_transform = pos_real + 1j * pos_imag

        # Simulate light curve from its Fourier transform
        arg  = np.concatenate(([self.mean], pos_freq_transform))

        # Inverse Fourier transform
        long_lc = np.fft.irfft(arg)
=======
        long_lc = self._find_inverse(pos_real, pos_imag)
>>>>>>> cbe87c34664519d992317792703ccec5492528f2

        lc = Lightcurve(self.time, self._extract_and_scale(long_lc),
                        err_dist='gauss', dt=self.dt)
        return lc


    def _simulate_model_string(self, model_str, params):
        """
        For generating a light curve from a pre-defined model

        Parameters
        ----------
<<<<<<< HEAD
        model_str: string
            name of the pre-defined model
        params: list or dictionary
=======
        model_str : string
            name of the pre-defined model
        params : list or dictionary
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            parameters of the pre-defined model

        Returns
        -------
<<<<<<< HEAD
        lightCurve: `LightCurve` object
=======
        lightCurve : `LightCurve` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        # Frequencies at which the PSD is to be computed
        # (only positive frequencies, since the signal is real)
        nbins = self.red_noise*self.N
        simfreq = np.fft.rfftfreq(nbins, d=self.dt)[1:]

        if model_str in dir(models):
            if isinstance(params, dict):
                model = eval('models.' + model_str + '(**params)')
                # Compute PSD from model
                simpsd = model(simfreq)
            elif isinstance(params, list):
                simpsd = eval('models.' + model_str + '(simfreq, params)')
            else:
                raise ValueError('Params should be list or dictionary!')

            fac = np.sqrt(simpsd/2.)
            pos_real   = self.random_state.normal(size=nbins//2)*fac
            pos_imag   = self.random_state.normal(size=nbins//2)*fac

<<<<<<< HEAD
            pos_freq_transform = pos_real + 1j * pos_imag

            # Simulate light curve from its Fourier transform
            arg  = np.concatenate(([self.mean], pos_freq_transform))

            # Inverse Fourier transform
            long_lc = np.fft.irfft(arg)
=======
            long_lc = self._find_inverse(pos_real, pos_imag)
>>>>>>> cbe87c34664519d992317792703ccec5492528f2

            lc = Lightcurve(self.time, self._extract_and_scale(long_lc),
                            err_dist='gauss', dt=self.dt)
            return lc
        else:
            raise ValueError('Model is not defined!')

<<<<<<< HEAD


=======
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
    def _simulate_impulse_response(self, s, h, mode='same'):
        """
        Generate LightCurve from impulse response. To get
        accurate results, binning intervals (dt) of variability
        signal 's' and impulse response 'h' must be equal.

        Parameters
        ----------
<<<<<<< HEAD
        s: array-like
            Underlying variability signal
        h: array-like
            Impulse response
        mode: str
=======
        s : array-like
            Underlying variability signal
        h : array-like
            Impulse response
        mode : str
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            mode can be 'same', 'filtered, or 'full'.
            'same' indicates that the length of output light
            curve is same as that of input signal.
            'filtered' means that length of output light curve
            is len(s) - lag_delay
            'full' indicates that the length of output light
            curve is len(s) + len(h) -1

        Returns
        -------
<<<<<<< HEAD
        lightCurve: `LightCurve` object
=======
        lightCurve : `LightCurve` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """
        lc = signal.fftconvolve(s, h)

        if mode == 'same':
            lc = lc[:-(len(h) - 1)]
        elif mode == 'filtered':
            lc = lc[(len(h) - 1):-(len(h) - 1)]

        time = self.dt * np.arange(len(lc))
        return Lightcurve(time, lc, err_dist='gauss', dt=self.dt)

    def _find_inverse(self, real, imaginary):
        """
        Forms complex numbers corresponding to real and imaginary
        parts and finds inverse series.

        Parameters
        ----------
<<<<<<< HEAD
        real: numpy.ndarray
            Co-effients corresponding to real parts of complex numbers
        imaginary: numpy.ndarray
=======
        real : numpy.ndarray
            Co-effients corresponding to real parts of complex numbers
        imaginary : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Co-efficients correspondong to imaginary parts of complex
            numbers

        Returns
        -------
<<<<<<< HEAD
        ifft: numpy.ndarray
=======
        ifft : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Real inverse fourier transform of complex numbers
        """

        # Form complex numbers corresponding to each frequency
        f = [complex(r, i) for r,i in zip(real,imaginary)]

        f = np.hstack([self.mean, f])

        # Obtain real valued time series
        f_conj = np.conjugate(np.array(f))

        # Obtain time series
        return np.fft.irfft(f_conj, n=self.red_noise*self.N)

    def _extract_and_scale(self, long_lc):
        """
        i) Make a random cut and extract a light curve of required
        length.

        ii) Rescale light curve i) with zero mean and unit standard
        deviation, and ii) user provided mean and rms (fractional
        rms * mean)

        Parameters
        ----------
<<<<<<< HEAD
        long_lc: numpy.ndarray
=======
        long_lc : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Simulated lightcurve of length 'N' times 'red_noise'

        Returns
        -------
<<<<<<< HEAD
        lc: numpy.ndarray
=======
        lc : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Normalized and extracted lightcurve of length 'N'
        """
        if self.red_noise == 1:
            lc = long_lc
        else:
            # Make random cut and extract light curve of length 'N'
<<<<<<< HEAD
            extract = self.random_state.randint(self.N-1, self.red_noise*self.N - self.N+1)
            lc = np.take(long_lc, list(range(extract, extract + self.N)))
=======
            extract = \
                self.random_state.randint(self.N-1,
                                          self.red_noise*self.N - self.N+1)
            lc = np.take(long_lc, range(extract, extract + self.N))
>>>>>>> cbe87c34664519d992317792703ccec5492528f2

        avg = np.mean(lc)
        std = np.std(lc)

        return (lc-avg)/std * self.mean * self.rms + self.mean

    def powerspectrum(self, lc, seg_size=None):
        """
        Make a powerspectrum of the simulated light curve.

        Parameters
        ----------
<<<<<<< HEAD
        lc: lightcurve.Lightcurve object OR
=======
        lc : lightcurve.Lightcurve object OR
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            iterable of lightcurve.Lightcurve objects
            The light curve data to be Fourier-transformed.

        Returns
        -------
<<<<<<< HEAD
        power: numpy.ndarray
=======
        power : numpy.ndarray
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            The array of normalized squared absolute values of Fourier
            amplitudes

        """
        if seg_size is None:
            seg_size = lc.tseg

        return AveragedPowerspectrum(lc, seg_size).power

    @staticmethod
    def read(filename, format_='pickle'):
        """
        Imports Simulator object.

        Parameters
        ----------
<<<<<<< HEAD
        filename: str
            Name of the Simulator object to be read.

        format_: str
=======
        filename : str
            Name of the Simulator object to be read.

        format_ : str
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Available option is 'pickle.'

        Returns
        -------
<<<<<<< HEAD
        object: `Simulator` object
=======
        object : `Simulator` object
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
        """

        if format_ == 'pickle':
            data = io.read(filename, 'pickle')
            return data
        else:
            raise KeyError("Format not supported.")

    def write(self, filename, format_='pickle'):
        """
        Exports Simulator object.

        Parameters
        ----------
<<<<<<< HEAD
        filename: str
            Name of the Simulator object to be created.

        format_: str
=======
        filename : str
            Name of the Simulator object to be created.

        format_ : str
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
            Available options are 'pickle' and 'hdf5'.
        """

        if format_ == 'pickle':
            io.write(self, filename)
        else:
            raise KeyError("Format not supported.")
