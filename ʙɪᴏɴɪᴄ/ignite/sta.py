from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from HEIST import *
from Ӽɛʀօռօɨɖ import *
from ᴄᴏɴᴄᴇᴘᴛ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


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
    caption=cap,
    reply_markup=JOIN_BUTTLOCK
    )    
    
cap = f"""
𝕆山ᑎER: {HON}

"""