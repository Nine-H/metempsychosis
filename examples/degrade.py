"""
examples/degrade.py
bitcrush some sinewaves, downsample a pcm file
Nine 2025.08.27
GPLv3+
"""
# package imports
from metempsychosis.constants import C_TUNING, SAMPLE_RATE
from metempsychosis.effects import fx_bitcrush, fx_downsample
from metempsychosis.file import read_wav, write_wav
from metempsychosis.oscillators import osc_sine
from metempsychosis.utils import ensure_dir, frequency_to_samples

if __name__ == "__main__":
    ensure_dir((path:= "export/degrade"))
    num_samples = frequency_to_samples(C_TUNING)

    # bitcrush sine waves:
    write_wav(
        path + "/sine1bit.wav",
        fx_bitcrush(osc_sine(C_TUNING, num_samples), 1)
    )
    write_wav(
        path + "/sine2bit.wav",
        fx_bitcrush(osc_sine(C_TUNING, num_samples), 2)
    )
    write_wav(
        path + "/sine3bit.wav",
        fx_bitcrush(osc_sine(C_TUNING, num_samples), 3)
    )
    write_wav(
        path + "/sine4bit.wav",
        fx_bitcrush(osc_sine(C_TUNING, num_samples), 4)
    )

    # bitcrush pcm sample
    write_wav(
        path + "/pcm2bit.wav",
        fx_bitcrush(read_wav("data/speech.wav"), 2)
    )

    # downsample pcm samples
    write_wav(
        path + "/pcmdownsamplespeech.wav",
        fx_downsample(read_wav("data/speech.wav"), SAMPLE_RATE // 16)
    )
    write_wav(
        path + "/pcmdownsampleping.wav",
        fx_downsample(read_wav("data/ping.wav"), SAMPLE_RATE // 24)
    )
