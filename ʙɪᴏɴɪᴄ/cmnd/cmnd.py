from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from HEIST import *
from Ӽɛʀօռօɨɖ import *
from ᴄᴏɴᴄᴇᴘᴛ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *

@ɦɖɛ.on_message(
filters.command("cmd",prefixes="/")) 
async def pong(_, xd: Message):
    await xd.reply_chat_action("playing")
    await xd.reply_photo(
    ZV0,
    caption="type .cmd to check all commands",
    )    