from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Welcome to URL downloader!\nPlease provide a valid url')


def textHandler(update: Update, context: CallbackContext) -> None:
    if update.message.parse_entities(types=MessageEntity.URL):
        update.message.reply_text(text='You sent a valid URL!', quote=True)

def main():
    TOKEN = "YOUR BOT TOKEN"
    
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
