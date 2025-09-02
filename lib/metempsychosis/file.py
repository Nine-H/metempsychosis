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
    :param d: bit depth as number of bits
    """
    return pow(-2, d - 1), pow(2, d - 1) - 1


def read_wav(path: str) -> Iterable[float]:
    """
    reads a sample file
    :param path: path to file
    """
    with open(path, "rb") as wav:
        # get metadata
        # FIXME: resampling would be useful
        nc = wav.getnchannels()
        n = wav.getnframes()
        sw = wav.getsampwidth()
        bd = sw // nc 
        _, m = _range(bd * 8)
        for _ in range(n):
            # FIXME: breaks when there are multiple channels
            frame = wav.readframes(1)
            yield int.from_bytes(frame, byteorder="little", signed=True) / m


def write_wav(path: str, sample: Iterable[float]) -> None:
    """
    writes a sample to a file
    :param path: path to file
    :param sample: sample data to write
    """
    _, m = _range()
    with open(path, "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(BIT_DEPTH // 8)
        file.setframerate(SAMPLE_RATE)
        for s in sample:
            file.writeframes(
                int(s * m).to_bytes(
                    length=BIT_DEPTH//8,
                    byteorder="little",
                    signed=True
                )
            )
