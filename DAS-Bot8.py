import telebot
from telebot import types

bot = telebot.TeleBot("7585964135:AAGWL1YjoJx0Zsah2JWi_ZG3fQuvwlYNm4U")

# Словарь с товарами и ценами (расширенный ассортимент)
products = {
    # Напитки #################################################################
    # Не крепкое
    "Лимончелло": 220,
    "Коктейль": 340,
    "Сидр": 250,
    "Вино": 450,
    "Соджу": 150,
    "Мартини": 750,
    "Ликер": 200,
    "Пунш": 300,
    "Вермут": 340,
    "Пиво": 170,
    "Шампанское": 700,
    # Крепкое
    "Чача": 230,
    "Абсент": 1200,
    "Джин": 950,
    "Бренди": 1300,
    "Самогон": 620,
    "Виски": 2300,
    "Водка": 400,
    "Текила": 760,
    "Ром": 3600,
    "Коньяк": 2100,
    # Безалкогольное
    # лимонад
    "Тоник": 170,
    "Минералка": 150,
    "Спрайт": 140,
    "Тархун": 100,
    "Дюшес": 100,
    "Кока-кола": 180,
    "Колокольчик": 120,
    # Морс
    "Облипиховый": 210,
    "Брусничный": 200,
    "Клюквенный": 240,
    # Сок
    "Мямлочный": 120,
    "Вишневый": 160,
    "Апельсиновый": 200,
    "Мультифрукт": 180,
    "Томатный": 150,
    ###############################################################################
    # Закуски
    # Дессерты
    "Халва": 250,
    "Пахлава": 200,
    "Мороженое": 220,
    "Маффин": 230,
    "Чизкейк": 260,
    "Фондю": 280,
    "Тирамиссу": 280,
    # Сыр
    "Брынза": 250,
    "Камамбер": 200,
    "Копченый": 220,
    "Чечил": 230,
    "Бри": 240,
    "Дорблю": 280,
    # Мясо
    "Вяленое": 250,
    "Колбаса": 200,
    "Паштет": 220,
    "Копченое": 230,
    "Сушеное": 240,
    # Морепродукты
    "Креветки": 300,
    "Кальмары": 500,
    "Мидии": 400,
    "Морская капуста": 230,
    "Омары": 600,
    "Рыба": 280,
    "Раки": 700,
    # Фрукты
    "Цитрусовые": 250,
    "Бананы": 200,
    "Сухофрукты": 220,
    "Персики": 230,
    "Сливы": 240,
    "Яблоки": 280,
    # Бутерброды
    "С сыром": 250,
    "С колбасой": 200,
    "С икрой": 220,
    "С красной рыбой": 230,
    # Колечки
    "Луковые": 250,
    "Сырные": 200,
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
    button_sir = types.KeyboardButton("Сыр")
    button_meet = types.KeyboardButton("Мясо")
    button_desert = types.KeyboardButton("Дессерты")
    button_seafood = types.KeyboardButton("Морепродукты")
    button_fruits = types.KeyboardButton("Фрукты")
    button_sandwich = types.KeyboardButton("Бутерброды")
    button_kolechki = types.KeyboardButton("Колечки")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_sir, button_meet, button_desert, button_seafood, button_fruits, button_sandwich,
                 button_kolechki, button_back)
    bot.send_message(message.chat.id, "Выберите закуски:", reply_markup=keyboard)



# Функции для отображения подкатегорий меню (алкогольные, безалкогольные напитки и т.д.)
def menu_alko(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_krepkoe = types.KeyboardButton("Крепкое")
    button_nekrepkoe = types.KeyboardButton("Не крепкое")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_nekrepkoe, button_krepkoe, button_back)
    bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)


def menu_krepkoe(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_chacha = types.KeyboardButton("Чача")
    button_abcent = types.KeyboardButton("Абсент")
    button_dzhin = types.KeyboardButton("Джин")
    button_brendy = types.KeyboardButton("Бренди")
    button_camogon = types.KeyboardButton("Самогон")
    button_viski = types.KeyboardButton("Виски")
    button_vodka = types.KeyboardButton("Водка")
    button_tekila = types.KeyboardButton("Текила")
    button_rom = types.KeyboardButton("Ром")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_chacha,button_abcent, button_dzhin,button_brendy, button_camogon,
    button_viski, button_vodka, button_tekila, button_rom,button_back)
    bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)

