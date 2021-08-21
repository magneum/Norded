"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"—••÷𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  ================== MAIN IMPORT AREA ============= —••÷[🕊NORDED🕊]÷••—÷••—"
'''
.................................................................
Builtin import area
.................................................................
'''

import os
import io
from re import I
import sys
import math
import time
import asyncio
import logging
import threading
import importlib
from os import execl
from time import time
from os import getenv
from datetime import *
from time import sleep

'''
.................................................................
Builtin import area
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Fetched modules import area
.................................................................
'''

try:
    from pytgcalls import pytgcalls
except ImportError:
    os.system("pip install pytgcalls")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import youtube_search
except ImportError:
    os.system("pip install youtube_search")
try:
    import youtube_dl
except ImportError:
    os.system("pip install youtube_dl")
try:
    import wheel
except ImportError:
    os.system("pip install wheel")
try:
    import TgCrypto
except ImportError:
    os.system("pip install TgCrypto")
try:
    import pyrogram
except ImportError:
    os.system("pip install pyrogram")
try:
    import heroku3
except ImportError:
    os.system("pip install heroku3")
try:
    import ffmpeg
except ImportError:
    os.system("pip install ffmpeg-python")
try:
    import urllib3
except ImportError:
    os.system("pip install urllib3")
try:
    from termcolor import *
except ImportError:
    os.system("pip install termcolor")
try:
    from loguru import logger
except ImportError:
    os.system("pip install loguru")
try:
    from dotenv import load_dotenv
except ImportError:
    os.system("pip install python-dotenv")
try: 
    import signal
except ImportError:
    os.system("pip install signal")
try: 
    import requests
except ImportError:
    os.system("pip install requests")

'''
.................................................................
Fetched modules import area
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Import and reload area
.................................................................
'''

import pyrogram
import wheel
import heroku3
import ffmpeg
import urllib3
import termcolor
import dotenv
import requests
import youtube_search
import youtube_dl
import signal
importlib.reload(pyrogram)
importlib.reload(wheel)
importlib.reload(heroku3)
importlib.reload(ffmpeg)
importlib.reload(urllib3)
importlib.reload(termcolor)
importlib.reload(dotenv)
importlib.reload(requests)
importlib.reload(youtube_search)
importlib.reload(signal)
importlib.reload(youtube_dl)

'''
.................................................................
Import and reload area
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Pyrogram and PyTgCalls 
modules import area
.................................................................
'''

load_dotenv("—••÷[🕊NORDED🕊]÷••—/.env")
file = open("db.py", "w") 
file.write("def init():\n    global db\n    db = {}") 
file.close()
import db
db.init()
import asyncio
from db import db
from pyromod import listen
from youtube_search import YoutubeSearch
from pyrogram.types import ChatPermissions
from pyrogram.utils import MAX_CHANNEL_ID
from pyrogram import Client, filters,idle
from asyncio.exceptions import TimeoutError
from pyrogram.raw.base import InputGroupCall
from pytgcalls import GroupCall as NORDCALLER
from pyrogram.types import Message as NordLink
utcnow = datetime.utcnow().replace(microsecond=0)
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pytgcalls import GroupCallFactory, GroupCallFileAction
from pyrogram.raw.functions.phone import EditGroupCallTitle
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.errors import SessionPasswordNeeded, FloodWait,PhoneNumberInvalid, ApiIdInvalid,PhoneCodeInvalid, PhoneCodeExpired

'''
.................................................................
Pyrogram and PyTgCalls 
modules import area
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""

'''
.................................................................
MIB keyboard shortcuts
.................................................................
'''

MIB = InlineKeyboardMarkup([[
InlineKeyboardButton(
text="🏷Group",
url="https://t.me/HYPEVOIDS"),
InlineKeyboardButton(
text="💰Channel",
url="https://t.me/HYPEVOIDLAB"),
InlineKeyboardButton(
text="⚜️Dev+Git",
url="https://t.me/HYPEVOIDBOT")],
[InlineKeyboardButton(
text="🧸Master Bot",
url="https://t.me/XERONOIDBOT")]])

'''
.................................................................
MIB keyboard shortcuts
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
A part of CallbackData
.................................................................
'''

HELP_BUTTONS = InlineKeyboardMarkup([[
InlineKeyboardButton(
"Member Commands 💛",
callback_data="Member Commands 💛"),],[
InlineKeyboardButton(
"Admin Commands ⚜️",
callback_data="Admin Commands ⚜️"),],[  
InlineKeyboardButton(
"Heroku Commands 🟣",
callback_data="Heroku Commands 🟣"),],[
InlineKeyboardButton(
"Exit Help Menu🔺",
callback_data="Exit Help Menu🔺")]])

'''
.................................................................
A part of CallbackData
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
A part of CallbackData
.................................................................
'''

CLOSE_BUTTON = InlineKeyboardMarkup(
[[InlineKeyboardButton(
"Exit Help Menu🔺",
callback_data="Exit Help Menu🔺")]])

'''
.................................................................
A part of CallbackData
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
A part of CallbackData
.................................................................
'''

MEM_BUTT = InlineKeyboardMarkup([[
InlineKeyboardButton(
"Admin Commands ⚜️",
callback_data="Admin Commands ⚜️"),],[
InlineKeyboardButton(
"Heroku Commands 🟣",
callback_data="Heroku Commands 🟣"),],[
InlineKeyboardButton(
"Exit Help Menu🔺",
callback_data="Exit Help Menu🔺")]])

'''
.................................................................
A part of CallbackData
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
A part of CallbackData
.................................................................
'''

ADM_BUTT = InlineKeyboardMarkup([[
InlineKeyboardButton(
"Member Commands 💛",
callback_data="Member Commands 💛"),],[
InlineKeyboardButton(
"Heroku Commands 🟣",
callback_data="Heroku Commands 🟣"),],[
InlineKeyboardButton(
"Exit Help Menu🔺",
callback_data="Exit Help Menu🔺")]])

'''
.................................................................
A part of CallbackData
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
A part of CallbackData
.................................................................
'''

HERO_BUTT = InlineKeyboardMarkup([[
InlineKeyboardButton(
"Member Commands 💛",
callback_data="Member Commands 💛"),],[
InlineKeyboardButton(
"Admin Commands ⚜️",
callback_data="Admin Commands ⚜️"),],[
InlineKeyboardButton(
"Exit Help Menu🔺",
callback_data="Exit Help Menu🔺")]])

'''
.................................................................
A part of CallbackData
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Environment area and depends 
on either .env or herokuvars
.................................................................
'''

HEROKU = getenv("HEROKU",None)
if HEROKU == "HEROKU":
    API_ID = int(getenv("API_ID",None))
    API_HASH = getenv("API_HASH",None)
    BOT_TOKEN = getenv("BOT_TOKEN",None)
    NORDED_SESSION = getenv("NORDED_SESSION",None)
    NORD_ADMINS = list(map(int, getenv("NORD_ADMINS").split()))
    CHAT_ID = list(map(int, getenv("CHAT_ID").split()))
    DYNO = getenv("DYNO",None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME",None)
    HEROKU_API_KEY = getenv("HEROKU_API_KEY",None)
    CLEANER = int(getenv("CLEANER",None))
    BOT_USERNAME = getenv("BOT_USERNAME",None)
    if BOT_USERNAME.startswith("@"):
        BOT_USERNAME = BOT_USERNAME
    else:
        BOT_USERNAME = "@"+BOT_USERNAME
else:
    NORD_ADMINS = list(map(int, getenv("NORD_ADMINS", "").split()))
    CHAT_ID = list(map(int, getenv("CHAT_ID", "").split()))
    NORDED_SESSION=getenv("NORDED_SESSION")
    BOT_USERNAME=getenv("BOT_USERNAME")
    BOT_TOKEN=getenv("BOT_TOKEN")
    API_HASH=getenv("API_HASH")
    CLEANER=getenv("CLEANER")
    API_ID=getenv("API_ID")
    DYNO=getenv("DYNO")
    HEROKU_API_KEY=None
    HEROKU_APP_NAME=None


    cprint(API_ID,"cyan")
    cprint(API_HASH,"cyan")
    cprint(NORD_ADMINS,"cyan")
    cprint(CHAT_ID,"cyan")
    cprint(BOT_TOKEN,"cyan")
    cprint(BOT_USERNAME,"cyan")

'''
.................................................................
Environment area and depends 
on either .env or herokuvars
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""

GROUP_CALLS = {}
FFMPEG_PROCESSES = {}
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
—••÷[🕊NORDED🕊]÷••— 
userbot client start point
.................................................................
'''

𝙽𝙾𝚁𝙳𝙴𝙳 = Client(
session_name=NORDED_SESSION,
api_id=API_ID,
api_hash=API_HASH
)

'''
.................................................................
—••÷[🕊NORDED🕊]÷••— 
userbot client start point
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
—••÷[🕊NORDED🕊]÷••— 
Bot client start point
.................................................................
'''

𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃 = Client(
bot_token=BOT_TOKEN,
api_id=API_ID,
api_hash=API_HASH,
session_name="𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃"
)
heroku_api = "https://api.heroku.com"
group_calls = NORDCALLER

'''
.................................................................
—••÷[🕊NORDED🕊]÷••— 
Bot client start point
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

DURATION_AUTOPLAY_MIN = 10
LICENSE =""""[—••÷[🕊NORDED🕊]÷••—Telegram Music player userbot has been licensed under GNU General Public License 𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀.GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2007 Free Software Foundation,Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.](https://github.com/HypeVoidSoul/Xeronoid/blob/VOID/LICENSE)"""
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
nordlinker="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg"
norderror = "https://telegra.ph/file/3b0adb8bdcf025bd61ccd.mp4"
nordanimer="https://telegra.ph/file/745b406e98758fe8c9089.gif"
ӼɛӼօ = "[•NORDED•🎧](https://t.me/hypevoidbot) **by** [🔺ΉYPΣ VӨID LΛB](https://t.me/hypevoidbot)\n🕊==========================🕊\n\n"
LINK = "(https://en.wikipedia.org/wiki/GNU_General_Public_License#:~:text=The%20GNU%20General%20Public%20License,share%2C%20and%20modify%20the%20software.&text=Prominent%20free%20software%20programs%20licensed,GNU%20Compiler%20Collection%20(GCC)"
DURATION_PLAY_HOUR = 3
HRKU = heroku3.from_key(HEROKU_API_KEY)
NordFix = prefixes=DYNO

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

