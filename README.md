# 🎤 AI Voice & Text Chatbot

A simple AI-powered chatbot that can take voice input, process it using an AI model (Groq API or OpenAI API), and provide a spoken response using text-to-speech (TTS).

## 🚀 Features

Speech-to-Text: Converts user speech into text.

AI Response Generation: Uses an AI model to generate responses.

Text-to-Speech: Speaks the AI-generated response aloud.

Continuous Conversation: Runs in a loop until the user says "exit".

### 🛠️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-repo/chatbot.git
cd chatbot

2️⃣ Install Dependencies

pip install speechrecognition pyttsx3 openai

3️⃣ Set Up API Key (Groq or OpenAI)

Create a .env file and add your API key:

OPENAI_API_KEY=your_api_key_here

📜 Usage

Run the chatbot

python main.py

### Example Interaction

🎤 Listening...
🗣 You: Hello, how are you?
🤖 Chatbot: I am fine, how can I assist you?
(Chatbot speaks the response)

Exit the chatbot

Say "exit" to stop the conversation.



### 📌 Future Improvements

✅ Multilingual support✅ UI with Tkinter or Flask✅ Integration with a database
