---

# 🤖 Async Telegram AI Bot (Aiogram + Groq AI)

This is an async Telegram bot built using **aiogram** and **Groq AI**. It supports command-based interaction, per-user chat memory, and runs locally using Python’s `asyncio` framework.

---

## 🚀 Features

* `/start`, `/help`, `/clear` commands
* Context-aware conversations using **Groq AI API**
* Separate memory per user for personalized chats
* Asynchronous & scalable structure
* `.env` file for secure secret management

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Aiogram** (Telegram Bot API)
* **Groq AI API**
* **python-dotenv** for environment variables

---

## 🧠 Memory (Context Handling)

Each user has a dedicated list of messages (chat history), ensuring smooth, back-and-forth conversations with AI.

Example:

```json
[
  {"role": "user", "content": "Hi"},
  {"role": "assistant", "content": "Hello, how can I assist you?"}
]
```

---

## 📁 Project Structure

```
.
├── bot.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔐 .env Setup

Create a `.env` file in the root directory and add your keys:

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  
GROQ_API_KEY=your_groq_api_key_here  
```

---

## 📦 Installation

**1. Clone This Repo**

```bash
git clone https://github.com/suyash-codes/TELEGRAM_BOT
cd Telegram_Bot
```

**2. Create a Virtual Environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux  
venv\Scripts\activate           # Windows  
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Bot**

```bash
python bot.py
```

---

## ✅ Supported Commands

| Command | Description                  |
| ------- | ---------------------------- |
| /start  | Start the conversation       |
| /help   | Show available commands      |
| /clear  | Clear chat memory (per user) |

---

## 🧠 Sample Conversation

**User:** /start
**Bot:** Hello, I’m a bot created by Suyash. How may I assist you today?

**User:** What's the capital of Japan?
**Bot:** The capital of Japan is Tokyo.

---

## 🧩 Future Improvements

* Add Whisper (voice input)
* Deploy to Render/Railway
* Add inline buttons with AI presets
* Implement rate limiting or usage caps
* Persist context with Redis or SQLite

---

## 👤 Author

Built by **Suyash Singh Gusain** ❤
🔗 [LinkedIn](https://www.linkedin.com/in/suyashsinghgusain)
🌐 [GitHub](https://github.com/suyash-codes)

---

## 📎 requirements.txt

```
aiogram  
groq  
python-dotenv  
```
