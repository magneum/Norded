from ᴀᴜɴᴇʀ import *
from pyrogram import filters
import heroku3
from pyrogram.types import Message
from ᴠᴏᴋᴀʟɪᴢᴇ.death_charm import *
DYNO_COMMAND = ɢʟɛǟʍ.DYNO_COMMAND
HEROKU_APP_NAME = ɢʟɛǟʍ.HEROKU_APP_NAME
HEROKU_API_KEY = ɢʟɛǟʍ.HEROKU_API_KEY
WHITE_COMMAND = ɢʟɛǟʍ.WHITE_COMMAND
DOPE_END = f"一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一\n\n**⏹Stopped Singing**"
Kill_Time = 6
Auto_Add2Play_TimeM = 10
HPN = ɢʟɛǟʍ.HEROKU_APP_NAME
HPI = ɢʟɛǟʍ.HEROKU_API_KEY
HON = ɢʟɛǟʍ.OWNER_USERNAME
Kill_Hour = 3
SYN = f"Syncing with @hypevoids's"
HPJN = "application/vnd.heroku+json; version=3.account-quotas"
GROUP_CALLS = {}
Heroku = heroku3.from_key(HPI)
FFMPEG_PROCESSES = {}
CMD_DEL = 30
VED = """
**Dҽʋ Mҽɳƚισɳ:**
    @hypevoidsoul"""
RYUKDEL = 10
XEof = '一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一\nOFFLINE   ⚰️🍁'
XEon = '一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一\nONLINE    🎷🍁'
RYUKONDEL = 5
UAA = "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
UAB = "AppleWebKit/537.36 (KHTML, like Gecko) "
UAC = "Chrome/80.0.3987.149 Mobile Safari/537.36"

ᴄᴇᴘᴛ = dict(root="ᴇxʜᴏʀᴛᴀᴛɪᴏɴ")
FHD = 60
ʙɪɪᴄ = dict(root="ʙɪᴏɴɪᴄ")
BN = ɢʟɛǟʍ.BOT_TOKEN

demon_killer_sigki = (
filters.group
& filters.text
& ~filters.edited
& ~filters.via_bot)
SNC1 = "     ♫     "
SNC3 = "  ❄️♫♫♫❄️   "
SNC5 = " ❄️♫*∆*♫❄️   "
SNC6 = "     ❄️   "
senzo_kryo_ni = filters.create(lambda _,__,ryui:
    (ryui.from_user and ryui.from_user.is_contact) or ryui.outgoing)
HEROKUDEL = 8
heroku_api = "https://api.heroku.com"
AD = API_ID = ɢʟɛǟʍ.API_ID
XE = "一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一"
ZV0 = "https://telegra.ph/file/136c238b287f9c7d5174c.jpg"
AH = API_HASH = ɢʟɛǟʍ.API_HASH
SN = ɢʟɛǟʍ.SN
async def misa_misa_filter(_,__,ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    if not voice_chatting.is_connected:
        return False
    chat_id = int("-100" + str(voice_chatting.full_chat.id))
    if ryui.chat.id == chat_id:
        return True
    return False
misa_misa = filters.create(misa_misa_filter)
