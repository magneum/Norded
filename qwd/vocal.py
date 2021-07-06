import asyncio
from datetime import datetime
from pyrogram.types import Message
from pytgcalls import GroupCall
from ᴇᴘɪꜱᴛʟᴇ import *
from .death_charm import *
    
SWITCH_ON_TIME = 3
SWITCH_OFF_TIME = 4
@ʜᴀᴅᴇ.voice_chatting.on_network_status_changed
async def network_status_changed_handler(ip: GroupCall, is_connected: bool):
    if is_connected:
        ʜᴀᴅᴇ.chat_id = int("-100" + str(ip.full_chat.id))
        hawk = await ʜᴀᴅᴇ.send_text(
            f"一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一\n"
            "𝕆ℕ𝕃𝕀ℕ𝔼🟢.\n"
            )     
        await delete_switch_on((hawk,), SWITCH_ON_TIME)              
    else:
        hawk = await ʜᴀᴅᴇ.send_text(
            f"一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一\n"     
            "🔇𝕀𝔻𝕃𝔼_𝕄𝕆𝔻𝔼_𝔸ℂ𝕋𝕀𝕍𝔼🔇.\n"
            )       
        await delete_switch_off((hawk,), SWITCH_OFF_TIME)                       
        ʜᴀᴅᴇ.chat_id = None
    
async def delete_switch_on(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()

async def delete_switch_off(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
    
@ʜᴀᴅᴇ.voice_chatting.on_playout_ended
async def playout_ended_handler(_, __):
    await ʜᴀᴅᴇ.skip_current_playing()
