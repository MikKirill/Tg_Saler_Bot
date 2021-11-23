import telebot
from telebot import types
import requests
import json
import config

print('start')  # Разделитель

bot = telebot.TeleBot(config.BOT)

    #   Приветствие нового пользователя
@bot.message_handler(commands=['start'])
def welcome(message):
        #   Создание кнопки "Тарифы"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    price = types.KeyboardButton('Тарифы')
    markup.add(price)
        #   Приветствие и описание бота
    bot.send_message(message.chat.id, 'Hello, my friend!!!')
        #   Вставка и описание кнопки
    bot.send_message(message.chat.id, 'Нажмите на кнопку "Тарифы", что бы выбрать желаемый', reply_markup=markup)

    #   Выбор тарифа
@bot.message_handler(content_types=['text'])
def get_link(message):
    if message.chat.type == 'private':
        if message.text == 'Тарифы':
                #   Создание инлайновых кнопок
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_2d = types.InlineKeyboardButton('2D', callback_data='2d_price')
            item_3d = types.InlineKeyboardButton('3D', callback_data='3d_price')
            item_al = types.InlineKeyboardButton('Все', callback_data='al_price')
            markup.add(item_2d, item_3d, item_al)
                #   Отображение инлайновых кнопок
            bot.send_message(message.chat.id, 'Выберите желаемый тарифный план', reply_markup=markup)

    #   Обработка кнопок выбора тарифа и оплаты
@bot.callback_query_handler(func=lambda call: True)
def callback_inline_pack(call):
    try:
            #   Начало обработки
        if call.message:
                #   Выбор тарифа
            if call.data == '2d_price':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                info_2d(call.message.chat.id)
            elif call.data == '3d_price':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                info_3d(call.message.chat.id)
            elif call.data == 'al_price':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                info_al(call.message.chat.id)
                #   Выбор оплаты для 2d
            elif call.data == 'to_pay_2d_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '2d', 1)
            elif call.data == 'to_pay_2d_2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '2d', 2)
            elif call.data == 'to_pay_2d_3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '2d', 3)
                #   Выбор оплаты для 3d
            elif call.data == 'to_pay_3d_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '3d', 1)
            elif call.data == 'to_pay_3d_2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '3d', 2)
            elif call.data == 'to_pay_3d_3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, '3d', 3)
                #   Выбор оплаты для Все
            elif call.data == 'to_pay_al_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, 'all', 1)
            elif call.data == 'to_pay_al_2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, 'all', 2)
            elif call.data == 'to_pay_al_3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Секундочку', reply_markup=None)
                next_pay_step(call.message.chat.id, 'all', 3)
        #   Завершаем "Try" (пока хз как работает)
    except Exception as e:
        print(repr(e))

    # 2D_price
@bot.message_handler(content_types=['Text'])
def info_2d(i):
        #   Создание инлайновых кнопок для выбора оплаты
    markup_pay = types.InlineKeyboardMarkup(row_width=1)
    pay1 = types.InlineKeyboardButton('Оплата способом 1', callback_data='to_pay_2d_1')
    pay2 = types.InlineKeyboardButton('Оплата способом 2', callback_data='to_pay_2d_2')
    pay3 = types.InlineKeyboardButton('Оплата способом 3', callback_data='to_pay_2d_3')
    markup_pay.add(pay1, pay2, pay3)
        #   Информация о тарифе
    bot.send_message(i, '2D Done')
    bot.send_message(i, 'Описание тарифа 2д',
                     reply_markup=markup_pay)

    # 3D_price
@bot.message_handler(content_types=['Text'])
def info_3d(i):
        #   Создание инлайновых кнопок для выбора оплаты
    markup_pay = types.InlineKeyboardMarkup(row_width=1)
    pay1 = types.InlineKeyboardButton('Оплата способом 1', callback_data='to_pay_3d_1')
    pay2 = types.InlineKeyboardButton('Оплата способом 2', callback_data='to_pay_3d_2')
    pay3 = types.InlineKeyboardButton('Оплата способом 3', callback_data='to_pay_3d_3')
    markup_pay.add(pay1, pay2, pay3)
        #   Информация о тарифе
    bot.send_message(i, '3D Done')
    bot.send_message(i, 'Описание тарифа 3д',
                     reply_markup = markup_pay)

    # All_price
@bot.message_handler(content_types=['Text'])
def info_al(i):
        #   Создание инлайновых кнопок для выбора оплаты
    markup_pay = types.InlineKeyboardMarkup(row_width=1)
    pay1 = types.InlineKeyboardButton('Оплата способом 1', callback_data='to_pay_al_1')
    pay2 = types.InlineKeyboardButton('Оплата способом 2', callback_data='to_pay_al_2')
    pay3 = types.InlineKeyboardButton('Оплата способом 3', callback_data='to_pay_al_3')
    markup_pay.add(pay1, pay2, pay3)
        #   Информация о тарифе
    bot.send_message(i, 'All Done')
    bot.send_message(i, 'Описание тарифа все',
                     reply_markup=markup_pay)

    #   Получаем код запроса для генерации и отправки счета
    #   Вход - (Координаты для отправки сообщений, выбранный пак, способ оплаты)
def next_pay_step(user_id, pack, pay):
            #   Тесстовый текст на основе выбора тарифа и способа оплаты
        print('Выбран ' + pack + '-пак и ' +
              str(pay) + 'й способ оплаты')
            #   Генерация счета на основе полученных данных
        pay_link = 'link.com'
            #   Возврат ссылки пользователю
        send_link(pay_link, user_id)

    #   Возврат сгенерированной ссылки пользователю
@bot.message_handler(content_types=['Text'])
def send_link(link, user_id):
    bot.send_message(user_id, link)

    #   Не останавливаем программу и всегда ожидаем запроса
bot.polling(none_stop=True)
