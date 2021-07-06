import asyncio
from Ӽɛʀօռօɨɖ import *
from pyrogram.types import Message
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from Importing import *


@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
& filters.command(
"replay",
prefixes=DYNO_COMMAND)) 
async def restart_playing(_, ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    if not ʜᴀᴅᴇ.playlist:
        return
    pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
    await pwn.edit_text("ETR> [░░░       ]")
    await pwn.edit_text("ETR> [░░░░░░    ]")
    await pwn.edit_text("ETR> [░░░░░░░░░░]")  
    await pwn.delete()
    await ryui.reply_text(f"""{XE}
[🦋]{ZV0}[🦋]                          
🔁ᴘʟᴀʏɪɴɢ ꜰʀᴏᴍ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ
""")
    voice_chatting.restart_playout()
    await ʜᴀᴅᴇ.update_start_time()           

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
