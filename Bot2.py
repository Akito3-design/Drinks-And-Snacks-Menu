# import telebot
# from telebot import types
#
# # Замените на ваш токен API бота
# bot = telebot.TeleBot("7322740602:AAHJXeL_JZfomMtTU8U53-yXQ8I_nXr2boQ")
#
# # Словарь с товарами и ценами (расширенный ассортимент)
# products = {
#   # Напитки
#   "Пиво": 150, "Водка": 300,
#   "Вино красное": 250, "Вино белое": 250,
#   "Вино розовое": 270, "Вода": 50,
#   "Лимонад": 80, "Сок апельсиновый": 100,
#   "Сок яблочный": 100, "Кола": 90,
#   "Спрайт": 90, "Фанта": 90,
#   # Закуски
#   "Сырные орешки": 150,
#   "Орешки с беконом": 180, "Орешки с васаби": 180,
#   "Чипсы": 80, "Сухарики": 70,
#   "Крекеры": 90, "Оливье": 150,
#   "Сельдь под шубой": 170,
#   # Тортики
#   "Шоколадный тортик": 250, "Воздушный тортик": 200,
#   "Карамельный тортик": 220, "Медовик": 230,
#   "Наполеон": 240, "Тирамису": 280
# }
#
# # Словарь для хранения корзины пользователя
# user_carts = {}
#
# # Функция для отображения главного меню
# def start_message(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_napitki = types.KeyboardButton("Напитки")
#   button_zakuski = types.KeyboardButton("Закуски")
#   button_cart = types.KeyboardButton("Корзина")
#   # Кнопка корзины
#   keyboard.add(button_napitki, button_zakuski, button_cart)
#   bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=keyboard)
#
# # Функция для отображения меню "Напитки"
# def menu_napitki(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_alko = types.KeyboardButton("Алкогольные")
#   button_bezalko = types.KeyboardButton("Безалкогольные")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_alko, button_bezalko, button_back)
#   bot.send_message(message.chat.id, "Выберите категорию напитков:", reply_markup=keyboard)
#
# # Функция для отображения меню "Закуски"
# def menu_zakuski(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_orehi = types.KeyboardButton("Орешки")
#   button_tortiki = types.KeyboardButton("Тортики")
#   button_holodnye = types.KeyboardButton("Холодные закуски")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_orehi, button_tortiki, button_holodnye, button_back)
#   bot.send_message(message.chat.id, "Выберите закуски:", reply_markup=keyboard)
#
# # Функция для отображения меню "Алкогольные напитки"
# def menu_alko(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_pivo = types.KeyboardButton("Пиво")
#   button_vodka = types.KeyboardButton("Водка")
#   button_vino_krasnoe = types.KeyboardButton("Вино красное")
#   button_vino_beloe = types.KeyboardButton("Вино белое")
#   button_vino_rozovoe = types.KeyboardButton("Вино розовое")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_pivo, button_vodka, button_vino_krasnoe, button_vino_beloe, button_vino_rozovoe, button_back)
#   bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)
#
# # Функция для отображения меню "Безалкогольные напитки"
# def menu_bezalko(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_voda = types.KeyboardButton("Вода")
#   button_limonad = types.KeyboardButton("Лимонад")
#   button_sok_apelsin = types.KeyboardButton("Сок апельсиновый")
#   button_sok_yabloko = types.KeyboardButton("Сок яблочный")
#   button_kola = types.KeyboardButton("Кола")
#   button_sprite = types.KeyboardButton("Спрайт")
#   button_fanta = types.KeyboardButton("Фанта")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_voda, button_limonad, button_sok_apelsin, button_sok_yabloko, button_kola, button_sprite, button_fanta, button_back)
#   bot.send_message(message.chat.id, "Выберите безалкогольный напиток:", reply_markup=keyboard)
#
# # Функция для отображения меню "Орешки"
# def menu_orehi(message):
#   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#   button_syrnye = types.KeyboardButton("Сырные")
#   button_bekon = types.KeyboardButton("С беконом")
#   button_vasabi = types.KeyboardButton("Васаби")
#   button_back = types.KeyboardButton("Назад")
#   keyboard.add(button_syrnye, button_bekon, button_vasabi, button_back)
#   bot.send_message(message.chat.id, "Выберите орешки:", reply_markup=keyboard)
#
# # ... (остальные функции для меню "Тортики", "Холодные закуски" и т.д.)
#
# # Функция для добавления товара в корзину
# def add_to_cart(message, item):
#   user_id = message.chat.id
#   if user_id not in user_carts:
#     user_carts[user_id] = {}
#   if item in user_carts[user_id]:
#     user_carts[user_id][item] += 1
#   else:
#     user_carts[user_id][item] = 1
#   bot.send_message(message.chat.id, f"{item} добавлен в корзину.")
#
# # Функция для отображения корзины
# def show_cart(message):
#   user_id = message.chat.id
#   if user_id in user_carts and user_carts[user_id]:
#     cart_items = user_carts[user_id]
#     cart_text = "Ваша корзина:\n"
#     total_price = 0
#     for item, quantity in cart_items.items():
#       price = products[item]
#       item_price = price * quantity
#       cart_text += f"{item} x {quantity} = {item_price}\n"
#       total_price += item_price
#     cart_text += f"\nИтого: {total_price}"
#     bot.send_message(message.chat.id, cart_text)
#   else:
#     bot.send_message(message.chat.id, "Ваша корзина пуста.")
#
# # Обработка команд
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#   start_message(message)
#
# @bot.message_handler(func=lambda message: message.text == "Напитки")
# def handle_napitki(message):
#   menu_napitki(message)
#
# @bot.message_handler(func=lambda message: message.text == "Закуски")
# def handle_zakuski(message):
#   menu_zakuski(message)
#
# @bot.message_handler(func=lambda message: message.text == "Корзина")
# def handle_cart(message):
#   show_cart(message)
#
# @bot.message_handler(func=lambda message: message.text == "Алкогольные")
# def handle_alko(message):
#   menu_alko(message)
#
# @bot.message_handler(func=lambda message: message.text == "Безалкогольные")
# def handle_bezalko(message):
#   menu_bezalko(message)
#
# @bot.message_handler(func=lambda message: message.text == "Орешки")
# def handle_orehi(message):
#   menu_orehi(message)
#
# # ... (обработчики для остальных меню)
#
# # Обработка выбора товара
# @bot.message_handler(func=lambda message: message.text in products)
# def handle_item_selection(message):
#   item = message.text
#   add_to_cart(message, item)
#
# # Обработка команды "Назад"
# @bot.message_handler(func=lambda message: message.text == "Назад")
# def handle_back(message):
#   start_message(message)
#
# # Запуск бота
# bot.polling()


