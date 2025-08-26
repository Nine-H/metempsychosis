"""
examples/oneshots.py
generates some oneshot samples
Nine 2025.04.24
GPLv3+
"""
# library imports
from metempsychosis.constants import C_TUNING
from metempsychosis.effects import fx_attenuate, fx_modulate
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_square
from metempsychosis.modulators import mod_attackrelease
from metempsychosis.utils import ensure_dir, duration_to_samples

if __name__ == "__main__":
    # make some oneshots
    ensure_dir((path:= "export/oneshots"))
    num_samples = duration_to_samples(1)

    write_wav(path + "/squareblip.wav", osc_square(C_TUNING, num_samples))
