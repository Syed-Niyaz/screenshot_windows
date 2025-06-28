# 🎙️ Voice-Controlled Screenshot Tool

A Python-based voice assistant that listens for simple voice commands like *"screenshot"* and *"stop"* to capture and preview screenshots — hands-free and efficient.

---

## 📺 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/sh_RIjSri-c/0.jpg)](https://youtu.be/sh_RIjSri-c)

---

## 📌 Features

- 🗣️ Voice-activated commands:
  - Say *"screenshot"* to take a full-screen screenshot
  - Say *"stop"* to exit the application
- 🖼️ Screenshots saved automatically with a timestamped filename
- 🔊 Camera shutter sound played on each capture
- 👁️ Screenshot preview opens immediately after capture
- 🗨️ Real-time voice feedback like "Screenshot taken" using text-to-speech
- 🎧 Continuous microphone listening without interrupting your workflow

---

## 🚀 Tech Stack

- Python 3.x  
- speech_recognition  
- pyttsx3  
- pyautogui  
- sounddevice  
- soundfile  
- winsound (Windows built-in)

---

## 📷 How It Works

1. The program continuously listens through your microphone.
2. When it hears the word *"screenshot"*, it:
   - Takes a screenshot using pyautogui
   - Plays a shutter sound using winsound
   - Opens the image using your system’s default viewer
   - Gives a voice confirmation using pyttsx3
3. On hearing *"stop"*, the program exits safely.

---

## 📂 Folder Structure