MEMBER_CATEG=f"""{ӼɛӼօ}[𝗠𝗲𝗺𝗯𝗲𝗿_𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}stream**
•♪ 𝘙𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦 𝘵𝘰 𝘱𝘭𝘢𝘺/𝘲𝘶𝘦𝘶𝘦 𝘵𝘰 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
**{DYNO}stream**
•♪ 𝘜𝘴𝘦 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬𝘰𝘶𝘵 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
**{DYNO}ping**   
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘵𝘩𝘦 𝘱𝘪𝘯𝘨 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
**{DYNO}license**
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘭𝘪𝘤𝘦𝘯𝘴𝘦 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
**{DYNO}yt**
•♪ __Direct youtube music download and play with 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.__
"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

ADMIN_CATEG=f"""{ӼɛӼօ}[𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}norded** 
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘸𝘩𝘦𝘳𝘦 𝘪𝘴 𝘵𝘩𝘦 —••÷[🕊NORDED🕊]÷••—𝘶𝘴𝘦𝘳𝘣𝘰𝘵 𝘱𝘭𝘶𝘨𝘨𝘦𝘥.
**{DYNO}plug**   
•♪ —••÷[🕊NORDED🕊]÷••—𝘑𝘰𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
**{DYNO}unplug** 
•♪ 𝘓𝘦𝘢𝘷𝘦 𝘵𝘩𝘦 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵 𝘸𝘩𝘦𝘳𝘦 —••÷[🕊NORDED🕊]÷••—𝘸𝘢𝘴 𝘱𝘭𝘢𝘺𝘪𝘯𝘨.
**{DYNO}end**    
•♪ 𝘊𝘭𝘦𝘢𝘯 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘢𝘯𝘥 𝘴𝘵𝘰𝘱 𝘢𝘭𝘭 𝘮𝘶𝘴𝘪𝘤.
**{DYNO}pause**  
•♪ 𝘗𝘢𝘶𝘴𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
**{DYNO}resume** 
•♪ 𝘜𝘯-𝘱𝘢𝘶𝘴𝘦 𝘵𝘩𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
**{DYNO}replay** 
•♪ 𝘗𝘭𝘢𝘺 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘦𝘨𝘪𝘯𝘯𝘪𝘯𝘨 𝘰𝘨 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘪𝘯𝘨 𝘱𝘭𝘢𝘺𝘦𝘥.
**{DYNO}next**   
•♪ 𝘔𝘰𝘷𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘯𝘦𝘹𝘵 𝘵𝘳𝘢𝘤𝘬 𝘰𝘳 𝘚𝘬𝘪𝘱 𝘵𝘳𝘢𝘤𝘬 𝘪𝘯 𝘲𝘶𝘦𝘶𝘦 𝘭𝘪𝘬𝘦 : "𝘯𝘦𝘹𝘵 2".
**{DYNO}temp**   
•♪ 𝘊𝘭𝘦𝘢𝘯 𝘵𝘦𝘮𝘱 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘴𝘦𝘳𝘷𝘦𝘳 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