def menu_nekrepkoe(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_limonchello = types.KeyboardButton("Лимончелло")
    button_kokteil = types.KeyboardButton("Коктейль")
    button_sidr = types.KeyboardButton("Сидр")
    button_vino = types.KeyboardButton("Вино")
    button_sodgy = types.KeyboardButton("Соджу")
    button_martini = types.KeyboardButton("Мартини")
    button_liker = types.KeyboardButton("Ликер")
    button_punsh = types.KeyboardButton("Пунш")
    button_vermut = types.KeyboardButton("Вермут")
    button_pivo = types.KeyboardButton("Пиво")
    button_shampanskoe = types.KeyboardButton("Шампанское")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_limonchello, button_kokteil, button_sidr, button_vino,
    button_sodgy,button_martini, button_liker, button_punsh, button_vermut,
    button_pivo, button_shampanskoe, button_back)
    bot.send_message(message.chat.id, "Выберите алкогольный напиток:", reply_markup=keyboard)


def menu_bezalko(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_limonade = types.KeyboardButton("Лимонад")
    button_mors = types.KeyboardButton("Морс")
    button_sok = types.KeyboardButton("Сок")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_limonade, button_mors, button_sok, button_back)
    bot.send_message(message.chat.id, "Выберите безалкогольный напиток:", reply_markup=keyboard)

def menu_limonade(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_tonik = types.KeyboardButton("Тоник")
    button_mineralka = types.KeyboardButton("Минералка")
    button_tarhune = types.KeyboardButton("Тархун")
    button_sprit = types.KeyboardButton("Спрайт")
    button_duhes = types.KeyboardButton("Дюшес")
    button_koka = types.KeyboardButton("Кока-кола")
    button_kolocolchik = types.KeyboardButton("Колокольчик")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_tonik,button_tarhune, button_koka, button_kolocolchik, button_mineralka,button_sprit,button_duhes,button_back)
    bot.send_message(message.chat.id, "Выберите лимонад:", reply_markup=keyboard)

def menu_mors(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_klukva= types.KeyboardButton("Клюквенный")
    button_brusnichniy = types.KeyboardButton("Брусничный")
    button_oblipixoviy = types.KeyboardButton("Облипиховый")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_klukva,button_brusnichniy,button_oblipixoviy,button_back)
    bot.send_message(message.chat.id, "Выберите морс:", reply_markup=keyboard)

def menu_sok(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_myamloko = types.KeyboardButton("Мямлочный")
    button_vishneviy = types.KeyboardButton("Вишневый")
    button_apelsin = types.KeyboardButton("Апельсиновый")
    button_multifrukt = types.KeyboardButton("Мультифрукт")
    button_tomaTOOOOOOOO = types.KeyboardButton("Томатный")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_multifrukt,button_apelsin,button_myamloko,button_vishneviy,button_tomaTOOOOOOOO,button_back)
    bot.send_message(message.chat.id, "Выберите сок:", reply_markup=keyboard)

def menu_sir(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_brynza = types.KeyboardButton("Брынза")
    button_kamamber = types.KeyboardButton("Камамбер")
    button_kopcheniy = types.KeyboardButton("Копченый")
    button_chechil = types.KeyboardButton("Чечил")
    button_bri = types.KeyboardButton("Бри")
    button_dorblue = types.KeyboardButton("Дорблю")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_brynza, button_kamamber, button_kopcheniy, button_chechil, button_bri, button_dorblue, button_back)
    bot.send_message(message.chat.id, "Выберите сыр:", reply_markup=keyboard)

def menu_meet(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_vyalenoe = types.KeyboardButton("Вяленое")
    button_kolbasa = types.KeyboardButton("Колбаса")
    button_pashtet = types.KeyboardButton("Паштет")
    button_kopchonoe = types.KeyboardButton("Копченое")
    button_sushonoe = types.KeyboardButton("Сушеное")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_vyalenoe, button_kolbasa, button_pashtet, button_kopchonoe, button_sushonoe, button_back)
    bot.send_message(message.chat.id, "Выберите мясо:", reply_markup=keyboard)

