"""
examples/supersaw.py
pseudo supersaw based on arp2500 patch
Nine 2025.08.21
GPLv3+
"""
# package imports
from metempsychosis.constants import C_TUNING
from metempsychosis.effects import fx_modulate, fx_xfade_equal
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_saw, osc_pwm
from metempsychosis.utils import ensure_dir, frequency_to_samples

if __name__ == "__main__":
    # create output directory
    ensure_dir((path:= "export/supersaw"))
    num_samples = frequency_to_samples(C_TUNING)

    write_wav(
        path + "/supersaw.wav",
        fx_xfade_equal(
            osc_saw(C_TUNING // 2, num_samples),
            fx_modulate(osc_pwm(C_TUNING // 2, num_samples))
        )
    )
