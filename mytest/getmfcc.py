# 获取音频的mfcc

import scipy.io.wavfile as wav
from python_speech_features import mfcc

fs, audio = wav.read("../samples/1.wav")
# fs 是采样频率



feature_mfcc = mfcc(audio, samplerate=fs)
print(feature_mfcc)
print(feature_mfcc.shape)


fs2, audio2 = wav.read("../samples/2.wav")


feature_mfcc2 = mfcc(audio2, samplerate=fs2)
print(feature_mfcc2)
print(feature_mfcc2.shape)




fs3, audio3 = wav.read("../samples/3.wav")


feature_mfcc3 = mfcc(audio3, samplerate=fs3)
print(feature_mfcc3)
print(feature_mfcc3.shape)
