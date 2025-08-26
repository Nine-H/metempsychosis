"""
file.py
functions to read and write files
Nine 2025.04.09
GPLv3+
"""
# system imports
from collections.abc import Iterable
from wave import open
# local imports
from .constants import BIT_DEPTH, SAMPLE_RATE


def _range(d: int = BIT_DEPTH) -> tuple[float, float]:
    """
    get the minimum and maximum value of a sample
    """
    return pow(-2, d - 1), pow(2, d - 1) - 1


def pcm(s: float) -> bytes:
    """
    converts samples to correct format for pcm wave
    :param s: a floating point sample
    """
    _, m = _range()
    s = int(s * m)
    return s.to_bytes(
        length=BIT_DEPTH//8,
        byteorder="little",
        signed=True
    )


def read_wav(path: str) -> Iterable[float]:
    """
    reads a sample file
    :param path: path to file
    """
    with open(path, "rb") as wav:
        # get metadata
        # FIXME: resampling would be useful
        c, w, _, n, _, _ = wav.getparams()
        # get bit depth in bytes by dividing width in bytes by channels
        d = w // c
        # FIXME: signed/unsigned?
        _, m = _range(d * 8)
        for _ in range(n):
            frame = wav.readframes(1)
            yield int(frame[:d]) / m


def write_wav(path: str, sample: Iterable[float]) -> None:
    """
    writes a sample to a file
    :param path: path to file
    """
    data = bytes()
    for s in sample:
        data += pcm(s)

    with open(path, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(BIT_DEPTH // 8)
        file.setframerate(SAMPLE_RATE)
        file.writeframes(data)
