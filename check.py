from logging import root
from pyrogram import Client as POD, filters , idle
from pyrogram.types import Message
from time import time
from datetime import datetime
import asyncio

BOT = POD(
    session_name="Ӽɛʀօʋօɨɖ",
    bot_token="1850694025:AAEoT5SIsoWZgmaxiCJzHPBMw9ecOOpe6NM",
    api_id=6372795,
    api_hash="4b7731b0a6d8e15bef82863887feb293",
    #plugins=ʙɪɪᴄ,
)
from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)


SNC1 = "     ♫     "
SNC3 = "  ❄️♫♫♫❄️   "
SNC5 = " ❄️♫*∆*♫❄️   "
SNC6 = "     ❄️   "

@BOT.on_message(
filters.command("test",prefixes="/")) 
async def test(_, xd: Message):
  pwn = await xd.reply_text(SNC1,True)
  await pwn.edit_text(SNC3)
  await pwn.edit_text(SNC5)
  await pwn.edit_text(SNC6)
  hawk = await xd.reply_photo(
  "https://telegra.ph/file/136c238b287f9c7d5174c.jpg",
  caption="| ✩❄️̩̩͙*˚⁺‧͙⁺˚*❄️̩̩͙✩❄️̩̩͙*˚⁺‧͙⁺❄️̩̩͙✩ |")
  await delete_command_blue((hawk,xd), 6)
  await pwn.delete()
  return  

async def delete_command_blue(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()  

BOT.start()
idle()
BOT.stop()