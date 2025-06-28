import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3
import pyautogui
import winsound
import os
from datetime import datetime

# Text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    print("🔊", text)
    engine.say(text)
    engine.runAndWait()

# Save folder
save_folder = os.path.join(os.path.expanduser("~"), "Pictures", "VoiceScreenshots")
os.makedirs(save_folder, exist_ok=True)

recognizer = sr.Recognizer()

def record_voice(filename="temp.wav", duration=5):
    samplerate = 44100
    try:
        print("🎤 Listening...")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()
        sf.write(filename, recording, samplerate)
        return filename
    except Exception as e:
        print("❌ Mic error:", e)
        speak("Microphone not working")
        return None

def listen_and_act():
    audio_file = record_voice()
    if audio_file is None:
        return True

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            try:
                command = recognizer.recognize_google(audio_data).lower()
                print("✅ You said:", command)

                if "screenshot" in command:
                    filename = f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
                    path = os.path.join(save_folder, filename)
                    pyautogui.screenshot(path)
                    winsound.PlaySound("camera.wav", winsound.SND_FILENAME)
                    speak("Screenshot taken and saved.")
                    print("📸 Saved at:", path)

                    # ✅ Show the screenshot preview (foreground)
                    os.startfile(path)

                elif "stop" in command:
                    speak("Program stopped.")
                    print("🛑 Stopped.")
                    return False

                else:
                    speak("Command not recognized.")

            except sr.UnknownValueError:
                speak("Sorry, I didn't understand.")
            except sr.RequestError as e:
                speak("Speech recognition error.")
                print("❌ Speech API error:", e)
    except Exception as e:
        speak("Audio error.")
        print("❌ Audio error:", e)
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)
    return True

# Loop
while True:
    if not listen_and_act():
        break