from Ӽɛʀօռօɨɖ import *
from pyrogram.types import Message
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *

@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
& filters.command(
"endvc",
prefixes=DYNO_COMMAND)) 
async def stop_playing(_, ryui: Message):
    pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
    await pwn.edit_text("ETR> [░░░       ]")
    await pwn.edit_text("ETR> [░░░░░░    ]")
    await pwn.edit_text("ETR> [░░░░░░░░░░]")  
    await pwn.delete()
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    voice_chatting.stop_playout()
    hawk = await ryui.reply_photo(
        ZV0,
        caption=DOPE_END
    )
    await ʜᴀᴅᴇ.update_start_time(reset=True)
    ʜᴀᴅᴇ.playlist.clear()
    await wait_before_rm((hawk, ryui), Kill_Time)

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()