HEROKU_CATEG=f"""{ӼɛӼօ}[𝗛𝗲𝗿𝗼𝗸𝘂 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}\n
**{DYNO}shutdown**
•♪ 𝘛𝘶𝘳𝘯 𝘰𝘧𝘧 𝘏𝘌𝘙𝘖𝘒𝘜 𝘋𝘺𝘯𝘰 𝘧𝘰𝘳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
**{DYNO}restart**
•♪ 𝘙𝘦𝘣𝘰𝘰𝘵 —••÷[🕊NORDED🕊]÷••—𝘮𝘢𝘯𝘶𝘢𝘭𝘭𝘺 𝘪𝘯 𝘏𝘌𝘙𝘖𝘒𝘜.
**{DYNO}usage**  
•♪ 𝘍𝘪𝘯𝘥 —••÷[🕊NORDED🕊]÷••—𝘏𝘌𝘙𝘖𝘒𝘜 𝘥𝘺𝘯𝘰 𝘶𝘴𝘢𝘨𝘦
"""
INFO_CATEG = f"""{ӼɛӼօ}**__Please press below buttons to check the available commands.__**

⛵️Ðêv Mêñ†ïðñ§:
    @HypeVoidoul
    @HypeVoidBot
"""
NORN = f"""{ӼɛӼօ}**__Audio is here.__**\n**Please reply to the audio file with** /stream"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''

XERO_HELP = f"""{ӼɛӼօ}[𝗠𝗲𝗺𝗯𝗲𝗿_𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
**{DYNO}stream**   
•♪ 𝘙𝘦𝘱𝘭𝘺 𝘵𝘰 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦 𝘵𝘰 𝘱𝘭𝘢𝘺/𝘲𝘶𝘦𝘶𝘦 𝘵𝘰 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
`{DYNO}stream`   
•♪ 𝘜𝘴𝘦 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬𝘰𝘶𝘵 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
`{DYNO}ping`   
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘵𝘩𝘦 𝘱𝘪𝘯𝘨 𝘴𝘵𝘢𝘵𝘶𝘴 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
`{DYNO}license`
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘭𝘪𝘤𝘦𝘯𝘴𝘦 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.\n\n[𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
`{DYNO}norded` 
•♪ 𝘊𝘩𝘦𝘤𝘬 𝘸𝘩𝘦𝘳𝘦 𝘪𝘴 𝘵𝘩𝘦 —••÷[🕊NORDED🕊]÷••—𝘶𝘴𝘦𝘳𝘣𝘰𝘵 𝘱𝘭𝘶𝘨𝘨𝘦𝘥.
`{DYNO}plug`   
•♪ —••÷[🕊NORDED🕊]÷••—𝘑𝘰𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
`{DYNO}unplug` 
•♪ 𝘓𝘦𝘢𝘷𝘦 𝘵𝘩𝘦 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵 𝘸𝘩𝘦𝘳𝘦 —••÷[🕊NORDED🕊]÷••—𝘸𝘢𝘴 𝘱𝘭𝘢𝘺𝘪𝘯𝘨.
`{DYNO}end`    
•♪ 𝘊𝘭𝘦𝘢𝘯 𝘵𝘩𝘦 𝘱𝘭𝘢𝘺𝘭𝘪𝘴𝘵 𝘢𝘯𝘥 𝘴𝘵𝘰𝘱 𝘢𝘭𝘭 𝘮𝘶𝘴𝘪𝘤.
`{DYNO}pause`  
•♪ 𝘗𝘢𝘶𝘴𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
`{DYNO}resume` 
•♪ 𝘜𝘯-𝘱𝘢𝘶𝘴𝘦 𝘵𝘩𝘦 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘨𝘳𝘰𝘶𝘱 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵.
`{DYNO}replay` 
•♪ 𝘗𝘭𝘢𝘺 𝘧𝘳𝘰𝘮 𝘵𝘩𝘦 𝘣𝘦𝘨𝘪𝘯𝘯𝘪𝘯𝘨 𝘰𝘨 𝘤𝘶𝘳𝘳𝘦𝘯𝘵 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘪𝘯𝘨 𝘱𝘭𝘢𝘺𝘦𝘥.
`{DYNO}next`   
•♪ 𝘔𝘰𝘷𝘦 𝘵𝘰 𝘵𝘩𝘦 𝘯𝘦𝘹𝘵 𝘵𝘳𝘢𝘤𝘬 𝘰𝘳 𝘚𝘬𝘪𝘱 𝘵𝘳𝘢𝘤𝘬 𝘪𝘯 𝘲𝘶𝘦𝘶𝘦 𝘭𝘪𝘬𝘦 : "𝘯𝘦𝘹𝘵 2".
`{DYNO}temp`   
•♪ 𝘊𝘭𝘦𝘢𝘯 𝘵𝘦𝘮𝘱 𝘢𝘶𝘥𝘪𝘰 𝘧𝘪𝘭𝘦𝘴 𝘪𝘯 𝘴𝘦𝘳𝘷𝘦𝘳 𝘰𝘧 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.\n\n[𝗛𝗲𝗿𝗼𝗸𝘂 𝗔𝗱𝗺𝗶𝗻 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀]{LINK}
`{DYNO}shutdown`
•♪ 𝘛𝘶𝘳𝘯 𝘰𝘧𝘧 𝘏𝘌𝘙𝘖𝘒𝘜 𝘋𝘺𝘯𝘰 𝘧𝘰𝘳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
`{DYNO}restart`
•♪ 𝘙𝘦𝘣𝘰𝘰𝘵 —••÷[🕊NORDED🕊]÷••—𝘮𝘢𝘯𝘶𝘢𝘭𝘭𝘺 𝘪𝘯 𝘏𝘌𝘙𝘖𝘒𝘜.
`{DYNO}usage`  
•♪ 𝘍𝘪𝘯𝘥 —••÷[🕊NORDED🕊]÷••—𝘏𝘌𝘙𝘖𝘒𝘜 𝘥𝘺𝘯𝘰 𝘶𝘴𝘢𝘨𝘦
"""

'''
.................................................................
Some Bot and Userbot 
Variables and not to be changed
.................................................................
'''
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
PHONE_NUMBER_TEXT = """
Now send your Telegram account's Phone number in International Format.Including Country code. 
Example: **+919000000000**

ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
OTP =  """
÷•• ᴀɴ ᴏᴛᴘ ɪꜱ ꜱᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ

÷•• ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ᴏᴛᴘ ɪɴ `1 2 3 4 5` [**DO NOT FORGET SPACES IN BETWEEN**]

÷•• ɪꜰ 𝕡𝕪𝕣𝕠𝕘𝕣𝕒𝕞 ɴᴏᴛ ꜱᴇɴᴅɪɴɢ ᴏᴛᴘ ᴛʜᴇɴ ᴛʀʏ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴛᴀꜱᴋ ᴀɢᴀɪɴ ᴡɪᴛʜ /start ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʙᴏᴛ.



ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.
"""
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"""
𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐩𝐥𝐚𝐲/𝐪𝐮𝐞𝐮𝐞 𝐭𝐨 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝐔𝐬𝐞 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤𝐨𝐮𝐭 𝐭𝐡𝐞 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐨𝐟 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐩𝐢𝐧𝐠 𝐬𝐭𝐚𝐭𝐮𝐬 𝐨𝐟 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️. 
𝐂𝐡𝐞𝐜𝐤 𝐥𝐢𝐜𝐞𝐧𝐬𝐞 𝐨𝐟 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝐂𝐡𝐞𝐜𝐤 𝐰𝐡𝐞𝐫𝐞 𝐢𝐬 𝐭𝐡𝐞 —••÷[🕊NORDED🕊]÷••—𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐩𝐥𝐮𝐠𝐠𝐞𝐝
𝐉𝐨𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐋𝐞𝐚𝐯𝐞 𝐭𝐡𝐞 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭 𝐰𝐡𝐞𝐫𝐞 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️. 𝐰𝐚𝐬 𝐩𝐥𝐚𝐲𝐢𝐧𝐠.
𝐂𝐥𝐞𝐚𝐧 𝐭𝐡𝐞 𝐩𝐥𝐚𝐲𝐥𝐢𝐬𝐭 𝐚𝐧𝐝 𝐬𝐭𝐨𝐩 𝐚𝐥𝐥 𝐦𝐮𝐬𝐢𝐜..
𝐏𝐚𝐮𝐬𝐞 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐔𝐧-𝐩𝐚𝐮𝐬𝐞 𝐭𝐡𝐞 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐏𝐥𝐚𝐲 𝐟𝐫𝐨𝐦 𝐭𝐡𝐞 𝐛𝐞𝐠𝐢𝐧𝐧𝐢𝐧𝐠 𝐨𝐠 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐦𝐮𝐬𝐢𝐜 𝐛𝐞𝐢𝐧𝐠 𝐩𝐥𝐚𝐲𝐞𝐝.
𝐌𝐨𝐯𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐧𝐞𝐱𝐭 𝐭𝐫𝐚𝐜𝐤 𝐨𝐫 𝐒𝐤𝐢𝐩 𝐭𝐫𝐚𝐜𝐤 𝐢𝐧 𝐪𝐮𝐞𝐮𝐞 𝐥𝐢𝐤𝐞 : "𝐧𝐞𝐱𝐭 𝟐".
𝐂𝐥𝐞𝐚𝐧 𝐭𝐞𝐦𝐩 𝐚𝐮𝐝𝐢𝐨 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 𝐬𝐞𝐫𝐯𝐞𝐫 𝐨𝐟 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝐓𝐮𝐫𝐧 𝐨𝐟𝐟 𝐇𝐄𝐑𝐎𝐊𝐔 𝐃𝐲𝐧𝐨 𝐟𝐨𝐫 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝐑𝐞𝐛𝐨𝐨𝐭 —••÷[🕊NORDED🕊]÷••—𝐦𝐚𝐧𝐮𝐚𝐥𝐥𝐲 𝐢𝐧 𝐇𝐄𝐑𝐎𝐊𝐔.
𝐅𝐢𝐧𝐝 —••÷[🕊NORDED🕊]÷••—𝐇𝐄𝐑𝐎𝐊𝐔 𝐝𝐲𝐧𝐨 𝐮𝐬𝐚𝐠𝐞

𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝗮𝘂𝗱𝗶𝗼 𝗳𝗶𝗹𝗲 𝘁𝗼 𝗽𝗹𝗮𝘆/𝗾𝘂𝗲𝘂𝗲 𝘁𝗼 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗨𝘀𝗲 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸𝗼𝘂𝘁 𝘁𝗵𝗲 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁 𝗼𝗳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗖𝗵𝗲𝗰𝗸 𝘁𝗵𝗲 𝗽𝗶𝗻𝗴 𝘀𝘁𝗮𝘁𝘂𝘀 𝗼𝗳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗖𝗵𝗲𝗰𝗸 𝗹𝗶𝗰𝗲𝗻𝘀𝗲 𝗼𝗳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗖𝗵𝗲𝗰𝗸 𝘄𝗵𝗲𝗿𝗲 𝗶𝘀 𝘁𝗵𝗲 —••÷[🕊NORDED🕊]÷••—𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗽𝗹𝘂𝗴𝗴𝗲𝗱
𝗝𝗼𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗟𝗲𝗮𝘃𝗲 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝘄𝗵𝗲𝗿𝗲 —••÷[🕊NORDED🕊]÷••—𝘄𝗮𝘀 𝗽𝗹𝗮𝘆𝗶𝗻𝗴.
𝗖𝗹𝗲𝗮𝗻 𝘁𝗵𝗲 𝗽𝗹𝗮𝘆𝗹𝗶𝘀𝘁 𝗮𝗻𝗱 𝘀𝘁𝗼𝗽 𝗮𝗹𝗹 𝗺𝘂𝘀𝗶𝗰..
𝗣𝗮𝘂𝘀𝗲 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗨𝗻-𝗽𝗮𝘂𝘀𝗲 𝘁𝗵𝗲 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁.
𝗣𝗹𝗮𝘆 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗯𝗲𝗴𝗶𝗻𝗻𝗶𝗻𝗴 𝗼𝗴 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗺𝘂𝘀𝗶𝗰 𝗯𝗲𝗶𝗻𝗴 𝗽𝗹𝗮𝘆𝗲𝗱.
𝗠𝗼𝘃𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝘁𝗿𝗮𝗰𝗸 𝗼𝗿 𝗦𝗸𝗶𝗽 𝘁𝗿𝗮𝗰𝗸 𝗶𝗻 𝗾𝘂𝗲𝘂𝗲 𝗹𝗶𝗸𝗲 : "𝗻𝗲𝘅𝘁 𝟮".
𝗖𝗹𝗲𝗮𝗻 𝘁𝗲𝗺𝗽 𝗮𝘂𝗱𝗶𝗼 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘀𝗲𝗿𝘃𝗲𝗿 𝗼𝗳 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗧𝘂𝗿𝗻 𝗼𝗳𝗳 𝗛𝗘𝗥𝗢𝗞𝗨 𝗗𝘆𝗻𝗼 𝗳𝗼𝗿 🎧NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ©️.
𝗥𝗲𝗯𝗼𝗼𝘁 —••÷[🕊NORDED🕊]÷••—𝗺𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝗶𝗻 𝗛𝗘𝗥𝗢𝗞𝗨.
𝗙𝗶𝗻𝗱 —••÷[🕊NORDED🕊]÷••—𝗛𝗘𝗥𝗢𝗞𝗨 𝗱𝘆𝗻𝗼 𝘂𝘀𝗮𝗴𝗲
"""
NORDEDBΣ=f"""{ӼɛӼօ}`ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɴᴏʀᴅ ᴀᴅᴍɪɴꜱ ᴏꜰ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴡʜᴇʀᴇ —••÷[🕊NORDED🕊]÷••—ɪꜱ ᴘʟᴜɢɢᴇᴅ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.`
**__If needed to know the commands then use /nord__**

[𝗣𝗹𝗲𝗮𝘀𝗲 𝘂𝘀𝗲 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽𝘀.](https://t.me/hypevoids)"""
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def Nord_Verity(_, __, ΣOЯ: NordLink):
    if ΣOЯ.from_user.id in NORD_ADMINS:
        return True
    return False
Nord_Admins = filters.create(Nord_Verity)
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def Nord_Connected(_, __, ΣOЯ: NordLink):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    if not (ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected):
        return False
    return True
Nord_Caller = filters.create(Nord_Connected)
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def Nord_Ghost_Filter(_, __, ΣOЯ: NordLink):
    return bool(
    ΣOЯ.from_user is None 
    and ΣOЯ.sender_chat)
Nord_Ghost = filters.create(Nord_Ghost_Filter)
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
""""""—••÷[🕊NORDED🕊]÷••—


* FROM HERE THE MAIN CODE FOR —••÷[🕊NORDED🕊]÷••— BOT STARTS.
* ALSO FOR ERROR HANDLINGS!


—••÷[🕊NORDED🕊]÷••—"""
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"plug",
NordFix))
async def plug(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"stream",
NordFix))
async def stream(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"next",
NordFix))
async def next(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"nord"))
async def nord(bot, update):
    try:
        try:
            text = INFO_CATEG.format(update.from_user.mention)
            reply_markup = HELP_BUTTONS
            pic=nordlinker
            await update.reply_photo(
            photo=pic,
            caption=text,
            reply_markup=reply_markup)
        except Exception as DΣD:
            ΣOЯ = NordLink
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ}⚠️There was an error processing the previous request.\nPlease check below to learn more\n `__{DΣD}__`")
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_callback_query()
async def cb_data(bot, update):
    try:
        try:
            if update.data == "help":
                await update.message.edit(
                text=INFO_CATEG,
                reply_markup=HELP_BUTTONS
                )
            elif update.data == "Member Commands 💛":
                await update.message.edit(
                text=MEMBER_CATEG,
                reply_markup=MEM_BUTT
                )
            elif update.data == "Admin Commands ⚜️":
                await update.message.edit(
                text=ADMIN_CATEG,
                reply_markup=ADM_BUTT
                )
            elif update.data == "Heroku Commands 🟣":
                await update.message.edit(
                text=HEROKU_CATEG,
                reply_markup=HERO_BUTT
                )
            elif update.data == "Exit Help Menu🔺":
                await update.message.delete()
            else:
                return False
        except Exception as DΣD:
            ΣOЯ = NordLink
            await ΣOЯ.reply_photo(
            photo=nordlinker,caption=f"""{ӼɛӼօ}⚠️There was an error processing the previous request.
            Please check below to learn more
            
            
            `__{DΣD}__`""")
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"norded",
NordFix))
async def norded(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"end",
NordFix))
async def end(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"replay",
NordFix))
async def replay(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"pause",
NordFix))
async def pause(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"resume",
NordFix))
async def resume(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"temp",
NordFix))
async def temp(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"ping",
NordFix))
async def ping_pong(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            start = datetime.now()
            end = datetime.now()
            delta_energy1 = (end - start).seconds
            delta_energy2= (end - start).microseconds
            psychodelic = await ΣOЯ.reply_photo(
            norderror,
            caption=f"""{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n
    |   𝚂𝚎𝚛𝚟𝚎𝚛 𝚛𝚎𝚜𝚙𝚘𝚗𝚜𝚎 𝚝𝚒𝚖𝚎 𝚒𝚜   |
            📡 **{delta_energy1}** `𝙨𝙚𝙘𝙤𝙣𝙙𝙨` 
            📡 **{delta_energy2}** `𝙢𝙞𝙘𝙧𝙤𝙨𝙚𝙘𝙤𝙣𝙙𝙨`
    """,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"license"))
async def on_license(
_,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=LICENSE,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& filters.command("start"))
async def on_start(
_,
ΣOЯ: NordLink):
    try:
        try:
            try:
                PERM = await ΣOЯ.reply_text("**CHECKING BOT PERMISSIONS.........**")
                await asyncio.sleep(2)
                await PERM.delete()
                await ΣOЯ.delete()
            except Exception:
                await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"""{ӼɛӼօ}
        @Admins Please make [🔹 𝗡Ө𝗥𝗗Σ𝗗_𝗣LΛ𝗬Σ𝗥 🔹](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg) admin.

        **Bot is missing required permissions to work properly.**
            `❌ CHAT_ADMIN`
            `❌ RIGHT TO DELETE`
            `❌ RIGHT TO PIN MESSAGE`

        __Once given proper right, bot will stop sending any such error notifications.__
        """,
            disable_notification=False)
        except Exception as DΣD:
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command(
"start"))
async def on_start(
_,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"""{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n
        **I am** [🔹 𝗡Ө𝗥𝗗Σ𝗗_𝗣LΛ𝗬Σ𝗥 🔹](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg) **for playing music in the voice chats of Telegram Groups & Channels**.

        Send me `/nord` for more info.""",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
async def roku():
    try:
        HEROKU = heroku3.from_key(HEROKU_API_KEY)
        app = HEROKU.apps()[HEROKU_APP_NAME]
        app.restart()
        ΣOЯ: NordLink
        await ΣOЯ.reply_photo(
        photo=nordlinker,
        caption=f"{ӼɛӼօ} **𝙽𝙾𝚁𝙳𝙴𝙳 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣𝙚𝙙 𝙪𝙥 𝙖𝙣𝙙 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙞𝙩𝙨𝙚𝙡𝙛!**",
        reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🕊DΣV GЯӨЦP",
        url=f"https://t.me/hypevoids",),],[
        InlineKeyboardButton(
        text="🤖 ΉYPΣ VӨID BӨT",
        url=f"https://t.me/hypevoidbot")
        ]]))
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& Nord_Admins
& filters.command(
"restart",
NordFix))
async def restart(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None:
                await ΣOЯ.delete()
                ΣOЯPS = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️   𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝗿𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗛𝗲𝗿𝗼𝗸𝘂-𝗗𝘆𝗻𝗼.\n𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 𝙛𝙤𝙧 30𝙨𝙚𝙘-1𝙢𝙞𝙣",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                await roku()
                # await asyncio.sleep(15)
                # await ΣOЯPS.delete()
                # await ΣOЯ.reply_photo(
                # photo=nordlinker,
                # caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n  **𝙽𝙾𝚁𝙳𝙴𝙳 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣𝙚𝙙 𝙪𝙥 𝙖𝙣𝙙 𝙧𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙞𝙩𝙨𝙚𝙡𝙛!**",
                # reply_markup=InlineKeyboardMarkup([[
                # InlineKeyboardButton(
                # text="🕊DΣV GЯӨЦP",
                # url=f"https://t.me/hypevoids",),],[
                # InlineKeyboardButton(
                # text="🤖 ΉYPΣ VӨID BӨT",
                # url=f"https://t.me/hypevoidbot")
                # ]]))
                # lic = await ΣOЯ.reply_photo(
                # photo=nordlinker,
                # caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n{LICENSE}")
                # await asyncio.sleep(12)
                # await lic.delete()
            else:
                if HEROKU_API_KEY is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️   𝗦𝗲𝗲𝗺𝘀 𝗹𝗶𝗸𝗲 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝗲𝘁 𝗮𝗻 𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗜_𝗞𝗘𝗬.\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                elif HEROKU_APP_NAME is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️   𝗦𝗲𝗲𝗺𝘀 𝗹𝗶𝗸𝗲 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝗲𝘁 𝗮𝗻 𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗣_𝗡𝗔𝗠𝗘.\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                elif HEROKU_API_KEY is None and HEROKU_APP_NAME is None:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️   𝗦𝗲𝗲𝗺𝘀 𝗹𝗶𝗸𝗲 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘀𝗲𝘁 𝗮𝗻 𝗶𝗻𝗰𝗼𝗿𝗿𝗲𝗰𝘁 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗜_𝗞𝗘𝗬 𝗮𝗻𝗱 𝗛𝗘𝗥𝗢𝗞𝗨_𝗔𝗣𝗣_𝗡𝗔𝗠𝗘.\n𝗣𝗹𝗲𝗮𝘀𝗲 𝗳𝗶𝘅 𝗶𝘁 𝗮𝗻𝗱 𝗯𝗼𝘁 𝘄𝗶𝗹𝗹 𝘄𝗼𝗿𝗸 𝗽𝗲𝗿𝗳𝗲𝗰𝘁𝗹𝘆",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                else:
                    await ΣOЯ.delete()
                    await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n  𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐥𝐨𝐠𝐬 𝐭𝐨 @HypeVoids 𝐢𝐟 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐰𝐫𝐨𝐧𝐠 𝐡𝐚𝐩𝐩𝐞𝐧𝐬",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~filters.edited
& Nord_Admins
& filters.command(
"shutdown",
NordFix))
async def shutdown(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            shuts = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️  `𝗧𝘂𝗿𝗶𝗻𝗴 𝗢𝗳𝗳 𝗛𝗲𝗿𝗼𝗸𝘂 𝗗𝘆𝗻𝗼𝘀 𝗳𝗼𝗿 NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿.\n𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆 𝘁𝘂𝗿𝗻 𝗶𝘁 𝗼𝗻 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻.`")
            await asyncio.sleep(2)
            await shuts.delete()
            if HEROKU_APP_NAME is not None:
                HEROKU_APP_NAME.process_formation()["worker"].scale(0)
            else:
                sys.exit()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        sys.exit()
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.command("usage",
NordFix))
async def usage(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            event = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️  **𝗔𝘀𝗸𝗶𝗻𝗴 𝗛𝗲𝗿𝗼𝗸𝘂 𝗮𝗻𝗱 𝗣𝗿𝗼𝗰𝗲𝘀𝘀𝗶𝗻𝗴 𝗥𝗲𝗾𝘂𝗲𝘀𝘁**")
            useragent = (
                "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/80.0.3987.149 Mobile Safari/537.36"
            )
            user_id = HRKU.account().id
            headers = {
                "User-Agent": useragent,
                "Authorization": f"Bearer {HEROKU_API_KEY}",
                "Accept": "application/vnd.heroku+json; version=3.account-quotas",
            }
            path = "/accounts/" + user_id + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                return await event.edit(
                    "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
                )
            result = r.json()
            quota = result["account_quota"]
            quota_used = result["quota_used"]

            """ - Used - """
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)

            """ - Current - """
            App = result["apps"]
            try:
                App[0]["quota_used"]
            except IndexError:
                AppQuotaUsed = 0
                AppPercentage = 0
            else:
                AppQuotaUsed = App[0]["quota_used"] / 60
                AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
            AppHours = math.floor(AppQuotaUsed / 60)
            AppMinutes = math.floor(AppQuotaUsed % 60)
            await asyncio.sleep(1.5)
            return await event.edit(f""""
        👾 **Dyno Usage** 👾:\n\n
        ➠ __Dyno usage for__ • **{HEROKU_APP_NAME}** • :\n
            ★  `{AppHours}**h**  `{AppMinutes}**YΣ**  
        **|**  `{AppPercentage}**%**"
        ➠ __Dyno hours remaining this month__ :\n
            ★  `{hours}**h**  `{minutes}**YΣ**  
        **|**  `{percentage}**%**""")
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"LET ME TRY TO MAKE THE CODE FOR DIRECT YOUTUBE PLAY USING /yt COMMAND"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& Nord_Caller
& ~filters.edited
& filters.command(
"yt",
NordFix))
def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            ΣOЯ.delete()
            query = ''
            for i in ΣOЯ.command[1:]:
                query += ' ' + str(i)
            ydl_opts = {
            "format":
            "bestaudio[ext=m4a]"}
            try:
                results = []
                count = 0
                while len(results) == 0 and count < 6:
                    if count>0:
                        results = YoutubeSearch(
                        query,
                        max_results=1).to_dict()
                    count += 1
                try:
                    psychode =  ΣOЯ.reply_photo(
                    animation="worklord/norded_dling.gif",
                    duration=4,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n[Please Wait till](https://t.me/hypevoidbot) **🔹 𝗡Ө𝗥𝗗Σ𝗗_𝗣LΛ𝗬Σ𝗥 🔹** [downloads and converts Audio for streaming in the group voice chat!](https://t.me/hypevoidbot)")
                    link = f"https://youtube.com{results[0]['url_suffix']}"
                    title = results[
                    0][
                    "title"]
                    thumbnail = results[
                    0][
                    "thumbnails"][
                    0]
                    duration = results[0][
                    "duration"]
                    views = results[
                    0][
                    "views"]
                    NORDED_THUMBNAIL = f'🎧•NORDED•🎧 by 🔥ΉYPΣ VӨID LΛB🔥-𝙽𝙾𝚁𝙳𝙴𝙳{ΣOЯ.message_id}.jpg'
                    thumb = requests.get(
                    thumbnail,
                    allow_redirects=False)#True
                    open(
                    NORDED_THUMBNAIL,
                    'wb').write(
                    thumb.content
                    )

                except Exception as DΣD:
                    psychodelic =  ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"""
                    {ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n✖️**𝗙𝗼𝘂𝗻𝗱 𝗻𝗼𝘁𝗵𝗶𝗻𝗴. 𝗧𝗿𝘆 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘁𝗵𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗮 𝗹𝗶𝘁𝘁𝗹𝗲.**\n\n\n**Please Inform @HypeVoidSoul or @HypeVoids:>>**\n`{DΣD}`""",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                    asyncio.sleep(
                CLEANER
                )
                    psychodelic.delete()
                    return
                    
            except Exception as DΣD:
                psychodelic = ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"""
                {ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n✖️ **𝙁𝙤𝙪𝙣𝙙 𝙉𝙤𝙩𝙝𝙞𝙣𝙜. 𝙎𝙤𝙧𝙧𝙮.**\n\n**𝗧𝗿𝘆 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝗼𝗿 𝗺𝗮𝘆𝗯𝗲 𝘀𝗽𝗲𝗹𝗹 𝗶𝘁 𝗽𝗿𝗼𝗽𝗲𝗿𝗹𝘆.**\n\n\n**Please Inform @HypeVoidSoul or @HypeVoids:>>**\n`{DΣD}`""",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                asyncio.sleep(
                CLEANER
                )
                psychodelic.delete()
                return
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as nordl:
                    info_dict = nordl.extract_info(
                    link,
                    download=False
                    )
                    audio_file = nordl.prepare_filename(
                    info_dict
                    )
                    nordl.process_info(
                    info_dict
                    )

                nordlcap = f"""
    📜`ᴀᴜᴅɪᴏ ᴛɪᴛʟᴇ`: **[{title[:35]}]({link})**
    ⏳`ᴀᴜᴅɪᴏ ᴅᴜʀᴀᴛɪᴏɴ`: **[{duration}]({link})**

    ☢️[𝚃𝚑𝚒𝚜 𝙰𝚞𝚍𝚒𝚘 𝚒𝚜 𝚜𝚎𝚗𝚝 𝚋𝚢](https://t.me/hypevoidbot) **🔹 𝗡Ө𝗥𝗗Σ𝗗_𝗣LΛ𝗬Σ𝗥 🔹** [𝚏𝚘𝚛 𝚘𝚗𝚕𝚢 𝚜𝚝𝚛𝚎𝚊𝚖𝚒𝚐 𝚒𝚗 𝚅𝙾𝙸𝙲𝙴_𝙲𝙷𝙰𝚃𝚂.](https://t.me/hypevoidbot)❗️
    🤖[𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 𝘉𝘦𝘭𝘰𝘸 𝘉𝘰𝘵𝘴 𝘵𝘰 𝘥𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘢𝘯𝘺 𝘰𝘵𝘩𝘦𝘳 𝘠𝘰𝘶𝘛𝘶𝘣𝘦 𝘝𝘪𝘥𝘦𝘰/𝘈𝘶𝘥𝘪𝘰 𝘪𝘯 𝘜𝘏𝘋](https://t.me/hypevoidbot)
    """
                secmul, dur, dur_arr = 1, 0, duration.split(':')
                for i in range(len(dur_arr)-1, -1, -1):
                    dur += (int(
                    dur_arr[i]) * secmul)
                    secmul *= 60

                psychode.delete()
                psychoded = ΣOЯ.reply_photo(
                animation="https://telegra.ph/file/c8f986b67bb8b3ab566b3.mp4",
                caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n🔥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ꜰɪɴɪꜱʜᴇᴅ\n𝗔𝘂𝗱𝗶𝗼 𝗯𝗲𝗶𝗻𝗴 𝗽𝗿𝗲𝗽𝗱 𝗳𝗼𝗿 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴 𝘂𝘀𝗶𝗻𝗴 **🔹 𝗡Ө𝗥𝗗Σ𝗗_𝗣LΛ𝗬Σ𝗥 🔹**"
                )

                ADU = ΣOЯ.reply_audio(
                audio=audio_file,
                caption=nordlcap,
                title=title,
                duration=dur,
                thumb=NORDED_THUMBNAIL,
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="📷 YouTube Downloader",
                url=f"https://t.me/HVYouTubeBot",),],[
                InlineKeyboardButton(
                text="⭕️ YouTube Music Downloader",
                url=f"https://t.me/HVYouTubeMusicBot",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))

                psychoded.delete()
                ADU.reply_photo(
                photo=NORDED_THUMBNAIL,
                caption=NORN
                )
                asyncio.sleep(CLEANER)


            except Exception as DΣD:
                psychodelic = ΣOЯ.reply_text(f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n❌ Error\n\n`{DΣD}`")
                psychodelic.delete()
            try:
                os.remove(audio_file)
                os.remove(NORDED_THUMBNAIL)
                os.system("clear")
                cprint("Success and Cleared Screen", "cyan")
            except Exception as DΣD:
                psychodelic = ΣOЯ.reply_text(f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n❌ Error cleaning yt temp files.\n\n`{DΣD}`")
        except Exception as DΣD:
            ΣOЯ.reply_photo(
            animation=norderror,
            caption=f"""{ӼɛӼօ}
        🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
# @𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
# filters.chat(
# CHAT_ID)
# & Nord_Caller
# & ~filters.edited
# & filters.command(
# "ytlicoius",
# NordFix))
# async def yt(
# client,
# ΣOЯ: NordLink):
#     try:
#         mntn = ΣOЯ.from_user.mention
#         await ΣOЯ.delete()
#         query = ''
#         for i in ΣOЯ.command[1:]:
#             query += ' ' + str(i)
#         ydl_opts = {
#         "format":
#         "bestaudio[ext=m4a]"}
#         try:
#             results = []
#             count = 0
#             while len(results) == 0 and count < 6:
#                 if count>0:
#                     results = YoutubeSearch(
#                     query,
#                     max_results=1).to_dict()
#                 count += 1
#             try:
#                 link = f"https://youtube.com{results[0]['url_suffix']}"
#                 title = results[
#                 0][
#                 "title"]
#                 thumbnail = results[
#                 0][
#                 "thumbnails"][
#                 0]
#                 duration = results[0][
#                 "duration"]
#                 views = results[
#                 0][
#                 "views"]
#                 NORDED_THUMBNAIL = f'𝙽𝙾𝚁𝙳𝙴𝙳{ΣOЯ.message_id}.jpg'
#                 thumb = requests.get(
#                 thumbnail,
#                 allow_redirects=True)
#                 open(
#                 NORDED_THUMBNAIL,
#                 'wb').write(
#                 thumb.content)
#             except Exception as DΣD:
#                 psychodelic =  await ΣOЯ.reply_photo(
#                 photo=nordlinker,
#                 caption=f"""
#                 {ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n✖️**𝗙𝗼𝘂𝗻𝗱 𝗻𝗼𝘁𝗵𝗶𝗻𝗴. 𝗧𝗿𝘆 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝘁𝗵𝗲 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴 𝗮 𝗹𝗶𝘁𝘁𝗹𝗲.**\n\n\n**Please Inform @HypeVoidSoul or @HypeVoids:>>**\n`{DΣD}`""",
#                 reply_markup=InlineKeyboardMarkup([[
#                 InlineKeyboardButton(
#                 text="🕊DΣV GЯӨЦP",
#                 url=f"https://t.me/hypevoids",),],[
#                 InlineKeyboardButton(
#                 text="🔖ɢɪᴛʜᴜʙ",
#                 url=f"https://t.me/hypevoidbot",),],[
#                 InlineKeyboardButton(
#                 text="🤖 ΉYPΣ VӨID BӨT",
#                 url=f"https://t.me/hypevoidbot")
#                 ]]))
#                 await asyncio.sleep(
#            CLEANER
#           )
#                 await psychodelic.delete()
#                 return
#         except Exception as DΣD:
#             psychodelic = await ΣOЯ.reply_photo(
#             photo=nordlinker,
#             caption=f"""
#             {ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n✖️ **𝙁𝙤𝙪𝙣𝙙 𝙉𝙤𝙩𝙝𝙞𝙣𝙜. 𝙎𝙤𝙧𝙧𝙮.**\n\n**𝗧𝗿𝘆 𝗮𝗻𝗼𝘁𝗵𝗲𝗿 𝗸𝗲𝘆𝘄𝗼𝗿𝗱 𝗼𝗿 𝗺𝗮𝘆𝗯𝗲 𝘀𝗽𝗲𝗹𝗹 𝗶𝘁 𝗽𝗿𝗼𝗽𝗲𝗿𝗹𝘆.**\n\n\n**Please Inform @HypeVoidSoul or @HypeVoids:>>**\n`{DΣD}`""",
#             reply_markup=InlineKeyboardMarkup([[
#             InlineKeyboardButton(
#             text="🕊DΣV GЯӨЦP",
#             url=f"https://t.me/hypevoids",),],[
#             InlineKeyboardButton(
#             text="🔖ɢɪᴛʜᴜʙ",
#             url=f"https://t.me/hypevoidbot",),],[
#             InlineKeyboardButton(
#             text="🤖 ΉYPΣ VӨID BӨT",
#             url=f"https://t.me/hypevoidbot")
#             ]]))
#             await asyncio.sleep(
#           CLEANER
#           )
#             await psychodelic.delete()
#             return
#         try:
#             with youtube_dl.YoutubeDL(ydl_opts) as nordl:
#                 info_dict = nordl.extract_info(link, download=False)
#                 audio_file = nordl.prepare_filename(info_dict)
#                 nordl.process_info(info_dict)
#             nordlcap = f'🎧 **Title**: [{title[:35]}]({link})\n⏳ **Duration**: `{duration}`\n👁‍🗨 **Views**: `{views}`'
#             secmul, dur, dur_arr = 1, 0, duration.split(':')
#             for i in range(len(dur_arr)-1, -1, -1):
#                 dur += (int(dur_arr[i]) * secmul)
#                 secmul *= 60
#             chat_id = int(str(ΣOЯ.chat.id))
#             ADU = await ΣOЯ.reply_audio(
#             audio=audio_file,
#             caption=nordlcap,
#             title=title,
#             duration=dur,
#             thumb=NORDED_THUMBNAIL
#             )
#             await ADU.reply_photo(
#             photo=NORDED_THUMBNAIL,
#             caption=NORN,
#             reply_markup=InlineKeyboardMarkup([[
#             InlineKeyboardButton(
#             text="🕊DΣV GЯӨЦP",
#             url=f"https://t.me/hypevoids",),],[
#             InlineKeyboardButton(
#             text="🔖ɢɪᴛʜᴜʙ",
#             url=f"https://t.me/hypevoidbot",),],[
#             InlineKeyboardButton(
#             text="🤖 ΉYPΣ VӨID BӨT",
#             url=f"https://t.me/hypevoidbot")
#             ]]))
#         except Exception as DΣD:
#             psychodelic = await ΣOЯ.reply_text(f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n❌ Error\n\n`{DΣD}`")
#             await psychodelic.delete()
#         try:
#             os.remove(audio_file)
#             os.remove(NORDED_THUMBNAIL)
#         except Exception as DΣD:
#             psychodelic = await ΣOЯ.reply_text(f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n❌ Error cleaning yt temp files.\n\n`{DΣD}`")
#     except Exception as DΣD:
#         await ΣOЯ.reply_photo(
#         photo=nordlinker,
#         caption=
#        f"""{ӼɛӼօ}
# 🕊 {mntn} 🕊 
# ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**\n**ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**\n\n `__{DΣD}__`
# """)
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"stream",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ʜꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/stream]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"pause",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ʜꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/pause]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Admins
& Nord_Caller
& ~filters.edited
& filters.command(
"pause",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.\n𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴"""
    )
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"resume",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/resume]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Admins
& Nord_Caller
& ~filters.edited
& filters.command(
"resume",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.\n𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴"""
    )
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"unplug",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ʜꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/unplug]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()


        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Admins
& Nord_Caller
& ~filters.edited
& filters.command(
"unplug",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.\n𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴"""
    )
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()


        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"vol",
NordFix))
async def volume(
client,
ΣOЯ: NordLink):
    try:
        usage = "**Usage:**\n/volume [1-200]"
        if len(ΣOЯ.command) != 2:
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await psychodelic.delete()
            return

        if "plug" not in db:
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption="VC isn't started"
            )
            await asyncio.sleep(CLEANER)
            await psychodelic.delete()
            return

        vc = db["plug"]
        volume = int(
        ΣOЯ.text.split(
        None, 1)[1])
        if (volume < 1) or (volume > 200):
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await psychodelic.delete()
            return
            
        try:
            await vc.set_my_volume(
            volume=volume
            )       
            return
        except ValueError:
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=usage
            )
            await asyncio.sleep(CLEANER)
            await psychodelic.delete()


        psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=f"**Volume Set To {volume}**"
            )
        await asyncio.sleep(CLEANER)
        await psychodelic.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"temp",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ʜꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/temp]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Admins
& Nord_Caller
& ~filters.edited
& filters.command(
"temp",
NordFix))
async def yt(
client,
ΣOЯ: NordLink):
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    😲🐣𝘚𝘦𝘦𝘮𝘴 𝘭𝘪𝘬𝘦 𝘺𝘰𝘶 𝘢𝘳𝘦 𝘯𝘰𝘵 𝘢 𝘷𝘢𝘭𝘪𝘥 𝘕𝘖𝘙𝘋-𝘈𝘥𝘮𝘪𝘯.\n𝘗𝘭𝘦𝘢𝘴𝘦 𝘶𝘴𝘦 `/nord` 𝘵𝘰 𝘤𝘩𝘦𝘤𝘬 𝘔𝘦𝘮𝘣𝘦𝘳 𝘰𝘯𝘭𝘺 𝘤𝘰𝘮𝘮𝘢𝘯𝘥𝘴"""
    )
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command(
"unplug",
NordFix))
async def unplug(
client,
ΣOЯ: NordLink): 
    try:
        mntn = ΣOЯ.from_user.mention
        await ΣOЯ.delete()
        try:
            await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=NORDEDBΣ,
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**\n**ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**\n\n `__{DΣD}__`
    """)
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
"|"
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.chat(
CHAT_ID
)
& ~Nord_Caller
& ~filters.edited
& filters.command(
"yt",
NordFix))
async def yt(
client,
ΣOЯ: NordLink): 
    try:
        try:
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            psychodelic = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
            f"""{ӼɛӼօ}
    🕊 {mntn} 🕊
    ⚠️`ʜꜱᴇᴇᴍꜱ ʟɪᴋᴇ` —••÷[🕊NORDED🕊]÷••—`ʜᴀꜱ ɴᴏᴛ ʙᴇᴇɴ ᴘʟᴜɢɢᴇᴅ ʏᴇᴛ ᴀɴᴅ` **__{chat.title}__** `ʜᴀꜱ ɪᴛ'ꜱ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ/ᴄᴀʟʟ ɴᴏᴛ ᴄᴏɴɴᴇᴄᴛᴇᴅ ʏᴇᴛ.`\n`ᴘʟᴇᴀꜱᴇ ᴀꜱᴋ ɴᴏʀᴅ-ᴀᴅᴍɪɴꜱ ᴏꜰ` **__{chat.title}__** `ᴛᴏ ᴛᴜʀɴ ɪᴛ ᴏɴ ꜰɪʀꜱᴛ ᴀɴᴅ ʀᴇᴛʀʏ` [/yt SONG.NAME]
    """)
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            await ΣOЯ.reply_text("😵") 
            chat_id = int(str(ΣOЯ.chat.id))
            chat = await client.get_chat(chat_id)
            mntn = ΣOЯ.from_user.mention
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"---------------------------------------------------------------------------------|____🤖NORDEDB🤖____"
"|"
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
""""""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— SESSION_MAKER STARTS
—••÷[🕊NORDED🕊]÷••—"""'''
EXIT module when users do it wrong
'''

async def exit_work(hn, text: str):
    if text.startswith("/exit"):
        await hn.reply("Process Cancelled.")
        return True
    return False

'''
EXIT module when users do it wrong
'''

@𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.on_message(
filters.private
& filters.command("session"))
async def norded(client, hn: NordLink):
    try:
        try:
            await hn.delete()
            chat = hn.chat
            HYPE_ASK_API = await hn.reply_photo(
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_ID` ᴛᴏ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ —••÷[🕊NӨЯDΣD🕊]÷••— ᴘʏʀᴏɢʀᴀᴍ ꜱᴇꜱꜱɪᴏɴ ɴᴀᴍᴇ.


    **ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ʜᴀᴠᴇ ᴇɪᴛʜᴇʀ ᴏꜰ ᴛʜᴏꜱᴇ ᴛʜᴇɴ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ʙᴏᴛ**
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))


            HYPE_API = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
            chat.id,
            f"**÷••>**")


            await HYPE_ASK_API.delete()


            if await exit_work(hn, HYPE_API.text):
                return


            
            try:
                HYPE_API_CHECK = int(HYPE_API.text)
            except Exception:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    `API_ID` ɪꜱ ɪɴᴠᴀʟɪᴅ.
    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return

            
            api_id = HYPE_API.text
            HYPE_ASK_HASK =  await hn.reply_photo(
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ɴᴏᴡ ꜱᴇɴᴅ ʏᴏᴜʀ `API_HASH`.

    ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))

            HYPE_HASH = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
            chat.id,
            f"**÷••>**")
            await HYPE_ASK_HASK.delete()
            await HYPE_API.delete()


            
            if await exit_work(hn, HYPE_HASH.text):
                return


            
            if not len(HYPE_HASH.text) >= 30:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🔴 ＣＯＤＥ－ＲＥＤ 🔴
    `API_HASH` ɪꜱ ɪɴᴠᴀʟɪᴅ.
    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return



            
            api_hash = HYPE_HASH.text
            while True:
                number = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(chat.id,PHONE_NUMBER_TEXT)
                if not number.text:
                    continue
                if await exit_work(hn, number.text):
                    return
                phone = number.text
                HYPE_ASK_Y = await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ɪꜱ ```{phone}``` ᴄᴏʀʀᴇᴄᴛ? (y/n)

    Ｓｅｎｄ： `y` 
    or
    Ｓｅｎｄ： `n` 

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))

                confirm = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
                chat.id,
                f"**÷••>**")
                await HYPE_HASH.delete()

                if await exit_work(hn, confirm.text):
                    return
                if "y" in confirm.text:
                    await  HYPE_ASK_Y.delete()
                    await confirm.delete()
                    break
                



            
            try:
                morphed = Client(
                "my_account",
                api_id=api_id,
                api_hash=api_hash
                )
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                text=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    **ᴇʀʀᴏʀ:** `{str(e)}`
    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            
            try:
                await morphed.connect()
            except ConnectionError:
                await morphed.disconnect()
                await morphed.connect()



            
            try:
                code = await morphed.send_code(phone)
            except FloodWait as e:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ʏᴏᴜ ʜᴀᴠᴇ ꜰʟᴏᴏᴅᴡᴀɪᴛ ᴏꜰ {e.x} ꜱᴇᴄᴏɴᴅꜱ

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            except ApiIdInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    **ᴀᴘɪ ɪᴅ** ᴀɴᴅ **ᴀᴘɪ ʜᴀꜱʜ** ᴀʀᴇ ɪɴᴠᴀʟɪᴅ.

    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            except PhoneNumberInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.

    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return



            
            try:
                HYPE_OTP = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(
                chat.id,
                OTP,
                timeout=300)
            except TimeoutError:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ.

    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return



            
            if await exit_work(hn, HYPE_OTP.text):
                return



            
            HYPE_otp_CODE = HYPE_OTP.text
            try:
                await morphed.sign_in(
                phone,
                code.phone_code_hash,
                phone_code=' '.join(str(HYPE_otp_CODE)))

            except PhoneCodeInvalid:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    ɪɴᴠᴀʟɪᴅ ᴄᴏᴅᴇ.


    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            except PhoneCodeExpired:
                await hn.reply_photo(
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    ᴄᴏᴅᴇ ɪꜱ **𝐄𝐗𝐏𝐈𝐑𝐄𝐃** ᴏʀ ʏᴏᴜ ꜰᴏʀɢᴏᴛ ᴛᴏ **𝐏𝐔𝐓 𝐏𝐑𝐎𝐏𝐄𝐑 𝐒𝐏𝐀𝐂𝐄𝐒**

    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            except SessionPasswordNeeded:
                try:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ **𝐓𝐰𝐨-𝐒𝐭𝐞𝐩 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧.**
    ᴘʟᴇᴀꜱᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀꜱꜱᴡᴏʀᴅ.

    ᴘʀᴇꜱꜱ /exit ᴛᴏ ᴄᴀɴᴄᴇʟ ᴘʀᴏɢʀᴇꜱꜱ.

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                    HYPE_PASSCODE = await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.ask(chat.id,f"**÷••>**",timeout=300)


                except TimeoutError:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    `ᴛɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏꜰ 5 ᴍɪɴ`

    ᴘʀᴇꜱꜱ /start ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴇɴᴛɪʀᴇ ᴘʀᴏᴄᴇꜱꜱ ᴀɢᴀɪɴ.`

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                    return


            
                if await exit_work(hn,HYPE_PASSCODE.text):
                    return



            
                HYPE_GOT_CODE = HYPE_PASSCODE.text
                try:
                    await morphed.check_password(HYPE_GOT_CODE)
                except Exception as e:
                    await hn.reply_photo(
                    photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                    caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    **ᴇʀʀᴏʀ:** `{str(e)}`

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                    return

            
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                text=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    **ᴇʀʀᴏʀ:** `{str(e)}`

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return


            try:
                SESSION_HYPED = await morphed.export_session_string()
                await morphed.send_photo(
                "me",
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ 𝘽𝙖𝙨𝙞𝙘 𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙎𝙚𝙨𝙨𝙞𝙤𝙣 𝙉𝙖𝙢𝙚:

    ```{SESSION_HYPED}```

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))


            
                await morphed.disconnect()
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    `𝘚𝘵𝘳𝘪𝘯𝘨 𝘨𝘦𝘯𝘦𝘳𝘢𝘵𝘪𝘰𝘯 𝘸𝘢𝘴 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘤𝘰𝘮𝘱𝘭𝘦𝘵𝘦𝘥`
    ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))


            
            except Exception as e:
                await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
                chat.id,
                photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
                caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    **ᴇʀʀᴏʀ:** `{str(e)}`

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
                return



            
        except Exception as e:
            await 𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.send_photo(
            chat.id,
            photo="https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg",
            caption=f"""
    **—••÷🧊 SΣSSIӨП_MΛKΣЯ 🧊÷••—** `by` 🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀


    🟡 ＣＯＤＥ－ＹＥＬＬＯＷ 🟡
    **ᴇʀʀᴏʀ:** `{str(e)}`

    —••÷[🕊NӨЯDΣD🕊]÷••—
    """,
        reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton(
        text="🏷Group",
        url="https://t.me/HYPEVOIDS"),],[
        InlineKeyboardButton(
        text="—••÷[🕊NӨЯDΣD🕊]÷••—",
        url="https://t.me/nordedbot"),],[
        InlineKeyboardButton(
        text="💰Channel",
        url="https://t.me/HYPEVOIDLAB"),],[
        InlineKeyboardButton(
        text="⚜️Dev+Git",
        url="https://t.me/HYPEVOIDBOT")
        ]]))
            return
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
""""""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— USERBOT STARTS....
GONNA BE LONG LOL
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Admins
& filters.command(
"plug",
NordFix))
async def plug(
client,
ΣOЯ: NordLink):
    try:
        mntn = ΣOЯ.from_user.mention
        ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
        if not ռօʀɖʀɨռɢ:
            ռօʀɖɦօք.ռօʀɖʀɨռɢ = GroupCallFactory(client).get_file_group_call()
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.add_handler(
            network_status_changed_handler,
            GroupCallFileAction.NETWORK_STATUS_CHANGED)
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.add_handler(
            playout_ended_handler,
            GroupCallFileAction.PLAYOUT_ENDED)
            await ռօʀɖɦօք.ռօʀɖʀɨռɢ.start(ΣOЯ.chat.id)
            await ΣOЯ.delete()
        if ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected:
            await ΣOЯ.delete()
            xy = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n `𝗡𝗼𝗿𝗱𝗲𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁!`")
            await asyncio.sleep(CLEANER)
            await xy.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        ռօʀɖɦօք.chat_id = MAX_CHANNEL_ID - context.full_chat.id
        kai = await NorDAnimatE(f"{ӼɛӼօ}𝗡𝗼𝗿𝗱𝗲𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁!")
        await asyncio.sleep(
        CLEANER
        )
        await kai.delete()
    else:
        kai = await NorDAnimatE(f"{ӼɛӼօ}𝐍𝐨𝐫𝐝𝐞𝐝 𝐮𝐬𝐞𝐫𝐛𝐨𝐭 𝐡𝐚𝐬 𝐥𝐞𝐟𝐭 𝐚𝐧𝐝 𝐮𝐧𝐩𝐥𝐮𝐠𝐠𝐞𝐝 𝐦𝐮𝐬𝐢𝐜 𝐩𝐥𝐚𝐲𝐞𝐫 𝐢𝐧 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭!")
        ռօʀɖɦօք.chat_id = None
        await asyncio.sleep(
        CLEANER
        )
        await kai.delete()