import telebot
from telebot import types

# Замените на ваш токен API бота
bot = telebot.TeleBot("7322740602:AAHJXeL_JZfomMtTU8U53-yXQ8I_nXr2boQ")

# Словарь с товарами и ценами (расширенный ассортимент)
products = {
 # Напитки
 "Пиво": 150,
 "Водка": 300,
 "Вино красное": 250,
 "Вино белое": 250,
 "Вино розовое": 270,
 "Вода": 50,
 "Лимонад": 80,
 "Сок апельсиновый": 100,
 "Сок яблочный": 100,
 "Кола": 90,
 "Спрайт": 90,
 "Фанта": 90,
 # Закуски
 "Сырные орешки": 150,
 "Орешки с беконом": 180,
 "Орешки с васаби": 180,
 "Чипсы": 80,
 "Сухарики": 70,
 "Крекеры": 90,
 "Оливье": 150,
 "Сельдь под шубой": 170,
 # Тортики
 "Шоколадный тортик": 250,
 "Воздушный тортик": 200,
 "Карамельный тортик": 220,
 "Медовик": 230,
 "Наполеон": 240,
 "Тирамису": 280
}

# Словарь для хранения корзины пользователя
user_carts = {}

# Функция для отображения главного меню
def start_message(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 button_napitki = types.KeyboardButton("Напитки")
 button_zakuski = types.KeyboardButton("Закуски")
 button_cart = types.KeyboardButton("Корзина") # Кнопка корзины
 keyboard.add(button_napitki, button_zakuski, button_cart)
 bot.send_message(message.chat.id, "Добро пожаловать! Выберите категорию:", reply_markup=keyboard)

# Функция для отображения меню "Напитки"
def menu_napitki(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 button_alko = types.KeyboardButton("Алкогольные")
 button_bezalko = types.KeyboardButton("Безалкогольные")
 button_back = types.KeyboardButton("Назад")
 keyboard.add(button_alko, button_bezalko, button_back)
 bot.send_message(message.chat.id, "Выберите категорию напитков:", reply_markup=keyboard)

# Функция для отображения меню "Закуски"
def menu_zakuski(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 button_orehi = types.KeyboardButton("Орешки")
 button_tortiki = types.KeyboardButton("Тортики")
 button_holodnye = types.KeyboardButton("Холодные закуски")
 button_back = types.KeyboardButton("Назад")
 keyboard.add(button_orehi, button_tortiki, button_holodnye, button_back)
 bot.send_message(message.chat.id, "Выберите закуски:", reply_markup=keyboard)

# Функция для отображения меню "Алкогольные напитки"
def menu_alko(message):
 keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
 button_pivo = types.KeyboardButton("Пиво")
 button_vodka = types.KeyboardButton("Водка")
 button_vino_krasnoe = types.KeyboardButton("Вино красное")
 button_vino_beloe = types.KeyboardButton("Вино белое")
 button_vino_rozovoe = types.KeyboardButton("Вино розовое")
 button_back = types.KeyboardButton("Назад")
 keyboard.add(button_pivo, button_vodka, button_vino_krasnoe, button_vino_beloe, button_vino_rozovoe, button_back)
 bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)

# Функция для отображения меню "Безалкогольные напитки"
def menu_bezalko(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_voda = types.KeyboardButton("Вода")
  button_limonad = types.KeyboardButton("Лимонад")
  button_sok_apelsin = types.KeyboardButton("Сок апельсиновый")
  button_sok_yabloko = types.KeyboardButton("Сок яблочный")
  button_kola = types.KeyboardButton("Кола")
  button_sprite = types.KeyboardButton("Спрайт")
  button_fanta = types.KeyboardButton("Фанта")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_voda, button_limonad, button_sok_apelsin, button_sok_yabloko, button_kola, button_sprite, button_fanta, button_back)
  bot.send_message(message.chat.id, "Выберите безалкогольный напиток:", reply_markup=keyboard)

# Функция для отображения меню "Орешки"
def menu_orehi(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_syrnye = types.KeyboardButton("Сырные")
  button_bekon = types.KeyboardButton("С беконом")
  button_vasabi = types.KeyboardButton("Васаби")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_syrnye, button_bekon, button_vasabi, button_back)
  bot.send_message(message.chat.id, "Выберите орешки:", reply_markup=keyboard)

# Функция для отображения меню "Тортики"
def menu_tortiki(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_shokolad = types.KeyboardButton("Шоколадный тортик")
  button_vozduшный = types.KeyboardButton("Воздушный тортик")
  button_karamel = types.KeyboardButton("Карамельный тортик")
  button_medovik = types.KeyboardButton("Медовик")
  button_napoleon = types.KeyboardButton("Наполеон")
  button_tiramisu = types.KeyboardButton("Тирамису")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_shokolad, button_vozduшный, button_karamel, button_medovik, button_napoleon, button_tiramisu, button_back)
  bot.send_message(message.chat.id, "Выберите тортик:", reply_markup=keyboard)

# Функция для отображения меню "Холодные закуски"
def menu_holodnye(message):
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button_olivie = types.KeyboardButton("Оливье")
  button_sel = types.KeyboardButton("Сельдь под шубой")
  button_back = types.KeyboardButton("Назад")
  keyboard.add(button_olivie, button_sel, button_back)
  bot.send_message(message.chat.id, "Выберите холодные закуски:", reply_markup=keyboard)

# Функция для добавления товара в корзину
def add_to_cart(message, item):
  user_id = message.chat.id
  if user_id not in user_carts:
    user_carts[user_id] = {}
  if item in user_carts[user_id]:
    user_carts[user_id][item] += 1
  else:
    user_carts[user_id][item] = 1
  bot.send_message(message.chat.id, f"{item} добавлен в корзину.")

# Функция для отображения корзины
def show_cart(message):
  user_id = message.chat.id
  if user_id in user_carts and user_carts[user_id]:
    cart_items = user_carts[user_id]
    cart_text = "Ваша корзина:\n"
    total_price = 0
    for item, quantity in cart_items.items():
      price = products[item]
      item_price = price * quantity
      cart_text += f"{item} x {quantity} = {item_price}\n"
      total_price += item_price
    cart_text += f"\nИтого: {total_price}"
    bot.send_message(message.chat.id, cart_text)
  else:
    bot.send_message(message.chat.id, "Ваша корзина пуста.")

# Функция для удаления товара из корзины
def remove_from_cart(message, product_name):
    chat_id = message.chat.id  # Get chat_id here
    if chat_id in user_carts and product_name in user_carts[chat_id]:
        if user_carts[chat_id][product_name] > 1:
            user_carts[chat_id][product_name] -= 1
            bot.send_message(chat_id, f"Товар '{product_name}' удален из корзины.")
        else:
            del user_carts[chat_id][product_name]
            bot.send_message(chat_id, f"Товар '{product_name}' удален из корзины.")
    else:
        bot.send_message(chat_id, f"Товар '{product_name}' не найден в корзине.")

# Обработка команд
@bot.message_handler(commands=['start'])
def send_welcome(message):
  start_message(message)

@bot.message_handler(func=lambda message: message.text == "Напитки")
def handle_napitki(message):
  menu_napitki(message)

@bot.message_handler(func=lambda message: message.text == "Закуски")
def handle_zakuski(message):
  menu_zakuski(message)

@bot.message_handler(func=lambda message: message.text == "Корзина")
def handle_cart(message):
  show_cart(message)

@bot.message_handler(func=lambda message: message.text == "Алкогольные")
def handle_alko(message):
  menu_alko(message)

@bot.message_handler(func=lambda message: message.text == "Безалкогольные")
def handle_bezalko(message):
  menu_bezalko(message)

@bot.message_handler(func=lambda message: message.text == "Орешки")
def handle_orehi(message):
  menu_orehi(message)

@bot.message_handler(func=lambda message: message.text == "Тортики")
def handle_tortiki(message):
  menu_tortiki(message)

@bot.message_handler(func=lambda message: message.text == "Холодные закуски")
def handle_holodnye(message):
  menu_holodnye(message)

# Обработка выбора товара
@bot.message_handler(func=lambda message: message.text in products)
def handle_item_selection(message):
  item = message.text
  add_to_cart(message, item)

# Обработка команды "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def handle_back(message):
  start_message(message)

# Обработка команды "Удалить"
@bot.message_handler(func=lambda message: message.text.startswith("Удалить "))
def handle_remove_item(message):
    product_name = message.text[7:]
    remove_from_cart(message, product_name)

# Запуск бота
bot.polling()


