"""
pysynth.py

procedurally generate samples and wavetables with python.
low level to support various retro samplers and trackers.
definitely bug free I swear XD.

Nine 2025.04.09
GPLv3+
"""
# system imports
from functools import partial
from math import floor, pi, sin, sqrt
from os import makedirs
from os.path import exists
from random import randint
from wave import open
# constants
SAMPLE_RATE = 44100
BIT_DEPTH = 16
A_TUNING = 440
C_TUNING = 261.63

# pcm typedef
pcm = partial(
    int.to_bytes,
    length=BIT_DEPTH // 8,
    byteorder="little",
    signed=True,
)


def ensure_dir(path):
    """
    ensures a filesystem path exists
    path = filesystem path
    """
    if not exists(path):
        makedirs(path)


def _range():
    """
    get the minimum and maximum value of a sample
    """
    return pow(-2, BIT_DEPTH - 1), pow(2, BIT_DEPTH - 1) - 1


def duration_to_samples(d):
    """
    convert a duration in seconds to samples
    d = duration seconds
    """
    return round(d * SAMPLE_RATE)


def frequency_to_samples(f):
    """
    returns number of samples to complete a cycle at sample rate
    f = frequency
    """
    return round(SAMPLE_RATE / f)


def samples_to_frequency(c):
    """
    returns the frequency of wave given the number of samples in 1 cycle
    c = num samples
    """
    return SAMPLE_RATE / c


def fx_clip(sample):
    """
    clips a sample to fit bit depth
    """
    sample_min, sample_max = _range()
    return min(max(sample, sample_min), sample_max)


def fx_xfade(a, b, mix):
    """
    mixes two samples
    a = sample a
    b = sample b
    mix = mix weight between 0 and 1
    """
    inverse = 1.0 - mix
    for a, b in zip(a, b):
        yield round(fx_clip((a * inverse) + (b * mix)))


def fx_xfade_equal(a, b, mix):
    """
    mixes two samples correcting for equal gain
    a = sample a
    b = sample b
    mix = mix weight between 0 and 1
    """
    mix = sqrt(1.0 - mix)
    inverse = -mix + 1
    for a, b in zip(a, b):
        yield round(fx_clip((a * mix) + (b * inverse)))


def osc_noise(c):
    """
    returns noise samples
    c = number of samples
    """
    sample_min, sample_max = _range()
    for _ in range(c):
        yield randint(sample_min, sample_max)


def osc_pwm(f, c, d=0.5):
    """
    return a pwm wave
    f = frequency hz
    c = number of samples
    d = duty cycle, 0 to 1
    """
    _, m = _range()
    f = frequency_to_samples(f)
    for i in range(c):
        a = (i % f < f * d) * 2 - 1
        yield round(a * m)


def osc_saw(f, c):
    """
    return a saw wave
    f = frequency hz
    c = number of samples
    """
    _, m = _range()
    f = frequency_to_samples(f)
    for i in range(c):
        # t = i % f / f
        # a = 1.0 - (t * 2)
        a = (1.0 - abs(i / f - floor (i / f)) - 0.5) * 2
        yield round(a * m)


def osc_sine(f, c):
    """
    return a sine wave
    f = frequency hz
    c = number of samples
    """
    _, m = _range()
    for i in range(c):
        t = i / SAMPLE_RATE
        a = sin(2 * pi * f * t)
        yield round(a * m)


def osc_square(f, c):
    """
    return a square wave
    f = frequency hz
    c = number of samples
    """
    _, m = _range()
    f = frequency_to_samples(f)
    for i in range(c):
        # a = (i % f < f / 2) * 2 - 1
        a = (floor(i / f - floor(i / f + 0.5)) + 0.5) * 2
        yield round(a * m)


def osc_triangle(f, c):
    """
    return a triangle wave
    f = frequency hz
    c = number of samples
    """
    _, m = _range()
    f = frequency_to_samples(f)
    for i in range(c):
        i += f / 4
        a = (abs(i / f - floor(i / f + 0.5)) - 0.25) * 4.0 
        yield round(a * m)


