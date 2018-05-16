import telebot
from telebot import TeleBot
from telebot import types

token = "516120741:AAFnJERmJRN_YoUMq6sl32u5ke1IFTrXHJ8"
bot: TeleBot = telebot.TeleBot(token)
bot.send_message('471090279',"ман корба тайёр")
@bot.message_handler(commands=['/start'])
def inline(message):
    key =types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Заработать миллион", callback_data="Молодец ты выиграл мииллион")
    but_2 = types.InlineKeyboardButton(text="Потратить миллион", callback_data="вы успешно потратили миллиард долларов")
    key .add(but_1,but_2)
    bot.send_message(message.chat.id, "Первый вопрос: ту чиними соқми, хотя ин дута савол буд", reply_markup=key)










if __name__ == "__main__":


 bot.polling(none_stop=True)