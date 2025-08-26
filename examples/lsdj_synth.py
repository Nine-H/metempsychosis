"""
examples/lsdj_synth.py
emulates the wavsynth built into lsdj
Nine 2025.04.09
GPLv3+
"""
# library imports
from metempsychosis.effects import (
    # fx_allpass,
    # fx_bandpass,
    fx_clip,
    fx_wavefold,
    fx_highpass,
    fx_lowpass,
    fx_wrap,
)
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_saw, osc_square, osc_triangle
from metempsychosis.macros import wavetable_lsdj
from metempsychosis.utils import ensure_dir, samples_to_frequency
# constants
OSCILLATORS = [osc_saw, osc_square, osc_triangle] 
FILTERS = [fx_lowpass, fx_highpass]  #, fx_bandpass, fx_allpass] 
DISTORTIONS = [fx_clip, fx_wavefold, fx_wrap]


if __name__ == "__main__":
    # set up synth
    ensure_dir((path:= "export/lsdj_wavetables"))
    num_cycles = 16
    num_samples = 32
    freq = samples_to_frequency(num_samples)

    # simple wavetable that is just a square wave shrinking to zero
    write_wav(
        path + "/volume.wav",
        wavetable_lsdj(
            OSCILLATORS[2],
            FILTERS[0],
            DISTORTIONS[0],
            n=num_cycles,
            c=num_samples,
            a_vol=1.0,
            b_vol=0.0,
        )
    )

    # wavetable that uses bias and wavefolding to become more distorted
    write_wav(
        path + "/fold.wav",
        wavetable_lsdj(
            OSCILLATORS[2],
            FILTERS[0],
            DISTORTIONS[1],
            n=num_cycles,
            c=num_samples,
            b_bias=1.0,
        )
    )

    # wavetable that uses bias and wavefolding to become more distorted
    write_wav(
        path + "/wrap.wav",
        wavetable_lsdj(
            OSCILLATORS[1],
            FILTERS[0],
            DISTORTIONS[2],
            n=num_cycles,
            c=num_samples,
        )
    )

    # wavetable that applies a lowpass to zero to a square wave
    write_wav(
        path + "/lowcut.wav",
        wavetable_lsdj(
            OSCILLATORS[1],
            FILTERS[0],
            DISTORTIONS[0],
            n=num_cycles,
            c=num_samples,
            b_cut=0.0,
        )
    )
