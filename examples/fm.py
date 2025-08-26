"""
examples/fm.py
generate samples using fm presets
Nine 2025.04.20
GPLv3+
"""
# library imports
from metempsychosis.file import write_wav

if __name__ == "__main__":
    with open("examples/fmpresets.csv") as presetfile:
        presets = presetfile.readlines()

    for line in presets[1:]:
        write_wav()
