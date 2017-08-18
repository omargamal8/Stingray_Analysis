<<<<<<< HEAD

from astropy.modeling.models import custom_model

@custom_model
def GeneralizedLorentz1D(x, x_0=1., fwhm=1., value=1., power_coeff=1.):
    """
    Generalized lorenzian function, 
=======
from __future__ import division, print_function, absolute_import
from astropy.modeling.models import custom_model


#TODO: Add Jacobian
@custom_model
def GeneralizedLorentz1D(x, x_0=1., fwhm=1., value=1., power_coeff=1.):
    """
    Generalized Lorentzian function,
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
    implemented using astropy.modeling.models custom model

    Parameters
    ----------

    x: numpy.ndarray
        non-zero frequencies

    x_0 : peak centeral frequency
    fwhm : FWHM of the peak (gamma)
    value : peak value at x=x0
    power_coeff : power coefficient [n]

    Returns
    -------
    model: astropy.modeling.Model
        generalized Lorentzian psd model
    """
    assert power_coeff > 0., "The power coefficient should be greater than zero."
<<<<<<< HEAD
    return value * (fwhm / 2)**power_coeff * 1./(abs(x - x_0)**power_coeff + (fwhm / 2)**power_coeff) 
    
=======
    return value * (fwhm / 2)**power_coeff * 1./(abs(x - x_0)**power_coeff + (fwhm / 2)**power_coeff)


#TODO: Add Jacobian
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
@custom_model
def SmoothBrokenPowerLaw(x, norm=1., gamma_low=1., gamma_high=1., break_freq=1.):
    """
    Smooth broken power law function,
    implemented using astropy.modeling.models custom model

    Parameters
    ----------
<<<<<<< HEAD

=======
>>>>>>> cbe87c34664519d992317792703ccec5492528f2
    x: numpy.ndarray
        non-zero frequencies

    norm: normalization frequency
    gamma_low: power law index for f --> zero
    gamma_high: power law index for f --> infinity
    break_freq: break frequency

    Returns
    -------
    model: astropy.modeling.Model
        generalized smooth broken power law psd model
    """
    return norm * x**(-gamma_low) / (1. + (x / break_freq)**2)**(-(gamma_low - gamma_high) / 2)
    

<<<<<<< HEAD
def lorenzian(x, p):
    """
    Generalized lorenzian function.
=======
def generalized_lorentzian(x, p):
    """
    Generalized Lorentzian function.
>>>>>>> cbe87c34664519d992317792703ccec5492528f2

    Parameters
    ----------

    x: numpy.ndarray
        non-zero frequencies

    p: iterable
        p[0] = peak centeral frequency
        p[1] = FWHM of the peak (gamma)
        p[2] = peak value at x=x0
        p[3] = power coefficient [n]

    Returns
    -------
    model: numpy.ndarray
<<<<<<< HEAD
        generalized lorenzian psd model
    """

    assert p[3] > 0., "The power coefficient should be greater than zero."
    return p[2] * (p[1] / 2)**p[3] * 1./(abs(x - p[0])**p[3] + (p[1] / 2)**p[3]) 
=======
        generalized lorentzian psd model
    """

    assert p[3] > 0., "The power coefficient should be greater than zero."
    return p[2] * (p[1] / 2)**p[3] * 1./(abs(x - p[0])**p[3] + (p[1] / 2)**p[3])

>>>>>>> cbe87c34664519d992317792703ccec5492528f2

def smoothbknpo(x, p):
    """
    Smooth broken power law function.

    Parameters
    ----------

    x: numpy.ndarray
        non-zero frequencies

    p: iterable
        p[0] = normalization frequency
        p[1] = power law index for f --> zero
        p[2] = power law index for f --> infinity
        p[3] = break frequency

    Returns
    -------
    model: numpy.ndarray
        generalized smooth broken power law psd model
    """

    return p[0] * x**(-p[1]) / (1. + (x / p[3])**2)**(-(p[1] - p[2]) / 2)