async def playout_ended_handler(_, __):
    await NorDIgnoreNow()
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def restart(text):
    HEROKU = heroku3.from_key(HEROKU_API_KEY)
    app = HEROKU.apps()[HEROKU_APP_NAME]
    app.restart()
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    chat_id = ռօʀɖɦօք.chat_id
    message = await client.send_message(chat_id,text)
    return message
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"unplug",
NordFix))
async def unplug(
client,
ΣOЯ: NordLink):
    try:
        await ΣOЯ.delete()
        try:
            HEROKU = heroku3.from_key(HEROKU_API_KEY)
            app = HEROKU.apps()[HEROKU_APP_NAME]
            app.restart()
        except Exception as DΣD:
            await ΣOЯ.reply_text(f"{ӼɛӼօ}Please use /restart before replugging as auto reboot failed")
            return

        mntn = ΣOЯ.from_user.mention
        ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
        ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ.clear()
        ռօʀɖʀɨռɢ.input_filename = ""
        await ռօʀɖʀɨռɢ.stop()
        await ΣOЯ.delete()


        try:
            if HEROKU_API_KEY is not None and HEROKU_APP_NAME is not None and HEROKU == "HEROKU":
                wait = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption="⚠️❗️ 𝐏𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭 𝐭𝐢𝐥𝐥 𝐜𝐨𝐝𝐞 𝐜𝐥𝐞𝐚𝐧𝐬 𝐚𝐧𝐝 𝐫𝐞𝐬𝐭𝐚𝐫𝐭𝐬 𝐢𝐭𝐬𝐞𝐥𝐟.\n𝙏𝙖𝙠𝙚𝙨 𝙖𝙧𝙤𝙪𝙣𝙙 30𝙨𝙚𝙘-1𝙢𝙞𝙣",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                # await restart(f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\nREBOOTED")
                await wait.delete()


            else:
                await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption="⚠️❗️ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗠𝗮𝗻𝘂𝗮𝗹𝗹𝘆 `/restart` 𝘁𝗵𝗲 𝗯𝗼𝘁 𝗮𝘀 𝗶𝘁 𝗶𝘀 𝗶𝗻 𝗡𝗢𝗡-𝗛𝗘𝗥𝗢𝗞𝗨 𝗺𝗼𝗱𝗲",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& filters.command("stream",NordFix))
