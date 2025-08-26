"""
examples/lofi.py
generates low fidelity wavetables for LittleGPTracker
Nine 2025.04.09
GPLv3+
"""
# library imports
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_noise, osc_saw, osc_sine, osc_square, osc_triangle
from metempsychosis.macros import wavetable_pwm, wavetable_xfade
from metempsychosis.utils import ensure_dir, samples_to_frequency
# os imports
from os import getenv
# constants
NUM_CYCLES = int(getenv("NUM_CYCLES") or 16)
NUM_SAMPLES = int(getenv("NUM_SAMPLES") or 16)

if __name__ == "__main__":
    # procedurally generate wavetables
    ensure_dir((path:= "export/lofi"))
    freq = int(samples_to_frequency(NUM_SAMPLES))

    # prerender basic waves to save time
    noise = list(osc_noise(NUM_SAMPLES))
    saw = list(osc_saw(freq, NUM_SAMPLES))
    sine = list(osc_sine(freq, NUM_SAMPLES))
    square = list(osc_square(freq, NUM_SAMPLES))
    triangle = list(osc_triangle(freq, NUM_SAMPLES))

    # noise to *
    write_wav(path + "/noisetosaw.wav", wavetable_xfade(NUM_CYCLES, noise, saw))
    write_wav(path + "/noisetosine.wav", wavetable_xfade(NUM_CYCLES, noise, sine))
    write_wav(path + "/noisetosquare.wav", wavetable_xfade(NUM_CYCLES, noise, square))
    write_wav(path + "/noisetotriangle.wav", wavetable_xfade(NUM_CYCLES, noise, triangle))

    # saw to *
    write_wav(path + "/sawtonoise.wav", wavetable_xfade(NUM_CYCLES, saw, noise))
    write_wav(path + "/sawtosine.wav", wavetable_xfade(NUM_CYCLES, saw, sine))
    write_wav(path + "/sawtosquare.wav", wavetable_xfade(NUM_CYCLES, saw, square))
    write_wav(path + "/sawtotriangle.wav", wavetable_xfade(NUM_CYCLES, saw, triangle))

    # sine to *
    write_wav(path + "/sinetonoise.wav", wavetable_xfade(NUM_CYCLES, sine, noise))
    write_wav(path + "/sinetosaw.wav", wavetable_xfade(NUM_CYCLES, sine, saw))
    write_wav(path + "/sinetosquare.wav", wavetable_xfade(NUM_CYCLES, sine, square))
    write_wav(path + "/sinetotriangle.wav", wavetable_xfade(NUM_CYCLES, sine, triangle))

    # square to *
    write_wav(path + "/squaretonoise.wav", wavetable_xfade(NUM_CYCLES, square, noise))
    write_wav(path + "/squaretosaw.wav", wavetable_xfade(NUM_CYCLES, square, saw))
    write_wav(path + "/squaretosine.wav", wavetable_xfade(NUM_CYCLES, square, sine))
    write_wav(path + "/squaretotriangle.wav", wavetable_xfade(NUM_CYCLES, square, triangle))

    # triangle to *
    write_wav(path + "/triangletonoise.wav", wavetable_xfade(NUM_CYCLES, triangle, noise))
    write_wav(path + "/triangletosaw.wav", wavetable_xfade(NUM_CYCLES, triangle, saw))
    write_wav(path + "/triangletosine.wav", wavetable_xfade(NUM_CYCLES, triangle, sine))
    write_wav(path + "/triangletosquare.wav", wavetable_xfade(NUM_CYCLES, triangle, square))

    # pwm wavetable
    write_wav(path + "/pwm.wav", wavetable_pwm(NUM_CYCLES, NUM_SAMPLES))
