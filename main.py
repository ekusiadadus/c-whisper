import openai

file = open("./data/test.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription)