async def stream(
client,
ΣOЯ: NordLink):
    try:
        mntn = ΣOЯ.from_user.mention
        ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
        ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
        try:
            if ΣOЯ.audio:
                if ΣOЯ.audio.duration > (
                    DURATION_AUTOPLAY_MIN * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60):
                    psychodelic = await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{str(DURATION_AUTOPLAY_MIN)}",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await psychodelic.delete()
                    return
                m_audio = ΣOЯ

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
        
            elif ΣOЯ.reply_to_message and ΣOЯ.reply_to_message.audio:
                m_audio = ΣOЯ.reply_to_message
                if m_audio.audio.duration > (
                    DURATION_PLAY_HOUR * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60 * 60):
                    psychodelic = await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{str(DURATION_PLAY_HOUR)}",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await psychodelic.delete()
                    return

                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            else:
                await ռօʀɖɦօք.send_playlist()
                await ΣOЯ.delete()
                return

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            if ռօʀɖքʟǟʏɛʀʟɨֆȶ and ռօʀɖքʟǟʏɛʀʟɨֆȶ[-1].audio.file_unique_id \
                    == m_audio.audio.file_unique_id:
                psychodelic = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n That Audio file was successfully already added",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                await asyncio.sleep(
                CLEANER
                )
                await psychodelic.delete()
                return

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            ռօʀɖքʟǟʏɛʀʟɨֆȶ.append(m_audio)
            if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
                m_status = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n`𝗣𝗹𝗲𝗮𝘀𝗲 𝘄𝗮𝗶𝘁 𝗳𝗼𝗿 —••÷[🕊NORDED🕊]÷••—𝘁𝗼 𝗹𝗶𝗻𝗸 𝘄𝗶𝘁𝗵 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝘀𝗲𝗿𝘃𝗲𝗿...`\n𝙂𝙧𝙚𝙖𝙩𝙚𝙧 𝙖𝙪𝙙𝙞𝙤 𝙨𝙞𝙯𝙚, 𝙢𝙤𝙧𝙚 𝙩𝙞𝙢𝙚 𝙩𝙤 𝙖𝙙𝙙 𝙩𝙤 𝙨𝙚𝙧𝙫𝙚𝙧",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                await ռօʀɖɖօառʟօǟɖɛʀ(ռօʀɖքʟǟʏɛʀʟɨֆȶ[0])
                ռօʀɖʀɨռɢ.input_filename = os.path.join(
                client.workdir,
                DEFAULT_DOWNLOAD_DIR,
                f"{ռօʀɖքʟǟʏɛʀʟɨֆȶ[0].audio.file_unique_id}.raw")
                await ռօʀɖɦօք.NorDClocK()
                await m_status.delete()
            await ռօʀɖɦօք.send_playlist()

            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            try:
                async for YΣ in client.search_messages(
                    ΣOЯ.chat.id,
                    filter="pinned",
                    limit=1):
                    if YΣ.audio:
                        await YΣ.unpin()
                await ΣOЯ.reply_to_message.pin(True)
                NORD_TITLE = "🎶🌟NORDED_SMΛЯƬ_MUSIC_PLΛYΣЯ"
                try:
                    chatID = ΣOЯ.chat.id
                    EditGroupCallTitle(call=chatID, title=NORD_TITLE)
                except Exception:
                    await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ}\n[ERROR]: FAILED TO EDIT VC TITLE, MAKE ME ADMIN."
                    )
                    pass
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            for track in ռօʀɖքʟǟʏɛʀʟɨֆȶ[:2]:
                await ռօʀɖɖօառʟօǟɖɛʀ(track)
            if not ΣOЯ.audio:
                await ΣOЯ.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"next",
