import subprocess
voice = 'en-IE-EmilyNeural'
def speak(data):
    voice = 'en-CA-LiamNeural'
    filename = "data.wav"

    # Split the input text into chunks
    chunks = data.split()
    chunk_size = 1000
    chunks = [chunks[i:i + chunk_size]
              for i in range(0, len(chunks), chunk_size)]

    # Convert and write each chunk to file
    for chunk in chunks:
        text = ' '.join(chunk)
        command = f'edge-tts --voice "{voice}" --text "{text}"  --rate=+25%  --write-media "{filename}"'
        subprocess.run(command, shell=True)

    return True
speak("hello")