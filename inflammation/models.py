"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2d array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :returns: Numpy array from a CSV
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data
    (each row has measurements for a single patient across all days)
    :returns: An array of mean values of measurements for each day.
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily maximum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data
    (each row has measurements for a single patient across all days)
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily minimum of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data
    (each row has measurements for a single patient across all days)
    :returns: An array of min values of measurements for each day.
    """
    return np.min(data, axis=0)


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


def daily_stdev(data):
    """Calculate the daily standard deviation of a 2D inflammation data array for each day.

    :param data: A 2D data array with inflammation data
    (each row has measurements for a single patient across all days)
    :returns: An array of standard deviation values of measurements for each day.
    """
    return np.std(data, axis=0)


