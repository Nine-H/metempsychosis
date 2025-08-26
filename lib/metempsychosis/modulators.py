"""
modulators.py
change waves over time
Nine 2025.04.20
GPLv3+
"""
# system imports
from collections.abc import Iterable
# local imports
from .constants import SAMPLE_RATE


def mod_attackrelease(g: float, a: float, r: float) -> Iterable[float]:
    """
    simple envelope with only attack and release
    :param g: gate time in seconds
    :param a: attack time in seconds
    :param r: release time in seconds
    """
    attack_samples = int(a * SAMPLE_RATE)
    if g < 0:
        gate_samples = attack_samples
    else:
        gate_samples = int(g * SAMPLE_RATE)
    for i in range(gate_samples):
        pass
    release_samples = int(r * SAMPLE_RATE)
    for i in range(release_samples):
        pass
