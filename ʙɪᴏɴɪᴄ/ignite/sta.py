from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from HEIST import *
from Ӽɛʀօռօɨɖ import *
from ᴄᴏɴᴄᴇᴘᴛ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *

CAPP = f"""
—(••÷[🔆 Ӽɛʀօռօɨɖ 💠]÷••—
🎧 𝘗𝘭𝘢𝘺 𝘢𝘯𝘺 𝘮𝘶𝘴𝘪𝘤 𝘪𝘯 𝘺𝘰𝘶𝘳 𝘨𝘳𝘰𝘶𝘱 𝘷𝘤.𝘠𝘰𝘶 𝘸𝘪𝘭𝘭 𝘩𝘢𝘷𝘦 𝘵𝘰 𝘣𝘦 𝘰𝘸𝘯𝘦𝘳 𝘵𝘰 𝘶𝘴𝘦 𝘵𝘩𝘪𝘴 𝘣𝘰𝘵 𝘰𝘳 𝘨𝘦𝘵 𝘦𝘳𝘳𝘰𝘳𝘴.

🔹 ɪ ᴀᴍ xᴇʀᴏɴᴏɪᴅ ʙᴏᴛ'ꜱ ᴄᴏᴍᴍᴀɴᴅ ʜᴇʟᴘᴇʀ ʙᴏᴛ.ɪ ʜᴀᴠᴇ ʙᴇᴇɴ ᴄᴏᴅᴇᴅ ᴛᴏ ᴡᴏʀᴋ ᴡɪᴛʜ xᴇʀᴏɴᴏɪᴅ ᴜꜱᴇʀʙᴏᴛꜱ.ᴠɪꜱɪᴛ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ

𝘾𝙪𝙧𝙧𝙚𝙣𝙩 𝙓𝙚𝙧𝙤𝙣𝙤𝙞𝙙'𝙨 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙤𝙬𝙣𝙚𝙧 𝙞𝙨:
🎶 {HON}


💻**Dҽʋ Mҽɳƚισɳ:**
 @hypevoidsoul
 @hypevoidbot
"""

JOIN_BUTTLOCK = InlineKeyboardMarkup(
[[
    InlineKeyboardButton(
            " Ӽɛʀօռօɨɖ 』🎧",
                url="https://t.me/hypevoidlab/107"
)],[
    InlineKeyboardButton(
            "🍺『 ɢʀᴏᴜᴘ 』",          
                url="https://t.me/HYPEVOIDS"
)],[
    InlineKeyboardButton(
            "🔥『 ᴄʜᴀɴɴᴇʟ 』",          
            url="https://t.me/HYPEVOIDLAB"
)]])

@ɦɖɛ.on_message(
filters.command("start",prefixes="/")) 
async def pong(_, xd: Message):
    await xd.reply_chat_action("playing")
    await xd.reply_photo(
    ZV0,
    caption=CAPP,
    reply_markup=JOIN_BUTTLOCK
    )    