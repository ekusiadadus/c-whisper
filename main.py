import openai

OPENAI_API_KEY = "YOUR_API_KEY"

file = open("./data/test.mp3", "rb")
transcription = openai.Audio.transcribe("whisper-1", file, api_key=OPENAI_API_KEY)

print(transcription)
