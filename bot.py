from telegram.ext import Updater, CommandHandler

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('541654752:AAH9S1XoCAGRaNpKIiUSUD2vaOSXB3WxPK4')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
