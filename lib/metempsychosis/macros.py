"""
macros.py
macros that combine other effects
Nine 2025.04.09
GPLv3+
"""
# system imports
from collections.abc import Callable, Iterable
# local imports
from .effects import fx_attenuate, fx_bias, fx_clip, fx_xfade_equal
from .oscillators import osc_pwm
from .utils import samples_to_frequency
# constants
FILTER_MAX = 20_000


def wavetable_lsdj(
    osc: Callable,
    filt: Callable,
    dist: Callable,
    n: int,
    c: int,
    a_vol: float = 1.0,
    a_res: float = 0.0,
    a_cut: float = 1.0,
    a_bias: float = 0.0,
    a_lim: float = 1.0,
    a_phase: float = 0.0,
    b_vol: float = 1.0,
    b_res: float = 0.0,
    b_cut: float = 1.0,
    b_bias: float = 0.0,
    b_lim: float = 1.0,
    b_phase: float = 0.0,
) -> Iterable[float]:
    """
    emulation of the lsdj wavetable synth
    :param signal: an oscillator function
    :param filter: a filter function
    :param distortion: a clipping function
    :param n: number of cycles
    :param c: number of samples per wave
    :param a_vol: start volume
    :param a_res: start resonance
    :param a_cut: start cutoff
    :param a_bias: start bias
    :param a_bias: start bias
    :param a_lim: start lim
    :param a_phase: start phase
    :param b_vol: end volume
    :param b_res: end resonance
    :param b_cut: end cutoff
    :param b_bias: end bias
    :param b_bias: end bias
    :param b_lim: end lim
    :param b_phase: end phase
    """
    # precalculate deltas
    d_vol = b_vol - a_vol
    d_res = b_res - a_res
    d_cut = b_cut - a_cut
    d_bias = b_bias - a_bias
    d_lim = b_lim - a_lim
    d_phase = b_phase - a_phase

    # start generating wavetables
    wave = []
    for i in range(n):
        lerp = i / (n - 1)
        # calculate interpolated parameters
        vol = a_vol + (lerp * d_vol)
        res = a_res + (lerp * d_res)
        cut = a_cut + (lerp * d_cut)
        bias = a_bias + (lerp * d_bias)
        lim = a_lim + (lerp * d_lim)
        phase = a_phase + (lerp * d_phase)

        # signal chain
        samples = osc(samples_to_frequency(c), c)  # initial waveform
        samples = filt(samples, cut * FILTER_MAX, res, 0.0)  # filtered
        samples = fx_bias(samples, bias)  # biased
        samples = dist(samples, lim)  # clipped
        samples = fx_attenuate(samples, vol)  # attenuated
        samples = fx_clip(samples) # fix bad programming

        # append them to the wave
        wave.extend(list(samples))

    return wave


def wavetable_pwm(n: int, c: int) -> Iterable[float]:
    """
    creates a pwm wavetable
    :param n: number of cycles
    :param c: number of samples
    """
    f = samples_to_frequency(c)
    return [s for i in range(n) for s in list(osc_pwm(f, c, i / (n - 1)))]


def wavetable_xfade(n: int, a: Iterable[float], b: Iterable[float]) -> Iterable[float]:
    """
    creates a crossfade wavetable
    :param n: number of cycles
    :param a: sample a
    :param b: sample b
    """
    return [s for i in range(n) for s in list(fx_xfade_equal(a, b, i / (n - 1)))]
