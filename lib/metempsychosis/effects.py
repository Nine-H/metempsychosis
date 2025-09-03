"""
effects.py
transform waves with effects
Nine 2025.04.09
GPLv3+
"""
# system imports
from collections.abc import Iterable
from math import pi, sqrt, tan
# loacl imports
from .constants import BIT_DEPTH, SAMPLE_RATE


def fx_allpass(sample, c: float, r: float, q: float) -> Iterable[float]:
    """
    apply a allpass filter to the sample
    sample = the sample to process
    :param c: filter cutoff
    :param r: resonance
    :param q: width
    """
    b = 0
    for s in sample:
        t = tan(pi * c / SAMPLE_RATE)
        a1 = (t - 1.0) / (t + 1.0)
        a = a1 * s + b
        b = s - a1 * a
        yield a


def fx_attenuate(sample, mix: float) -> Iterable[float]:
    """
    sets the gain on a sample
    :param sample: sample
    :param mix: volume between 0 and 1
    """
    for s in sample:
        yield s * mix


def fx_bandpass(sample, c: float, r: float, q: float) -> Iterable[float]:
    """
    apply a highpass filter to the sample
    :param sample: sample to process
    :param c: filter cutoff
    :param r: resonance
    :param q: width
    """
    for s, f in zip(sample, fx_allpass(sample, c, r, q)):
        # FIXME: this is probably stupid
        h = (f * -1 + s) * 0.5
        yield (h + f) * 0.5


def fx_bias(sample, bias: float) -> Iterable[float]:
    """
    biases a sample
    :param sample: sample to process
    :param bias: bias from -1 to 1
    """
    for s in sample:
        yield s + bias


def fx_bitcrush(
    sample: Iterable[float],
    bit_depth: int = BIT_DEPTH,
) -> Iterable[float]:
    """
    distorts sample by reducing bit depth
    :param bit_depth: the new bit depth for the sample
    """
    d = pow(2, min(bit_depth, BIT_DEPTH)) - 1
    for s in sample:
        n = (s + 1.0) * 0.5
        q = round(n * d) / d
        yield (q - 0.5) * 2.0
 

def fx_clip(sample, lim: float = 1.0) -> Iterable[float]:
    """
    clips a sample to fit amplitude by limit
    :param sample: sample to process
    :param lim: limit from 0 to 1
    """
    for s in sample:
        yield min(max(s, -lim), lim)


def fx_downsample(
    sample: Iterable[float],
    sample_rate: int = SAMPLE_RATE,
) -> Iterable[float]:
    """
    distorts sample by reducing sample rate
    :param sample_rate: the new sample rate for the sample
    """
    sample_rate = min(sample_rate, SAMPLE_RATE)
    r = int(SAMPLE_RATE / sample_rate)
    b = 0.0
    for i, s in enumerate(sample):
        if i == 0:
            b = s
        elif i % r == 0:
            b = s
        yield b


def fx_highpass(sample, c: float, r: float, q: float) -> Iterable[float]:
    """
    apply a highpass filter to the sample
    :param sample: sample to process
    :param c: filter cutoff
    :param r: resonance
    :param q: width
    """
    for s, f in zip(sample, fx_allpass(sample, c, r, q)):
        yield (f * -1 + s) * 0.5


def fx_lowpass(sample, c: float, r: float, q: float) -> Iterable[float]:
    """
    apply a lowpass filter to the sample
    :param sample: sample to process
    :param c: filter cutoff
    :param r: resonance
    :param q: width
    """
    for s, f in zip(sample, fx_allpass(sample, c, r, q)):
        yield (s + f) * 0.5


def fx_reverse(sample: Iterable[float]) -> Iterable[float]:
    """
    play sample in reverse
    :param sample: sample to process
    """
    for s in list(sample)[::-1]:
        yield s


def fx_speed(sample: Iterable[float], t: float) -> Iterable[float]:
    """
    change the speed of a sample, not preserving pitch
    :param sample: sample to process
    :param t: speed
    """
    n = SAMPLE_RATE * t
    for s in sample:
        yield s


def fx_timestretch(sample: Iterable[float], t: float) -> Iterable[float]:
    """
    change the speed of a sample, preserving pitch
    :param sample: sample to process
    :param t: speed
    """
    b = list(sample)
    n = int(len(b) * t)
    for s in sample:
        yield s


def fx_wavefold(sample, lim: float = 1.0) -> Iterable[float]:
    """
    clips a sample to fit amplitude by folding it back on itself
    :param sample: sample to process
    :param lim: limit from 0 to 1
    """
    for s in sample:
        if s > lim:
            yield lim - (s - lim)
        elif s < -lim: 
            yield -lim + (s - lim)
        else:
            yield s


def fx_wrap(sample, lim: float = 1.0) -> Iterable[float]:
    """
    clips a sample to fit amplitude by wrapping it around to negative
    :param sample: sample to process
    :param lim: limit from 0 to 1
    """
    for s in sample:
        if s > lim:
            yield -lim + (s - lim)
        elif s < -lim: 
            yield lim - (s - lim)
        else:
            yield s


def fx_xfade(a, b, mix: float = 0.5) -> Iterable[float]:
    """
    mixes two samples
    :param a: sample a
    :param b: sample b
    :param mix: mix weight between 0 and 1
    """
    inverse = 1.0 - mix
    for a, b in zip(a, b):
        yield (a * inverse) + (b * mix)


def fx_xfade_equal(a, b, mix: float = 0.5) -> Iterable[float]:
    """
    mixes two samples correcting for equal gain
    :param a: sample a
    :param b: sample b
    :param mix: mix weight between 0 and 1
    """
    mix = sqrt(1.0 - mix)
    inverse = -mix + 1
    for a, b in zip(a, b):
        yield (a * mix) + (b * inverse)
