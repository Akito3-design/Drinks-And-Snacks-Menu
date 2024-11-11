# import telebot
# from telebot import types
#
# # Замените на ваш токен API бота
# bot = telebot.TeleBot("7322740602:AAHJXeL_JZfomMtTU8U53-yXQ8I_nXr2boQ")
#
# # Меню "Напитки"
# def menu_napitki(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_alko = types.KeyboardButton("Алкогольные")
#   button_bezalko = types.KeyboardButton("Безалкогольные")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_alko, button_bezalko, button_back)
#   bot.send_message(message.chat.id, "Выберите категорию напитков:", reply_markup=keyboard)
#
# # Меню "Закуски"
# def menu_zakuski(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_orehi = types.KeyboardButton("Орешки")
#   button_tortiki = types.KeyboardButton("Тортики")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_orehi, button_tortiki, button_back)
#   bot.send_message(message.chat.id, "Выберите закуски:", reply_markup=keyboard)
#
# # Обработчик команд "/start"
# @bot.message_handler(commands=['start'])
# def start_message(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_napitki = types.KeyboardButton("Напитки")
#   button_zakuski = types.KeyboardButton("Закуски")
#   keyboard.add(button_napitki, button_zakuski)
#   bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=keyboard)
#
# # Обработчик текстовых сообщений
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#   if message.text == "Напитки":
#     menu_napitki(message)
#   elif message.text == "Закуски":
#     menu_zakuski(message)
#   elif message.text == "Алкогольные":
#     bot.send_message(message.chat.id, "Вы выбрали Алкогольные напитки")
#   elif message.text == "Безалкогольные":
#     bot.send_message(message.chat.id, "Вы выбрали Безалкогольные напитки")
#   elif message.text == "Орешки":
#     bot.send_message(message.chat.id, "Вы выбрали Орешки")
#   elif message.text == "Тортики":
#     bot.send_message(message.chat.id, "Вы выбрали Тортики")
#   elif message.text == "Назад":
#     start_message(message) # Вернуться в главное меню
#   else:
#     bot.send_message(message.chat.id, "Неверный выбор.")
#
# # Запускаем бота
# bot.polling(non_stop=True)

import telebot
from telebot import types

# Замените на ваш токен API бота
bot = telebot.TeleBot("7322740602:AAHJXeL_JZfomMtTU8U53-yXQ8I_nXr2boQ")

# Меню "Напитки"
def menu_napitki(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_alko = types.KeyboardButton("Алкогольные")
  button_bezalko = types.KeyboardButton("Безалкогольные")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_alko, button_bezalko, button_back)
  bot.send_message(message.chat.id, "Выберите категорию напитков:", reply_markup=keyboard)

# Меню "Закуски"
def menu_zakuski(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_orehi = types.KeyboardButton("Орешки")
  button_tortiki = types.KeyboardButton("Тортики")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_orehi, button_tortiki, button_back)
  bot.send_message(message.chat.id, "Выберите закуски:", reply_markup=keyboard)

# Меню "Алкогольные напитки"
def menu_alko(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_pivo = types.KeyboardButton("Пиво")
  button_vodka = types.KeyboardButton("Водка")
  button_vino = types.KeyboardButton("Вино")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_pivo, button_vodka, button_vino, button_back)
  bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)

# Меню "Безалкогольные напитки"
def menu_bezalko(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_voda = types.KeyboardButton("Вода")
  button_limonad = types.KeyboardButton("Лимонад")
  button_sok = types.KeyboardButton("Сок")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_voda, button_limonad, button_sok, button_back)
  bot.send_message(message.chat.id, "Выберите безалкогольный напиток:", reply_markup=keyboard)

# Меню "Орешки"
def menu_orehi(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_syrnye = types.KeyboardButton("Сырные")
  button_bekon = types.KeyboardButton("С беконом")
  button_vasabi = types.KeyboardButton("Васаби")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_syrnye, button_bekon, button_vasabi, button_back)
  bot.send_message(message.chat.id, "Выберите орешки:", reply_markup=keyboard)

# Меню "Тортики"
def menu_tortiki(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_shokolad = types.KeyboardButton("Шоколадный")
  button_vozduшный = types.KeyboardButton("Воздушный")
  button_karamel = types.KeyboardButton("Карамельный")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_shokolad, button_vozduшный, button_karamel, button_back)
  bot.send_message(message.chat.id, "Выберите тортик:", reply_markup=keyboard)

  # Обработчик команд "/start"


@bot.message_handler(commands=['start'])
def start_message(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_napitki = types.KeyboardButton("Напитки")
  button_zakuski = types.KeyboardButton("Закуски")
  keyboard.add(button_napitki, button_zakuski)
  bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=keyboard)


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
  if message.text == "Напитки":
    menu_napitki(message)
  elif message.text == "Закуски":
    menu_zakuski(message)
  elif message.text == "Алкогольные":
    menu_alko(message)
  elif message.text == "Безалкогольные":
    menu_bezalko(message)
  elif message.text == "Орешки":
    menu_orehi(message)
  elif message.text == "Тортики":
    menu_tortiki(message)
  elif message.text == "Пиво":
    bot.send_message(message.chat.id, "Вы выбрали Пиво")
  elif message.text == "Водка":
    bot.send_message(message.chat.id, "Вы выбрали Водку")
  elif message.text == "Вино":
    bot.send_message(message.chat.id, "Вы выбрали Вино")
  elif message.text == "Вода":
    bot.send_message(message.chat.id, "Вы выбрали Воду")
  elif message.text == "Лимонад":
    bot.send_message(message.chat.id, "Вы выбрали Лимонад")
  elif message.text == "Сок":
    bot.send_message(message.chat.id, "Вы выбрали Сок")
  elif message.text == "Сырные":
    bot.send_message(message.chat.id, "Вы выбрали Сырные орешки")
  elif message.text == "С беконом":
    bot.send_message(message.chat.id, "Вы выбрали Орешки с беконом")
  elif message.text == "Васаби":
    bot.send_message(message.chat.id, "Вы выбрали Орешки с васаби")
  elif message.text == "Шоколадный":
    bot.send_message(message.chat.id, "Вы выбрали Шоколадный тортик")
  elif message.text == "Воздушный":
    bot.send_message(message.chat.id, "Вы выбрали Воздушный тортик")
  elif message.text == "Карамельный":
    bot.send_message(message.chat.id, "Вы выбрали Карамельный тортик")
  elif message.text == "Назад":
    start_message(message)  # Вернуться в главное меню
  else:
    bot.send_message(message.chat.id, "Неверный выбор.")


# Запускаем бота
bot.polling(non_stop=True)

