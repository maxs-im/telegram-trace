import telebot.credentials as storage
from telebot.trace import trace

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import (ChatAction)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hey this is your bot!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Currently I am in Alpha stage, help me also!')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_chat_action(action=ChatAction.TYPING)
    # filter message (allowed digits, alphabet, ",", ":", "/")
    filtered_msg = "".join([character for character in update.message.text 
                                        if character.isalnum() or character in ":./"])
    update.message.reply_text(trace(filtered_msg))

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def set_handlers(dispatcher):
    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dispatcher.add_error_handler(error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    try:
        updater = Updater(storage.TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        set_handlers(updater.dispatcher)

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
    except Exception as e:
        logger.fatal('During bot creation: %s', e)
