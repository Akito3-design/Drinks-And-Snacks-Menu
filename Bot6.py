import telebot
from telebot import types

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

# Словари для хранения корзины и состояния пользователя
user_carts = {}
user_states = {}

# Функция для отображения главного меню
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_napitki = types.KeyboardButton("Напитки")
    button_zakuski = types.KeyboardButton("Закуски")
    button_cart = types.KeyboardButton("Корзина")
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

# Функции для отображения подкатегорий меню (алкогольные, безалкогольные напитки и т.д.)
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

def menu_orehi(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_syrnye = types.KeyboardButton("Сырные орешки")
    button_bekon = types.KeyboardButton("Орешки с беконом")
    button_vasabi = types.KeyboardButton("Орешки с васаби")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_syrnye, button_bekon, button_vasabi, button_back)
    bot.send_message(message.chat.id, "Выберите орешки:", reply_markup=keyboard)

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

def menu_holodnye(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_olivye = types.KeyboardButton("Оливье")
    button_sel_d = types.KeyboardButton("Сельдь под шубой")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_olivye, button_sel_d, button_back)
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
    
    # Установка флагов и предложение закусок или напитков только один раз
    if user_id not in user_states:
        user_states[user_id] = {"offered_zakuski": False, "offered_napitki": False}

    if product_name in ["Пиво", "Водка", "Вино красное", "Вино белое", "Вино розовое", "Вода", "Лимонад", "Сок апельсиновый", "Сок яблочный", "Кола", "Спрайт", "Фанта"]:
        if not user_states[user_id]["offered_zakuski"]:
            user_states[user_id]["offered_zakuski"] = True
            ask_for_zakuski(message)
    elif product_name in ["Сырные орешки", "Орешки с беконом", "Орешки с васаби", "Чипсы", "Сухарики", "Крекеры", "Оливье", "Сельдь под шубой", "Шоколадный тортик", "Воздушный тортик", "Карамельный тортик", "Медовик", "Наполеон", "Тирамису"]:
        if not user_states[user_id]["offered_napitki"]:
            user_states[user_id]["offered_napitki"] = True
            ask_for_napitki(message)

# Функции для предложения приобрести закуску или напиток
def ask_for_zakuski(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = types.KeyboardButton("Да")
    button_no = types.KeyboardButton("Нет")
    keyboard.add(button_yes, button_no)
    bot.send_message(message.chat.id, "Не хотите приобрести закуску?", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_zakuski_decision)

def ask_for_napitki(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_yes = types.KeyboardButton("Да")
    button_no = types.KeyboardButton("Нет")
    keyboard.add(button_yes, button_no)
    bot.send_message(message.chat.id, "Не хотите приобрести напиток?", reply_markup=keyboard)
    bot.register_next_step_handler(message, handle_napitki_decision)

def handle_zakuski_decision(message):
    if message.text == "Да":
        menu_zakuski(message)
    else:
        menu_napitki(message)

def handle_napitki_decision(message):
    if message.text == "Да":
        menu_napitki(message)
    else:
        menu_zakuski(message)

# Отображение корзины пользователя
def show_cart(message):
    user_id = message.chat.id
    if user_id in user_carts and user_carts[user_id]:
        cart_items = user_carts[user_id]
        cart_text = "Ваша корзина:\n"
        total_price = 0
        for item, quantity in cart_items.items():
            price = products[item]
            item_total = price * quantity
            cart_text += f"{item} x {quantity} = {item_total} руб.\n"
            total_price += item_total
        cart_text += f"\nИтого: {total_price} руб."
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_clear_cart = types.KeyboardButton("Очистить корзину")
        button_back = types.KeyboardButton("Назад")
        keyboard.add(button_clear_cart, button_back)
        bot.send_message(message.chat.id, cart_text, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Ваша корзина пуста.")

# Очистка корзины
def clear_cart(message):
    user_id = message.chat.id
    if user_id in user_carts:
        user_carts[user_id] = {}
        bot.send_message(message.chat.id, "Ваша корзина очищена.")
    else:
        bot.send_message(message.chat.id, "Ваша корзина пуста.")

# Обработчик команд
@bot.message_handler(commands=["start"])
def handle_start(message):
    start_message(message)

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Напитки":
        menu_napitki(message)
    elif message.text == "Закуски":
        menu_zakuski(message)
    elif message.text == "Корзина":
        show_cart(message)
    elif message.text == "Назад":
        start_message(message)
    elif message.text in products:
        add_to_cart(message, message.text)
    elif message.text == "Алкогольные":
        menu_alko(message)
    elif message.text == "Безалкогольные":
        menu_bezalko(message)
    elif message.text == "Орешки":
        menu_orehi(message)
    elif message.text == "Тортики":
        menu_tortiki(message)
    elif message.text == "Холодные закуски":
        menu_holodnye(message)
    elif message.text == "Очистить корзину":
        clear_cart(message)
    else:
        bot.send_message(message.chat.id, "Я вас не понял. Пожалуйста, выберите одну из предложенных опций.")

bot.polling(none_stop=True)