def menu_desert(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_halva = types.KeyboardButton("Халва")
    button_pahlava = types.KeyboardButton("Пахлава")
    button_icecream = types.KeyboardButton("Мороженое")
    button_maffin = types.KeyboardButton("Маффин")
    button_chiscake = types.KeyboardButton("Чизкейк")
    button_fondu = types.KeyboardButton("Фондю")
    button_tiramissu = types.KeyboardButton("Тирамиссу")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_halva, button_pahlava, button_icecream, button_maffin, button_chiscake, button_fondu, button_tiramissu, button_back)
    bot.send_message(message.chat.id, "Выберите дессерты:", reply_markup=keyboard)

def menu_seafood(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_krevetki = types.KeyboardButton("Креветки")
    button_kalmari = types.KeyboardButton("Кальмары")
    button_midii = types.KeyboardButton("Мидии")
    button_seacapusta = types.KeyboardButton("Морская капуста")
    button_omar = types.KeyboardButton("Омары")
    button_fish = types.KeyboardButton("Рыба")
    button_rak = types.KeyboardButton("Раки")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_krevetki, button_kalmari, button_midii, button_seacapusta, button_omar, button_fish, button_rak, button_back)
    bot.send_message(message.chat.id, "Выберите морепродукты:", reply_markup=keyboard)

def menu_fruits(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_citrus = types.KeyboardButton("Цитрусовые")
    button_banana = types.KeyboardButton("Бананы")
    button_suhfruits = types.KeyboardButton("Сухофрукты")
    button_percik = types.KeyboardButton("Персики")
    button_sliva = types.KeyboardButton("Сливы")
    button_apple = types.KeyboardButton("Яблоки")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_citrus, button_banana, button_suhfruits, button_percik, button_sliva, button_apple, button_back)
    bot.send_message(message.chat.id, "Выберите фрукты:", reply_markup=keyboard)

def menu_sandwich(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_ssirom = types.KeyboardButton("С сыром")
    button_skolbasa = types.KeyboardButton("С колбасой")
    button_sikra = types.KeyboardButton("С икрой")
    button_sredfish = types.KeyboardButton("С красной рыбой")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_ssirom, button_skolbasa, button_sikra, button_sredfish, button_back)
    bot.send_message(message.chat.id, "Выберите бутерброды:", reply_markup=keyboard)

def menu_kolechki(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_lyk = types.KeyboardButton("Луковые")
    button_sirnie = types.KeyboardButton("Сырные")
    button_back = types.KeyboardButton("Назад")
    keyboard.add(button_lyk, button_sirnie, button_back)
    bot.send_message(message.chat.id, "Выберите колечки:", reply_markup=keyboard)


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

    if product_name in ["Пиво", "Водка", "Вино красное", "Вино белое", "Вино розовое", "Вода", "Лимонад",
                        "Сок апельсиновый", "Сок яблочный", "Кола", "Спрайт", "Фанта"]:
        if not user_states[user_id]["offered_zakuski"]:
            user_states[user_id]["offered_zakuski"] = True
            ask_for_zakuski(message)
    elif product_name in ["Сырные орешки", "Орешки с беконом", "Орешки с васаби", "Чипсы", "Сухарики", "Крекеры",
                          "Оливье", "Сельдь под шубой", "Шоколадный тортик", "Воздушный тортик", "Карамельный тортик",
                          "Медовик", "Наполеон", "Тирамису"]:
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
    elif message.text == "Крепкое":
        menu_krepkoe(message)
    elif message.text == "Не крепкое":
        menu_nekrepkoe(message)
    elif message.text == "Сок":
        menu_sok(message)
    elif message.text == "Лимонад":
        menu_limonade(message)
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
    elif message.text == "Морс":
        menu_mors(message)
    elif message.text == "Сыр":
        menu_sir(message)
    elif message.text == "Мясо":
        menu_meet(message)
    elif message.text == "Дессерты":
        menu_desert(message)
    elif message.text == "Морепродукты":
        menu_seafood(message)
    elif message.text == "Фрукты":
        menu_fruits(message)
    elif message.text == "Бутерброды":
        menu_sandwich(message)
    elif message.text == "Колечки":
        menu_kolechki(message)
    elif message.text == "Очистить корзину":
        clear_cart(message)
    else:
        bot.send_message(message.chat.id, "Я вас не понял. Пожалуйста, выберите одну из предложенных опций.")


bot.polling(none_stop=True)