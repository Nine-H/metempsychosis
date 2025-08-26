# metempsychosis

synthesizer module for python focused on offline rendering to .wav files.
procedurally generate samples and wavetables with python.
low level to support various retro samplers and trackers.
definitely bug free I swear.

> WARNING: this module is licensed GPL3+, which has some implications for derivitive works

# what?

- a toolkit for procedurally generating samples
- to compliment LittleGPTracker
- (and hopefully many different software and hardware trackers, samplers, and synths)
- programmed in pure python using the builtin modules for extreme portability
- using python generators and streaming to be as fast as possible
- to procedurally generate samples to emulate classic instruments and effects
- to assist in the design of new instruments, algorithms, and effects

# features

> WARNING: this is very alpha software, functionality and interfaces will be subject to change

- write samples to wave
- oscillators
    - noise
    - pwm
    - basic waves
- effects
    - clipping
    - xfade
    - low, high, allpass filters
- macros
    - wavetable_xfade: create a wavetable that transitions between two waves
    - wavetable_pwm: create a wavetable that modulates pwm
- modulation
    - simple envelopes

# future goals

- attenuation and envelopes: mandatory for moving past raw wave generation for piggy tracker
- sample loading: I want to be able to incorporate pre-recorded samples in scripts
- lsdj synth macro: create a macro that takes all the parameters of the lsdj wav synth but exports 16 bit pcm
- super/hyper saws: an iconic effect
- fm: I want to support arbitrary numbers of operators and all possible algorithms
- granular sampling: I want to figure out what needs to be done to support granular style effects in LittleGPTracker
- mobile: I want to create a sample studio app for chinese handhelds
- realtime: I want to expiriment with realtime software synthesis on pc class hardware
- formats: create scripts that export directly to instrument and sample formats for different hardware/software

# research

- fm presets to steal: <https://github.com/corthax/mdtracker/blob/main/src/MDT_Presets.c>
- defense mechanism's intense lsdj tech: <https://defensemech.com/intense-tech/>
- not a bad explanation of filters: <https://www.youtube.com/watch?v=I8_E1ppC3-Q>

# env vars

- setting these environment variables before running scripts let you change the configuration

env var       | default | description
--------------|---------|--------------------------------------------------------
`SAMPLE_RATE` | 44100   | sample rate used for exported .wav files and for tuning
`BIT_DEPTH`   | 16      | bit depth of exported wav files
`C_TUNING`    | 261.63  | frequency of middle C

# example scripts

- `basicwaves.py`: hello metempsychosis, outputs single cycle basic waves at cd quality
- `filters.py`: test script for filters
- `fm.py`: TBD, render general midi fm presets to samples
- `lofi.py`: renders wavetables with a configurable number of cycles and samples, defaults both to 16
- `lsdj_synth.py`: WIP, procedurally generates wavetables that simulate the lsdj wav synth
- `oneshots.py`: TBD, testbed for modulation, envelopes, sound design
- `wavetables.py`: renders cd quality wavetables crossfading between different basic waves

# gear/software

> INFO: not a support list, gear that I'm interested in and may/may not have

- Arturia microfreak
- Dirtywave M8
- KoalaSampler
- MilkyTracker
- monome norns
- nanoloop mobile
- picotracker
- soundfonts
- sunvox
