"""
oscillators.py
simple function generators for pysynth
Nine 2025.04.09
GPLv3+
"""
# system imports
from collections.abc import Iterable
from math import floor, pi, sin
from random import random
# local imports
from .constants import SAMPLE_RATE
from .utils import frequency_to_samples


def osc_noise(c: int) -> Iterable[float]:
    """
    returns noise samples
    :param c: number of samples
    """
    for _ in range(c):
        yield random() * 2 - 1


def osc_pwm(f: float, c: int, d: float=0.5) -> Iterable[float]:
    """
    return a pwm wave
    :param f: frequency hz
    :param c: number of samples
    d = duty cycle, 0 to 1
    """
    f = frequency_to_samples(f)
    for i in range(c):
        yield (i % f < f * d) * 2 - 1


def osc_saw(f: float, c: int) -> Iterable[float]:
    """
    return a saw wave
    f = frequency hz
    c = number of samples
    """
    f = frequency_to_samples(f)
    for i in range(c):
        # t = i % f / f
        # a = 1.0 - (t * 2)
        yield (1.0 - abs(i / f - floor (i / f)) - 0.5) * 2


def osc_sine(f: float, c: int) -> Iterable[float]:
    """
    return a sine wave
    :param f: frequency hz
    :param c: number of samples
    """
    for i in range(c):
        t = i / SAMPLE_RATE
        yield sin(2 * pi * f * t)


def osc_square(f: float, c: int) -> Iterable[float]:
    """
    return a square wave
    :param f: frequency hz
    :param c: number of samples
    """
    f = frequency_to_samples(f)
    for i in range(c):
        # a = (i % f < f / 2) * 2 - 1
        yield (floor(i / f - floor(i / f + 0.5)) + 0.5) * 2


def osc_triangle(f, c) -> Iterable[float]:
    """
    return a triangle wave
    :param f: frequency hz
    :param c: number of samples
    """
    f = frequency_to_samples(f)
    for i in range(c):
        i += f / 4
        yield (abs(i / f - floor(i / f + 0.5)) - 0.25) * 4.0 
