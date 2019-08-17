# 异步识别

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

client = speech_v1.SpeechClient()

encoding = enums.RecognitionConfig.AudioEncoding.FLAC
# encoding = enums.RecognitionConfig.AudioEncoding.
sample_rate_hertz = 44100
language_code = 'en-US'
config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
uri = 'D:\\python_workspace\\nytacotron\\data\\yuyin\\test1.flac'
audio = {'uri': uri}

response = client.recognize(config, audio)

print(response)