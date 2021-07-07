from Ӽɛʀօռօɨɖ import *
from HEIST import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& filters.command(
"on",
prefixes=DYNO_COMMAND)) 
async def join_voice_chatting(client, ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    voice_chatting.client = client
    if voice_chatting.is_connected:
        pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
        await pwn.edit_text("ETR> [░░░       ]")
        await pwn.edit_text("ETR> [░░░░░░    ]")
        await pwn.edit_text("ETR> [░░░░░░░░░░]")  
        await pwn.delete()        
        await ryui.reply_text(f"""{XE}
            [🦋]{ZV0}[🦋]"
            
 "**ᴜꜱᴇʀʙᴏᴛ ʜᴀꜱ ᴀʟʀᴇᴀᴅʏ ᴊᴏɪɴᴇᴅ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɪɴ**"""
            )   
        return        
    await voice_chatting.start(ryui.chat.id)    
    await ryui.delete()
    
async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
