"""
examples/filters.py
generates noise samples with various filters applied
Nine 2025.04.15
GPLv3+
"""
# library imports
from metempsychosis.effects import fx_allpass, fx_clip, fx_lowpass, fx_highpass  # fx_bandpass
from metempsychosis.file import write_wav
from metempsychosis.oscillators import osc_noise
from metempsychosis.utils import ensure_dir, duration_to_samples

if __name__ == "__main__":
    # filter examples
    ensure_dir((path:= "export/filters"))

    # compare like for like
    noise = list(osc_noise(duration_to_samples(1)))

    # lowpass cutoff test
    write_wav(path + "/lowpass_c20000.wav", fx_clip(fx_lowpass(noise, 20_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c10000.wav", fx_clip(fx_lowpass(noise, 10_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c5000.wav", fx_clip(fx_lowpass(noise, 5_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c2000.wav", fx_clip(fx_lowpass(noise, 2_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c1000.wav", fx_clip(fx_lowpass(noise, 1_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c500.wav", fx_clip(fx_lowpass(noise, 500.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c100.wav", fx_clip(fx_lowpass(noise, 100.0, 0.0, 0.0), 1.0))
    write_wav(path + "/lowpass_c50.wav", fx_clip(fx_lowpass(noise, 50.0, 0.0, 0.0), 1.0))

    # highpass cutoff test
    write_wav(path + "/highpass_c20000.wav", fx_clip(fx_highpass(noise, 20_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c10000.wav", fx_clip(fx_highpass(noise, 10_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c5000.wav", fx_clip(fx_highpass(noise, 5_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c2000.wav", fx_clip(fx_highpass(noise, 2_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c1000.wav", fx_clip(fx_highpass(noise, 1_000.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c500.wav", fx_clip(fx_highpass(noise, 500.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c100.wav", fx_clip(fx_highpass(noise, 100.0, 0.0, 0.0), 1.0))
    write_wav(path + "/highpass_c50.wav", fx_clip(fx_highpass(noise, 50.0, 0.0, 0.0), 1.0))