NordFix))
async def next(
client,
ΣOЯ: NordLink):
    try:
        mntn = ΣOЯ.from_user.mention
        try:
            await ΣOЯ.delete()
            ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
            if len(ΣOЯ.command) == 1:
                await NorDIgnoreNow()
            else:
                try:
                    items = list(dict.fromkeys(ΣOЯ.command[1:]))
                    items = [int(x) for x in items if x.isdigit()]
                    items.sort(reverse=True)
                    text = []
                    for i in items:
                        if 2 <= i <= (len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) - 1):
                            audio = f"[{ռօʀɖքʟǟʏɛʀʟɨֆȶ[i].audio.title}]({ռօʀɖքʟǟʏɛʀʟɨֆȶ[i].link})"
                            ռօʀɖքʟǟʏɛʀʟɨֆȶ.pop(i)
                            text.append(f" {i}. **{audio}**")
                        else:
                            text.append(f" {i}")
                    psychodelic = await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption="\n".join(text),disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                    await ռօʀɖɦօք.send_playlist()

                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                    """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

                except (ValueError, TypeError):
                    psychodelic = await ΣOЯ.reply_photo(
                    photo=nordlinker,
                    caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️  𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙞𝙣𝙥𝙪𝙩",
                    reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                    text="🕊DΣV GЯӨЦP",
                    url=f"https://t.me/hypevoids",),],[
                    InlineKeyboardButton(
                    text="🤖 ΉYPΣ VӨID BӨT",
                    url=f"https://t.me/hypevoidbot")
                    ]]))
                    await asyncio.sleep(
                CLEANER
                )
                    await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& filters.command(
"nord",
NordFix))
async def help(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            if cb_data is False:
                await ΣOЯ.reply_text(f"Add @{BOT_USERNAME} to group")
            else:
                await ΣOЯ.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Admins
& filters.command(
"norded",
NordFix))
async def norded(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            if ռօʀɖʀɨռɢ and ռօʀɖʀɨռɢ.is_connected:
                chat_id = int("-100" + str(ռօʀɖʀɨռɢ.full_chat.id))
                chat = await client.get_chat(chat_id)
                psychodelic = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"**NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝘀 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗶𝗻 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**:\n- **__{chat.title}__**",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                await asyncio.sleep(
                CLEANER
                )
                await psychodelic.delete()

                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
                """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            else:
                join = await ΣOЯ.reply_photo(
                photo=nordlinker,
                caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⚠️❗️ **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗱𝗶𝗱 𝗻𝗼𝘁 𝗷𝗼𝗶𝗻 𝗮𝗻𝘆 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝘆𝗲𝘁",
                reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                text="🕊DΣV GЯӨЦP",
                url=f"https://t.me/hypevoids",),],[
                InlineKeyboardButton(
                text="🤖 ΉYPΣ VӨID BӨT",
                url=f"https://t.me/hypevoidbot")
                ]]))
                await ΣOЯ.delete()
                await asyncio.sleep(
                CLEANER
                )
                await join.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"end",
