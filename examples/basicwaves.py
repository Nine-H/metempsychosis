"""
examples/basicwaves.py
generates basic waves in cd quality
Nine 2025.04.09
GPLv3+
"""
# package imports
from metempsychosis.constants import C_TUNING
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_noise, osc_saw, osc_sine, osc_square, osc_triangle
from metempsychosis.utils import ensure_dir, frequency_to_samples

if __name__ == "__main__":
    # basic waves cd quality:
    ensure_dir((path:= "export/basic"))
    num_samples = frequency_to_samples(C_TUNING)

    write_wav(path + "/noise.wav", osc_noise(num_samples))
    write_wav(path + "/saw.wav", osc_saw(C_TUNING, num_samples))
    write_wav(path + "/sine.wav", osc_sine(C_TUNING, num_samples))
    write_wav(path + "/square.wav", osc_square(C_TUNING, num_samples))
    write_wav(path + "/triangle.wav", osc_triangle(C_TUNING, num_samples))
