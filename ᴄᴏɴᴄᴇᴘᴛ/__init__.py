from logging import root
from pyrogram import Client as POD, filters , idle
from pyrogram.types import Message
from time import time
from datetime import datetime
from Importing import *

ɦɖɛ = POD(
    session_name="Ӽɛʀօʋօɨɖ",
    bot_token=BN,
    api_id=AD,
    api_hash=AH,
    plugins=ʙɪɪᴄ,
)
from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)