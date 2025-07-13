import pyaudio
import wave
from vosk import Model, KaldiRecognizer
import os
import json

# Audio recording configuration
SAMPLE_RATE = 16000         # 16 kHz for Vosk compatibility
CHANNELS = 1                # Mono audio
SAMPLE_WIDTH = 2            # 16-bit samples
FRAME_SIZE = 1024
RECORD_SECONDS = 5
WAV_OUTPUT = "temp.wav"

# Path to the new Vosk large model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../../models/vosk-model-en-us")

def record_audio(filename=WAV_OUTPUT, duration=RECORD_SECONDS):
    """Records audio and saves it to a WAV file."""
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=FRAME_SIZE
    )

    print(f"🎙 Recording for {duration} seconds...")
    frames = []

    for _ in range(int(SAMPLE_RATE / FRAME_SIZE * duration)):
        data = stream.read(FRAME_SIZE, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    pa.terminate()

    # Save to .wav
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_WIDTH)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"✅ Saved audio to {filename}")

def transcribe_audio(filename=WAV_OUTPUT):
    """Transcribes a WAV file using Vosk."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"❌ Vosk model not found at {MODEL_PATH}")

    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    wf = wave.open(filename, 'rb')
    if wf.getnchannels() != CHANNELS or wf.getframerate() != SAMPLE_RATE or wf.getsampwidth() != SAMPLE_WIDTH:
        raise ValueError("❌ Invalid WAV format: Must be 16kHz, mono, 16-bit.")

    print("🧠 Transcribing...")

    transcription = ""
    while True:
        data = wf.readframes(2048)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcription += result.get("text", "") + " "

    # Final result
    final_result = json.loads(recognizer.FinalResult())
    transcription += final_result.get("text", "")
    wf.close()

    return transcription.strip()

if __name__ == "__main__":
    record_audio()
    text = transcribe_audio()
    print("📝 Transcription:", text)
