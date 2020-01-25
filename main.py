#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
from secure import TOKEN

import telebot

import json

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    print(message.chat.id)

@bot.message_handler(commands=['help'])
def start(message):
  sent = bot.send_message(message.chat.id, 'Please describe your problem.')
  bot.register_next_step_handler(sent, hello)

def hello(message):
    bot.send_message(message.chat.id, 'Thank you!')

def askCosts(user):
    bot.send_message(user, 'Привет, напиши свои расходы за сегодня /start')

@bot.message_handler(func=lambda message: True)
def setMoney(message):
    bot.send_message(message.chat.id, 'Привет, напиши свой текущий баланс ')
    sent = bot.send_message(message.chat.id, 'Карта: ')
    bot.register_next_step_handler(sent, setCard)
def setCard(message):
    with open("users.json", "r") as jsonFile:
        data = json.load(jsonFile)

    tmp = data["users"]
    id = -1

    for i in range(len(tmp)):

        if(tmp[i]["id"] == message.chat.id):
            id = i
    if(id < 0):
        bot.send_message(message.chat.id, 'Пользователь не найден')
    else:
        data["users"][id]["card"] = message.text
        print(message.text)
        with open("users.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    bot.send_message(message.chat.id, "OK")
    #bot.send_message(message.chat.id, 'Наличные: ')



bot.polling()