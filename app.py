import urbandictionary as ud
import random
import telebot
import os

bot_key = os.getenv("BOT_KEY")
chat_id = "-1001378894764"

bot = telebot.TeleBot(bot_key)


def get_random_definition():
    random_definitions = ud.random()
    one_definition = random.choice(random_definitions)
    formatted_text = one_definition.definition.replace("[", "")
    formatted_text = formatted_text.replace("]", "")
    return f"{one_definition.word.upper()}: {formatted_text}"


def send_message(chat_id, text):
    bot.send_message(chat_id, text)


def app():
    send_message(chat_id=chat_id, text=get_random_definition())


if __name__ == '__main__':
    app()
