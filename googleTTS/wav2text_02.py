from google.cloud import speech

client = speech.SpeechClient()
audio = speech.types.RecognitionAudio(
    uri='D:\\python_workspace\\nytacotron\\data\\yuyin\\test1.flac')
config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code='en-US',
    sample_rate_hertz=44100)
results = client.recognize(config=config, audio=audio)
for result in results:
    for alternative in result.alternatives:
        print('=' * 20)
        print('transcript: ' + alternative.transcript)
        print('confidence: ' + str(alternative.confidence))
# ====================
# transcript: Hello, this is a test
# confidence: 0.81
# ====================
# transcript: Hello, this is one test
