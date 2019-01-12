#!/usr/bin/env python
# -*- coding: utf-8 -*-

#imports
import telepot

#api do bot
api = ''
bot = telepot.Bot(api)

def handle(msg):
        uid = msg['from']['id'] #id do usuário
        firstname = msg['from']['first_name'] #primeiro nome do usuário
        chat_id = msg['chat']['id'] #id do chat
        chat_type = msg['chat']['type'] #tipo de chat ex: private, supergroup
        try:
                user = '@' + msg['from']['username'] #username do usuário
        except:
                print ''
        msgid = msg['message_id'] #id da mensagem

        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg.get('text'):
                texto = msg['text'].split()[0]
                if texto == '/start':
                        if chat_type == 'private':
                                bot.sendMessage(chat_id, 'Mensagem')
                        elif chat_type == 'supergroup':
                                bot.sendMessage(chat_id, 'Mensagem')
bot.message_loop(handle)
print '[+] ON'
while 1:
        pass
