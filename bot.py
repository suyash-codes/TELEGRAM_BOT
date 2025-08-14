!pip install groq python-dotenv aiogram
import asyncio
import os
import logging
import sys
from dotenv import load_dotenv
from groq import AsyncGroq  
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ChatAction
# from google.colab import userdata # Import userdata

load_dotenv()

BOT_TOKEN = userdata.get("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = userdata.get("GROQ_API_KEY")

if not BOT_TOKEN or not GROQ_API_KEY:
    raise ValueError("Missing TELEGRAM_BOT_TOKEN or GROQ_API_KEY. Please add them to Colab Secrets Manager.")

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

groq_client = AsyncGroq(api_key=GROQ_API_KEY)

user_contexts = {}

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.reply("Hello, I am a bot created by Suyash.\nHow may I assist you today?")

@dp.message(Command("help"))
async def help_handler(message: types.Message):
    help_text = """
Hello! Here’s a list of commands you can try:  
/start – Begin the conversation  
/help – View help information  
/clear – Erase your chat history  
"""
    await message.reply(help_text)

@dp.message(Command("clear"))
async def clear_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id in user_contexts:
        del user_contexts[user_id]
    await message.reply("🧹 Your chat history has been cleared.")

@dp.message()
async def chat_handler(message: types.Message):
    user_id = message.from_user.id
    user_input = message.text

    await bot.send_chat_action(chat_id=user_id, action=ChatAction.TYPING)

    if user_id not in user_contexts:
        user_contexts[user_id] = [{"role": "system", "content": "You are a helpful assistant."}]

    user_contexts[user_id].append({"role": "user", "content": user_input})

    try:
        chat_completion = await groq_client.chat.completions.create(
            messages=user_contexts[user_id],
            model="llama3-8b-8192", 
        )

        bot_reply = chat_completion.choices[0].message.content

        user_contexts[user_id].append({"role": "assistant", "content": bot_reply})

        await message.reply(bot_reply)

    except Exception as e:
        logging.error(f"Error processing message for user {user_id}: {e}")
        await message.reply("⚠️ An error occurred while talking to Groq.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await main() 
