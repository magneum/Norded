import asyncio
from Ӽɛʀօռօɨɖ import *
from HEIST import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& misa_misa
& filters.command(
"resume",
prefixes=DYNO_COMMAND)) 
async def resume_playing(_, ryui: Message):
    pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
    await pwn.edit_text("ETR> [░░░       ]")
    await pwn.edit_text("ETR> [░░░░░░    ]")
    await pwn.edit_text("ETR> [░░░░░░░░░░]")  
    await pwn.delete()  
    hawk = await ryui.reply_text(f"""{XE}                  
[🦋]{ZV0}[🦋]                               
**▶️ʀᴇꜱᴜᴍᴇᴅ ᴘʟᴀʏɪɴɢ ᴍᴜꜱɪᴄ**""",quote=False)
    ʜᴀᴅᴇ.voice_chatting.resume_playout()
    if ʜᴀᴅᴇ.msg.get('pause') is not None:
        await ʜᴀᴅᴇ.msg['pause'].delete()
    await ryui.delete()
    await wait_before_rm((hawk, ryui), Kill_Time)

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()