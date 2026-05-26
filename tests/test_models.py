"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""

    test_input = np.array([[0, 0], [0, 0], [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""

    test_input = np.array([[1, 2], [3, 4], [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_positive_integers():
    """Test that max function works for an array positive integers."""

    test_input = np.array([[-2, -32], [0, 5], [4, 2]])
    test_result = np.array([4, 5])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max__negative_integers():
    """Test that max function works for an array of positive and negative integers."""

    test_input = np.array([[0, 32], [0, 0], [4, 2]])
    test_result = np.array([4, 32])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_max_string():
    """Test for TypeError whne parsing strings."""

    with pytest.raises(TypeError):
        error_expected = daily_max(["Hello", "there"])  # noqa: F841


@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0]),
        ([[1, 2, -1], [3, -2, 4], [5, -9, 6]], [1, -9, -1]),
        ([[0, 1, 2], [0, 3, 4]], [0, 1, 2]),  # array containing zeros
        ([[3, 3, 3], [3, 3, 3], [3, 3, 3]], [3, 3, 3]),  # all values the same
    ],
)
def test_daily_min(test_input, test_result):
    """Test that min function works for an array of positive and negative integers."""
    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_max_empty_array():
    """Test that daily_max raises ValueError when given an empty array."""
    with pytest.raises(ValueError):
        daily_max([])


def test_daily_max_nan_propagation():
    data = np.array([[1, np.nan], [3, 4]])
    result = daily_max(data)
    assert np.isnan(result[1])  # documents current behavior
