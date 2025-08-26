"""
examples/wavetables.py
generates cd quality wavetables for LittleGPTracker
Nine 2025.04.09
GPLv3+
"""
# library imports
from metempsychosis.constants import C_TUNING
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_noise, osc_saw, osc_sine, osc_square, osc_triangle
from metempsychosis.macros import wavetable_pwm, wavetable_xfade
from metempsychosis.utils import ensure_dir, frequency_to_samples

if __name__ == "__main__":
    # procedurally generate wavetables
    ensure_dir((path:= "export/wavetables"))
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

    # pwm wavetable
    write_wav(path + "/pwm.wav", wavetable_pwm(num_cycles, num_samples))
