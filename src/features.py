import librosa

import numpy as np

from config import N_MFCC, MAX_LENGTH


def extract_features(audio):

    mfcc = librosa.feature.mfcc(

        y=audio,

        sr=22050,

        n_mfcc=N_MFCC

    )

    if mfcc.shape[1] < MAX_LENGTH:

        pad_width = MAX_LENGTH - mfcc.shape[1]

        mfcc = np.pad(

            mfcc,

            pad_width=((0, 0), (0, pad_width)),

            mode="constant"

        )

    else:

        mfcc = mfcc[:, :MAX_LENGTH]

    return mfcc
