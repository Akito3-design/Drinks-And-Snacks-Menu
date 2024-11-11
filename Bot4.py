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
    keyboard.add(button_voda, button_limonad, button_sok_apelsin, button_sok_yabloko, button_kola, button_sprite,
                 button_fanta, button_back)
    bot.send_message(message.chat.id, "Выберите безалкогольный напиток:", reply_markup=keyboard)


# Функция для отображения меню "Орешки"
def menu_orehi(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_syrnye = types.KeyboardButton("Сырные орешки")
    button_bekon = types.KeyboardButton("Орешки с беконом")
    button_vasabi = types.KeyboardButton("Орешки с васаби")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_syrnye, button_bekon, button_vasabi, button_back)
    bot.send_message(message.chat.id, "Выберите орешки:", reply_markup=keyboard)


# Функция для обработки выбора "Тортики"
def menu_tortiki(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_shokoladny = types.KeyboardButton("Шоколадный тортик")
    button_vozduhsny = types.KeyboardButton("Воздушный тортик")
    button_karamelny = types.KeyboardButton("Карамельный тортик")
    button_medovik = types.KeyboardButton("Медовик")
    button_napoleon = types.KeyboardButton("Наполеон")
    button_tiramisu = types.KeyboardButton("Тирамису")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_shokoladny, button_vozduhsny, button_karamelny, button_medovik, button_napoleon, button_tiramisu, button_back)
    bot.send_message(message.chat.id, "Выберите тортик:", reply_markup=keyboard)

# Функция для обработки выбора "Холодные закуски"
def menu_holodnye(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_olivie = types.KeyboardButton("Оливье")
    button_sel_pod_shub = types.KeyboardButton("Сельдь под шубой")
    button_chips = types.KeyboardButton("Чипсы")
    button_suhariki = types.KeyboardButton("Сухарики")
    button_krekeri = types.KeyboardButton("Крекеры")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_olivie, button_sel_pod_shub, button_chips, button_suhariki, button_krekeri, button_back)
    bot.send_message(message.chat.id, "Выберите холодную закуску:", reply_markup=keyboard)

# Функция для добавления товара в корзину
def add_to_cart(message, product_name):
    user_id = message.chat.id
    if user_id not in user_carts:
        user_carts[user_id] = {}
    if product_name in user_carts[user_id]:
        user_carts[user_id][product_name] += 1
    else:
        user_carts[user_id][product_name] = 1
    bot.send_message(message.chat.id, f"Товар {product_name} добавлен в корзину!")

# Функция для отображения корзины пользователя
def show_cart(message):
    user_id = message.chat.id
    if user_id in user_carts and user_carts[user_id]:
        cart_items = user_carts[user_id]
        cart_text = "Ваша корзина:\n"
        total_price = 0
        for item, quantity in cart_items.items():
            price = products[item]
            item_total = price * quantity
            cart_text += f"{item} x {quantity} = {item_total}\n"
            total_price += item_total
        cart_text += f"\nИтого: {total_price}"
        bot.send_message(message.chat.id, cart_text)
    else:
        bot.send_message(message.chat.id, "Ваша корзина пуста.")

# Функция для удаления товара из корзины
def remove_from_cart(message, product_name):
    user_id = message.chat.id
    if user_id in user_carts and product_name in user_carts[user_id]:
        if user_carts[user_id][product_name] > 1:
            user_carts[user_id][product_name] -= 1
            bot.send_message(message.chat.id, f"Товар '{product_name}' удален из корзины.")
        else:
            del user_carts[user_id][product_name]
            bot.send_message(message.chat.id, f"Товар '{product_name}' удален из корзины.")
    else:
        bot.send_message(message.chat.id, f"Товар '{product_name}' не найден в корзине.")

# Обработка команд бота
@bot.message_handler(commands=['start'])
def start(message):
    start_message(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    text = message.text.lower()

    if text == "напитки":
        menu_napitki(message)
    elif text == "закуски":
        menu_zakuski(message)
    elif text == "корзина":
        show_cart(message)

    # Обработка категорий напитков
    elif text == "алкогольные":
        menu_alko(message)
    elif text == "безалкогольные":
        menu_bezalko(message)

    # Обработка категорий закусок
    elif text == "орешки":
        menu_orehi(message)
    elif text == "тортики":
        menu_tortiki(message)
    elif text == "холодные закуски":
        menu_holodnye(message)

    # Обработка выбора конкретных товаров
    elif text == "пиво":
        add_to_cart(message, "Пиво")
    elif text == "водка":
        add_to_cart(message, "Водка")
    elif text == "вино красное":
        add_to_cart(message, "Вино красное")
    elif text == "вино белое":
        add_to_cart(message, "Вино белое")
    elif text == "вино розовое":
        add_to_cart(message, "Вино розовое")
    elif text == "вода":
        add_to_cart(message, "Вода")
    elif text == "лимонад":
        add_to_cart(message, "Лимонад")
    elif text == "сок апельсиновый":
        add_to_cart(message, "Сок апельсиновый")
    elif text == "сок яблочный":
        add_to_cart(message, "Сок яблочный")
    elif text == "кола":
        add_to_cart(message, "Кола")
    elif text == "спрайт":
        add_to_cart(message, "Спрайт")
    elif text == "фанта":
        add_to_cart(message, "Фанта")
    elif text == "сырные орешки":
        add_to_cart(message, "Сырные орешки")
    elif text == "орешки с беконом":
        add_to_cart(message, "Орешки с беконом")
    elif text == "орешки с васаби":
        add_to_cart(message, "Орешки с васаби")
    elif text == "шоколадный тортик":
        add_to_cart(message, "Шоколадный тортик")
    elif text == "воздушный тортик":
        add_to_cart(message, "Воздушный тортик")
    elif text == "карамельный тортик":
        add_to_cart(message, "Карамельный тортик")
    elif text == "медовик":
        add_to_cart(message, "Медовик")
    elif text == "наполеон":
        add_to_cart(message, "Наполеон")
    elif text == "тираmisu":
        add_to_cart(message, "Тирамису")
    elif text == "оливье":
        add_to_cart(message, "Оливье")
    elif text == "сельдь под шубой":add_to_cart(message, "Сельдь под шубой")
    elif text == "чипсы":
        add_to_cart(message, "Чипсы")
    elif text == "сухарики":
        add_to_cart(message, "Сухарики")
    elif text == "крекеры":
        add_to_cart(message, "Крекеры")

    # Обработка команды "Удалить"
    elif text.startswith("удалить "):
        product_name = text[7:].strip()
        remove_from_cart(message, product_name)

    # Обработка кнопки "Назад"
    elif text == "назад":
        start_message(message)

# Запуск бота
bot.polling(none_stop=True)

