import livekit
import groq
import speech_recognition as sr
import pyttsx3
from livekit import rtc

# LiveKit API Setup
LIVEKIT_HOST = "wss://chatbot-project-uf8m6m3f.livekit.cloud"
LIVEKIT_API_KEY = "APIL5eP4M7tXaZX"
LIVEKIT_API_SECRET = "IEk1Wa1PYr6tfJm9wXAMupG7DylWMPMxPQfXqfoI2yUB"

# OpenAI API Setup
groq_api_key = "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"
client = groq.Groq(api_key=groq_api_key)
# Speech Recognition
recognizer = sr.Recognizer()

# Text-to-Speech (TTS)
tts_engine = pyttsx3.init()

# LiveKit Room Connect

room = rtc.Room()
room.connect(LIVEKIT_HOST, LIVEKIT_API_KEY, LIVEKIT_API_SECRET)

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣 You: {text}")
        return text
    except sr.UnknownValueError:
        print(" Could not understand audio")
        return None
    except sr.RequestError:
        print(" Speech Recognition Error")
        return None

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def chat_with_groq(prompt):
    """
    Sends user input to Groq API and returns the chatbot's response.
    """
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except groq.BadRequestError as e:
        print(f" Error: {e}")
        return "I am currently facing an issue. Please try again later."

while True:
    user_input = listen()
    if user_input:
        response = chat_with_groq(user_input)
        print("🤖 Bot:", response)
        speak(response)