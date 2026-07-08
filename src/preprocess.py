import librosa

import numpy as np

from config import SAMPLE_RATE


def load_audio(file_path):

    signal, sr = librosa.load(

        file_path,

        sr=SAMPLE_RATE

    )

    return signal


def normalize_audio(signal):

    signal = signal / np.max(np.abs(signal))

    return signal
