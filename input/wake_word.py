import pvporcupine
import pyaudio
import struct
import os

# Replace this with your actual access key from Picovoice Console
ACCESS_KEY = "uMBcDqce40zeZH0N6nEvddo2FxF22iWBVSLpiQujWPdn4W6DEmDpJw=="

# Path to your .ppn file
KEYWORD_PATH = "C:/harvis-assistant/HARVIS/models/porcupine/harveys_en_windows.ppn"

def listen_for_wake_word():
    print("Initializing Porcupine wake word engine...")

    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[KEYWORD_PATH]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("Listening for 'harveys'...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)

            if result >= 0:
                print("Wake word 'harveys' detected!")
                break  # You can call your speech-to-text or main function here

    except KeyboardInterrupt:
        print("Interrupted by user")

    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
        print("Resources released.")

if __name__ == "__main__":
    listen_for_wake_word()
