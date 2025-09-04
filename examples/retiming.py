"""
examples/retiming.py
faster and slower
Nine 2025.09.03
GPLv3+
"""
# package imports
from metempsychosis.effects import fx_reverse, fx_speed, fx_timestretch
from metempsychosis.file import read_wav, write_wav
from metempsychosis.utils import ensure_dir

if __name__ == "__main__":
    ensure_dir((path:= "export/retiming"))

    # reverse
    write_wav(
        path + "/reverse.wav",
        fx_reverse(read_wav("data/ping.wav"))
    )

    # speed    
    write_wav(
        path + "/pitchdouble.wav",
        fx_speed(read_wav("data/ping.wav"), 2.0)
    )
    write_wav(
        path + "/pitchhalf.wav",
        fx_speed(read_wav("data/ping.wav"), 0.5)
    )

    # timestretch
    write_wav(
        path + "/speeddouble.wav",
        fx_timestretch(read_wav("data/ping.wav"), 2.0)
    )
    write_wav(
        path + "/speedhalf.wav",
        fx_timestretch(read_wav("data/ping.wav"), 0.5)
    )