NordFix))
async def end(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            ռօʀɖʀɨռɢ.stop_playout()
            psychodelic = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⏹❗️ **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗽𝗹𝗮𝘆𝗶𝗻𝗴**",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            await ռօʀɖɦօք.NorDClocK(reset=True)

            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""
            """➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

            try:
                async for YΣ in client.search_messages(ΣOЯ.chat.id,filter="pinned",limit=1):
                    if YΣ.audio:
                        await YΣ.unpin()
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ.clear()
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"replay",
NordFix))
async def restart(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
            if not ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ:
                return
            ռօʀɖʀɨռɢ.restart_playout()
            await ռօʀɖɦօք.NorDClocK()
            psychodelic = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n⏹❗️ **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗶𝘀 𝗻𝗼𝘄 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝗼𝗻𝗴 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗯𝗲𝗴𝗶𝗻𝗻𝗶𝗻𝗴...**",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"pause",
NordFix))
async def pause(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.pause_playout()
            await ռօʀɖɦօք.NorDClocK(reset=True)
            psychodelic = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗽𝗮𝘂𝘀𝗲𝗱 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            ռօʀɖɦօք.ռօʀɖʍֆɢʀ["pause"] = psychodelic
            try:
                await psychodelic.pin()
            except ChatAdminRequired:
                pass
            except FloodWait:
                pass
            await asyncio.sleep(8)
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"resume",
NordFix))
async def resume(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            ռօʀɖɦօք.ռօʀɖʀɨռɢ.resume_playout()
            psychodelic = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗿𝗲𝘀𝘂𝗺𝗲𝗱 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁**",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            if ռօʀɖɦօք.ռօʀɖʍֆɢʀ.get("pause") is not None:
                await ռօʀɖɦօք.ռօʀɖʍֆɢʀ["pause"].delete()
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
@𝙽𝙾𝚁𝙳𝙴𝙳.on_message(
filters.chat(
CHAT_ID)
& ~filters.edited
& Nord_Caller
& Nord_Admins
& filters.command(
"temp",
NordFix))
async def clean(
client,
ΣOЯ: NordLink):
    try:
        try:
            mntn = ΣOЯ.from_user.mention
            await ΣOЯ.delete()
            download_dir = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR)
            temp_nord: list[str] = os.listdir(
            download_dir)
            for track in ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ[:2]:
                track_fn = f"{track.audio.file_unique_id}.raw"
                if track_fn in temp_nord:
                    temp_nord.remove(track_fn)
            count = 0
            if temp_nord:
                for ʀǟաƈ in temp_nord:
                    if ʀǟաƈ.endswith(".raw"):
                        count += 1
                        os.remove(
                        os.path.join(
                        download_dir,
                        ʀǟաƈ))
            psychodelic = await ΣOЯ.reply_photo(
            photo=nordlinker,
            caption=f"{ӼɛӼօ} 👾 Hɛʏ 𝙽𝙾𝚁𝙳𝙴𝙳 ʊֆɛʀ  {mntn}\n **NORDED©️ 𝗺𝘂𝘀𝗶𝗰 𝗽𝗹𝗮𝘆𝗲𝗿 𝗰𝗹𝗲𝗮𝗻𝗲𝗱 {count} 𝘁𝗲𝗺𝗽/𝗿𝗮𝘄 𝗳𝗶𝗹𝗲𝘀",
            reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
            text="🕊DΣV GЯӨЦP",
            url=f"https://t.me/hypevoids",),],[
            InlineKeyboardButton(
            text="🤖 ΉYPΣ VӨID BӨT",
            url=f"https://t.me/hypevoidbot")
            ]]))
            await asyncio.sleep(
            CLEANER
            )
            await psychodelic.delete()
        except Exception as DΣD:
            zygote = await ΣOЯ.reply_photo(
            animation=norderror,
            caption=
        f"""{ӼɛӼօ}
    🕊 {mntn} 🕊 
    ⚠️**ᴛʜᴇʀᴇ ᴡᴀꜱ ᴀɴ ᴇʀʀᴏʀ ᴘʀᴏᴄᴇꜱꜱɪɴɢ ᴛʜᴇ ᴘʀᴇᴠɪᴏᴜꜱ ʀᴇQᴜᴇꜱᴛ.**
    **ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ʙᴇʟᴏᴡ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ**

    `__{DΣD}__`
    """
    )
            await asyncio.sleep(CLEANER)
            await zygote.delete()
    except Exception as DΣD:
        print(DΣD)
        pass
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
""""""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— NORD_PLAYER STARTS
—••÷[🕊NORDED🕊]÷••—
"""
class NORDPLAYER(object):
    def __init__(self):
        self.ռօʀɖʀɨռɢ = None
        self.client = None
        self.chat_id = None
        self.ռօʀɖƈʟօƈӄ = None
        self.ռօʀɖքʟǟʏɛʀʟɨֆȶ = []
        self.ռօʀɖʍֆɢʀ = {}
    async def send_playlist(self):
        ռօʀɖքʟǟʏɛʀʟɨֆȶ = self.ռօʀɖքʟǟʏɛʀʟɨֆȶ
        if not ռօʀɖքʟǟʏɛʀʟɨֆȶ:
            NeoN = f"{ӼɛӼօ}[🔥 𝗡𝗢𝗥𝗗 𝗠𝘂𝘀𝗶𝗰 𝗹𝗶𝘀𝘁 𝙞𝙨 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙚𝙢𝙥𝙩𝙮 𝙖𝙣𝙙 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙞𝙣𝙥𝙪𝙩](https://telegra.ph/file/0592f028e92ff2a8e73f0.jpg)"
        else:
            if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
                NeoN = f"[🕊NORDED by ΉYPΣ VӨID LΛB](https://t.me/hypevoidbot)🎧𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪"
            else:
                NeoN = f"[🕊NORDED by ΉYPΣ VӨID LΛB](https://t.me/hypevoidbot)🎧𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪"
            
            NeoN += "\n".join([
                f"""🕊`÷ 𝙽𝙾𝚁𝙳𝙴𝙳 MUSIC ÷`🕊
🍪**ᴛɪᴛʟᴇ**: **{i}.**[{x.audio.title}]({x.link}) |**{x.audio.duration}sec**
"""
                for i, x in enumerate(ռօʀɖքʟǟʏɛʀʟɨֆȶ)
                ])
        if ռօʀɖɦօք.ռօʀɖʍֆɢʀ.get("ռօʀɖքʟǟʏɛʀʟɨֆȶ") is not None:
            await ռօʀɖɦօք.ռօʀɖʍֆɢʀ["ռօʀɖքʟǟʏɛʀʟɨֆȶ"].delete()
        ռօʀɖɦօք.ռօʀɖʍֆɢʀ["ռօʀɖքʟǟʏɛʀʟɨֆȶ"] = await NorDAnimatE(NeoN)
    async def NorDClocK(self, reset=False):
        self.ռօʀɖƈʟօƈӄ = (None if reset else datetime.utcnow().replace(microsecond=0))       
ռօʀɖɦօք = NORDPLAYER()
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def NorDAnimatE(text):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    chat_id = ռօʀɖɦօք.chat_id   
    animation="https://telegra.ph/file/976f71e4175c2f626fe04.mp4"
    message = await client.send_animation(
    chat_id,
    animation,
    text
    )
    return message
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def NorDIgnoreNow():
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    ռօʀɖքʟǟʏɛʀʟɨֆȶ = ռօʀɖɦօք.ռօʀɖքʟǟʏɛʀʟɨֆȶ
    if not ռօʀɖքʟǟʏɛʀʟɨֆȶ:
        return
    if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
        await ռօʀɖɦօք.NorDClocK()
        return
    client = ռօʀɖʀɨռɢ.client
    download_dir = os.path.join(
    client.workdir,
    DEFAULT_DOWNLOAD_DIR)
    ռօʀɖʀɨռɢ.input_filename = os.path.join(
    download_dir,
    f"{ռօʀɖքʟǟʏɛʀʟɨֆȶ[1].audio.file_unique_id}.raw")
    await ռօʀɖɦօք.NorDClocK()
    old_track = ռօʀɖքʟǟʏɛʀʟɨֆȶ.pop(0)
    await ռօʀɖɦօք.send_playlist()
    os.remove(os.path.join(
    download_dir,
    f"{old_track.audio.file_unique_id}.raw"))
    if len(ռօʀɖքʟǟʏɛʀʟɨֆȶ) == 1:
        return
    await ռօʀɖɖօառʟօǟɖɛʀ(ռօʀɖքʟǟʏɛʀʟɨֆȶ[1])
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
async def ռօʀɖɖօառʟօǟɖɛʀ(ΣOЯ: NordLink):
    ռօʀɖʀɨռɢ = ռօʀɖɦօք.ռօʀɖʀɨռɢ
    client = ռօʀɖʀɨռɢ.client
    raw_file = os.path.join(
    client.workdir,
    DEFAULT_DOWNLOAD_DIR,
    f"{ΣOЯ.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        original_file = await ΣOЯ.download()
        ffmpeg.input(original_file).output(
            raw_file,
            format="s16le",
            acodec="pcm_s16le",
            ac=2,
            ar="48k",
            loglevel="error"
        ).overwrite_output().run()
        os.remove(original_file)
"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
""""""—••÷[🕊NORDED🕊]÷••—
* FROM HERE THE CODE FOR —••÷[🕊NORDED🕊]÷••— LOOGER USING LOGURU STARTS
—••÷[🕊NORDED🕊]÷••—
"""
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
         "CRITICAL",
        logging.ERROR:
         "ERROR",
        logging.WARNING:
         "WARNING",
        logging.INFO:
         "INFO",
        logging.DEBUG:
         "DEBUG"        }
    def _get_level(
        self,
        record):
        return self.LEVELS_MAP.get(
        record.levelno,
        record.levelno)
    def emit(self, record):
        logger_opt = logger.opt(
        depth=6,
        exception=record.exc_info,
        ansi=True,
        lazy=True)
        logger_opt.log(self._get_level(record),
        record.getMessage())
logging.basicConfig(handlers=[InterceptHandler()],
level=logging.INFO)
ɴᴏʀᴅᴘᴜᴛ = logging.getLogger(__name__)


LICE="""➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
GNU GENERAL PUBLIC LICENSE 
Version 3, 29 June 2007
Copyright (C) 2007 Free Software Foundation
Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
—••÷[🕊NORDED🕊]÷••—  
Telegram Music player userbot 
has been licensed under GNU General Public License
𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🎧🎧➕🎧🎧➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"""

# file = open("bootlock.py", "w") 
# file.write("from 𝙽𝙾𝚁𝙳𝙴𝙳 import *\n\n\nNORDED𝗕𝗢𝗧.start()\nidle()\nNORDED𝗕𝗢𝗧.stop()") 
    
# file = open("bootlocker.py", "w") 
# file.write("from 𝙽𝙾𝚁𝙳𝙴𝙳 import *\n\n\nNORDED.start()\nidle()\nNORDED.stop()") 

# import subprocess
# subprocess.run("python3 bootlock.py & python3 bootlocker.py", shell=True)



try: 
    if HEROKU == "HEROKU":
        pass
    else:
        os.system("clear")
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢")
    ɴᴏʀᴅᴘᴜᴛ.info(":              ONLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢")
    𝙽𝙾𝚁𝙳𝙴𝙳.start()
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢")
    ɴᴏʀᴅᴘᴜᴛ.info(":              ONLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🟢")
    𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.start()
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(f"\n\n\n\n{LICE}")
    ""
    ""
    idle()
    ""
    ""
    if HEROKU == "HEROKU":
        pass
    else:
        os.system("clear")
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴")
    ɴᴏʀᴅᴘᴜᴛ.info(":              OFFLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴")
    𝙽𝙾𝚁𝙳𝙴𝙳.stop()
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴")
    ɴᴏʀᴅᴘᴜᴛ.info(":              OFFLINE")
    ɴᴏʀᴅᴘᴜᴛ.info(":              𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃")
    ɴᴏʀᴅᴘᴜᴛ.info(":              🔴")
    𝙽𝙾𝚁𝙳𝙴𝙳_𝙱𝙾𝚃.stop()
    ""
    ""
    ɴᴏʀᴅᴘᴜᴛ.info(f"\n\n\n\n{LICE}")
    sys.exit()
except Exception as DΣD:
    ɴᴏʀᴅᴘᴜᴛ.info(DΣD)
    ɴᴏʀᴅᴘᴜᴛ.info("Overriding to exit system")
    sys.exit()


"""
|
|
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
                                                       GNU GENERAL PUBLIC LICENSE 
                                                         Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        —••÷[🕊NORDED🕊]÷••— 
                                                    Telegram Music player userbot 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇🖇
|
|
"""
