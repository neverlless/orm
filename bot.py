# -*- coding: utf-8 -*-
# coding: utf-8
import re
import copy
import requests
import sys
import traceback
import json
import time
from os.path import exists
import logging
import os
import math
import threading
from threading import Timer
import random
import pymysql
import datetime
import telebot
import asyncio
from tortoise import Tortoise, fields, run_async
from tortoise.models import Model
from tortoise.expressions import F, Q
import logger
import engine as db
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

# Здесь игровые штуки
import logger
import engine as db

# Constants
ifellow = 334798437
devChat = -1002177765326
owner = ['334798437']
devs = ['334798437']
tradeChat = -1002177765326
godEyeChat = -1002177765326
leadersChannel = -1002177765326
main_chat = -1002177765326

# Logging configuration
logging.basicConfig(level=logging.INFO, filename='toh.log')

# Initialize bot and dispatcher
bot = Bot(token='')
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Подхват файлов
print("Подключение плагинов...")
game_plugins = [f[:-3] for f in os.listdir('game') if f.endswith('.py')]
for plugin in game_plugins:
    try:
        exec(open(f"./game/{plugin}.py", encoding="utf-8").read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin) 
        print(str(e))

# Main function to restart database connection
async def databasetimer():
    while True:
        if not db.database.is_closed():
            db.database.close()
            db.database.connect()
            print("DB conn restart")
        await asyncio.sleep(3600)

# Start the database timer in the background
async def on_startup():
    asyncio.create_task(databasetimer())

if __name__ == "__main__":
    # Start polling
    dp.start_polling(dp, on_startup=on_startup)
