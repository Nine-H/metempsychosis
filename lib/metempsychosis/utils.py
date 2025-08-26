"""
utils.py
utility functions that are generally useful
Nine 2025.04.09
GPLv3+
"""
# imports
from os import makedirs
from os.path import exists
# local imports
from .constants import SAMPLE_RATE


def duration_to_samples(d) -> int:
    """
    convert a duration in seconds to samples
    d = duration seconds
    """
    return round(d * SAMPLE_RATE)


def ensure_dir(path) -> None:
    """
    ensures a filesystem path exists
    path = filesystem path
    """
    if not exists(path):
        makedirs(path)


def frequency_to_samples(f) -> int:
    """
    returns number of samples to complete a cycle at sample rate
    f = frequency
    """
    return round(SAMPLE_RATE / f)


def samples_to_frequency(c) -> float:
    """
    returns the frequency of wave given the number of samples in 1 cycle
    c = num samples
    """
    return SAMPLE_RATE / c
