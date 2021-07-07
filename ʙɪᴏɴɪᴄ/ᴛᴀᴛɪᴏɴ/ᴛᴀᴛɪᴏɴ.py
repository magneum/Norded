from ᴄᴏɴᴄᴇᴘᴛ import *
from HEIST import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@ɦɖɛ.on_message(
filters.command("cmd",prefixes=WHITE_COMMAND)) 
async def show_help(_, xd: Message): 
  pwn = await xd.reply_text(SYN,True)
  await pwn.edit_text(SNC3)
  await pwn.edit_text(SNC5)
  await pwn.edit_text(SNC6)
  hawk = await xd.reply_photo(
  ZV0,
  caption=FULL_PLAYING_HELP)
  await delete_command_blue((hawk,xd), FHD)
  await pwn.delete()
  return  

async def delete_command_blue(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()   