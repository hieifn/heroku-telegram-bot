import socket, subprocess, json
import time
import os.path


from telegram.ext import Updater

updater = Updater(token='TELEGRAM_TOKEN')

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Bem vindo ao desColado Bot! Alguém deixou cair um Tanenbaum?")

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

def echo(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Experimente um de nossos comandos: \n /octEval para avaliar uma sentença no octave \n /mathgraph para receber o output grafico de uma função no Matlab")

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
        text_caps = ' '.join(args).upper()
        bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)
        
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
        query = update.inline_query.query
        if not query:
                return
        results = list()
        results.append(
                InlineQueryResultArticle(
                        id=query.upper(),
                        title='Caps',
                        input_message_content=InputTextMessageContent(query.upper())
                )
        )
        bot.answerInlineQuery(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text=" Comando não reconhecido. Tente novamente !")

unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
