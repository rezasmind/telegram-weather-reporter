from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from telegram import Update,Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

owm = OWM('TOKEN')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Neka')
w = observation.weather

def weather():
    time = datetime.datetime.now().strftime("%H")
    while True:
        if(time == "08"):
            return "Neka's Weather for Today: \n " + str(w.detailed_status)

    

def main():
    bot = Bot("TOKEN")
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher

    bot.send_message(chat_id="-1001604367904", text=weather())
    updater.start_polling()
    updater.idle()

main()
