import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_TOKEN = '8d1f636828f2d5994705a245dc7acdf7'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I will notify you when a match is found.')


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update: Update, context: CallbackContext):
    """Log errors caused by updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Register message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

def notify_match(chat_id, match_info):
    """Send a notification about a found match to a specific user."""
    updater.bot.send_message(chat_id, f"Match found! {match_info}")



if __name__ == '__main__':
    main()
