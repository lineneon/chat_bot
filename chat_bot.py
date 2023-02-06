import telebot
import openai

bot = telebot.TeleBot("")
openai.api_key = ""

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ask me something dude")

@bot.message_handler(func=lambda message: True)
def answer_question(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Answer the following question: " + message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].get("text")
    
    bot.reply_to(message, response)

bot.polling()
