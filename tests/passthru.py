"""
tests/passthru.py
reads and writes a file without effects
Nine 2025.08.28
GPLv3+
"""
# system imports
from datetime import datetime
# package imports
from metempsychosis.file import read_wav, write_wav
from metempsychosis.utils import ensure_dir

if __name__ == "__main__":
    ensure_dir((path:= "export/tests"))

    # debug passthru
    start = datetime.now()
    write_wav(
        path + "/passthru.wav",
        read_wav("data/speech.wav")
    )
    print(f'passthru time: {datetime.now() - start}')
