"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_positive_integers():
    """Test that max function works for an array positive integers."""
    

    test_input = np.array([[-2, -32],
                           [0, 5],
                           [4, 2]])
    test_result = np.array([4, 5])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max__negative_integers():
    """Test that max function works for an array of positive and negative integers."""
    

    test_input = np.array([[0, 32],
                           [0, 0],
                           [4, 2]])
    test_result = np.array([4, 32])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max_string():
    """Test for TypeError whne parsing strings."""

    with pytest.raises(TypeError):
        error_expected = daily_max(['Hello','there'])

