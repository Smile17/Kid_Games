# Import the required module for text
# to speech conversion
import codecs

from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
prefix = 'ukr_alpha17'
words = []
f = 'input.txt'
with codecs.open(f, encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        words.append(line.replace('\n', '').replace('\r', ''))
words = [word.lower() for word in words]
print(words)

# Language in which you want to convert
language = 'uk'

for i, word in enumerate(words):
    obj = gTTS(text=word, lang=language, slow=False)
    f = str(i + 1)
    if i + 1 < 10:
        f = "0" + f
    obj.save("audio/" + prefix + "_" + f + ".m4a")

# Playing the converted file
#os.system("welcome.mp3")

