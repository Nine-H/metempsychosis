"""
constants.py
config and constants
Nine 2025.04.09
GPLv3+
"""
# system imports
from os import getenv

SAMPLE_RATE = int(getenv("SAMPLE_RATE") or 44100) 
BIT_DEPTH = int(getenv("BIT_DEPTH") or 16)
A_TUNING = float(getenv("A_TUNING") or 440)
C_TUNING = float(getenv("C_TUNING") or 261.63)