def write_wav(name, samples):
    """
    writes a sample to a file
    """
    data = bytes()
    for s in samples:
        data += pcm(s)

    with open(name, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(BIT_DEPTH // 8)
        file.setframerate(SAMPLE_RATE)
        file.writeframes(data)


def wavetable_pwm(n, c):
    """
    creates a pwm wavetable
    n = number of cycles
    c = number of samples
    """
    f = samples_to_frequency(c)
    return [s for i in range(n) for s in list(osc_pwm(f, n, i / (n - 1)))]


def wavetable_xfade(n, a, b):
    """
    creates a crossfade wavetable
    n = number of cycles
    a = wave a
    b = wave b
    """
    return [s for i in range(n) for s in list(fx_xfade_equal(a, b, i / (n - 1)))]


if __name__ == "__main__":

    # basic waves cd quality:
    ensure_dir((path:= "samples/basic"))
    num_samples = frequency_to_samples(C_TUNING) * 2

    write_wav(path + "/noise.wav", osc_noise(num_samples))
    write_wav(path + "/sine.wav", osc_sine(C_TUNING, num_samples))
    write_wav(path + "/saw.wav", osc_saw(C_TUNING, num_samples))
    write_wav(path + "/square.wav", osc_square(C_TUNING, num_samples))
    write_wav(path + "/triangle.wav", osc_triangle(C_TUNING, num_samples))

    # complex wave
    ensure_dir((path:= "samples/complex"))
    write_wav(
        path + "/mix.wav",
        fx_xfade(
            osc_sine(C_TUNING, frequency_to_samples(C_TUNING)),
            fx_xfade(
                osc_square(C_TUNING, frequency_to_samples(C_TUNING)),
                osc_triangle(C_TUNING/4, frequency_to_samples(C_TUNING)),
                0.8,
            ),
            0.8,
        )
    )

    # procedurally generate wavetables
    ensure_dir((path:= "samples/wavetables"))
    num_cycles = 16
    num_samples = frequency_to_samples(C_TUNING)

    noise = list(osc_noise(num_samples))
    saw = list(osc_saw(C_TUNING, num_samples))
    sine = list(osc_sine(C_TUNING, num_samples))
    square = list(osc_square(C_TUNING, num_samples))
    triangle = list(osc_triangle(C_TUNING, num_samples))

    # noise to *
    write_wav(path + "/noisetosaw.wav", wavetable_xfade(num_cycles, noise, saw))
    write_wav(path + "/noisetosine.wav", wavetable_xfade(num_cycles, noise, sine))
    write_wav(path + "/noisetosquare.wav", wavetable_xfade(num_cycles, noise, square))
    write_wav(path + "/noisetotriangle.wav", wavetable_xfade(num_cycles, noise, triangle))

    # saw to *
    write_wav(path + "/sawtonoise.wav", wavetable_xfade(num_cycles, saw, noise))
    write_wav(path + "/sawtosine.wav", wavetable_xfade(num_cycles, saw, sine))
    write_wav(path + "/sawtosquare.wav", wavetable_xfade(num_cycles, saw, square))
    write_wav(path + "/sawtotriangle.wav", wavetable_xfade(num_cycles, saw, triangle))

    # sine to *
    write_wav(path + "/sinetonoise.wav", wavetable_xfade(num_cycles, sine, noise))
    write_wav(path + "/sinetosaw.wav", wavetable_xfade(num_cycles, sine, saw))
    write_wav(path + "/sinetosquare.wav", wavetable_xfade(num_cycles, sine, square))
    write_wav(path + "/sinetotriangle.wav", wavetable_xfade(num_cycles, sine, triangle))

    # square to *
    write_wav(path + "/squaretonoise.wav", wavetable_xfade(num_cycles, square, noise))
    write_wav(path + "/squaretosaw.wav", wavetable_xfade(num_cycles, square, saw))
    write_wav(path + "/squaretosine.wav", wavetable_xfade(num_cycles, square, sine))
    write_wav(path + "/squaretotriangle.wav", wavetable_xfade(num_cycles, square, triangle))

    # triangle to *
    write_wav(path + "/triangletonoise.wav", wavetable_xfade(num_cycles, triangle, noise))
    write_wav(path + "/triangletosaw.wav", wavetable_xfade(num_cycles, triangle, saw))
    write_wav(path + "/triangletosine.wav", wavetable_xfade(num_cycles, triangle, sine))
    write_wav(path + "/triangletosquare.wav", wavetable_xfade(num_cycles, triangle, square))

    # lofi gameboy waves
    ensure_dir((path:= "samples/gb_waves"))
    num_samples = 32
    freq = samples_to_frequency(num_samples)

    noise = list(osc_noise(num_samples))
    saw = list(osc_saw(freq, num_samples))
    sine = list(osc_sine(freq, num_samples))
    square = list(osc_square(freq, num_samples))
    triangle = list(osc_square(freq, num_samples))

    write_wav(path + "/gbnoise.wav", noise)
    write_wav(path + "/gbsaw.wav", saw)
    write_wav(path + "/gbsine.wav", sine)
    write_wav(path + "/gbsquare.wav", square)
    write_wav(path + "/gbtriangle.wav", triangle)

    # lofi gameboy wavetables
    num_cycles = 16
    ensure_dir((path:= "samples/gb_wavetables"))
    write_wav(path + "/gb_pwm.wav", wavetable_pwm(num_samples, num_cycles))

    # write_wav("gbsine.wav", osc_sine(samples_to_frequency(16), 16))
    # write_wav(path + "gb_sinetosaw.wav", wavetable_xfade(num_cycles, sine, saw))
