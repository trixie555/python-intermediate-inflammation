"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np

class Patient:
    def __init__(self, name, weight, height): # Constructor; self means it passes a variable to itself
        self.name = name 
        self.weight = weight
        self.height = height

    def get_body_mass_index(self):
        """compute body mass index: weight_in_kg/height_in_meters**2
        """
        return self.weight/self.height**2

class Circle:
    def __init__(self, radius): # Constructor; self means it passes a variable to itself
        self.radius = radius 

# rosa = Circle(radius=4)
# rosa.radius

def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data:np.array):
    """Calculates the mean of axis 0 of a data file.

    :param data: csv file of shape (m,n) with m = , n = 
    :return: mean of each column (m,1) (pandas datafile)
    """    
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)

