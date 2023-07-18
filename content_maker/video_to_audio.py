from pydub import AudioSegment
from pydub.silence import split_on_silence

sound_file = AudioSegment.from_wav("input/alphabet.wav")
audio_chunks = split_on_silence(sound_file, min_silence_len=100, silence_thresh=-20)

for i, chunk in enumerate(audio_chunks):
    out_file = "output/chunk{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")