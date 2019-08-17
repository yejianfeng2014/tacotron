from gtts import gTTS

import  time

time_time1 = time.time()

text = "this is a test"

tts = gTTS(text=text, lang="en")
tts.save("test1.mp3")
# AudioSegment.from_mp3(filename_mp3).export(filename_wav, format="wav")


print(time.time()- time_time1)



# from gtts import gTTS
import os
tts = gTTS(text='您好，您吃早饭了吗？需要我给你推荐些吃的吗？', lang='zh-tw')
tts.save("hello.mp3")
# os.system("mpg321 hello.mp3")


print(time.time()- time_time1)