from HEIST import *
from Ӽɛʀօռօɨɖ import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@Ӽɛռ.on_message(
demon_killer_sigki
& senzo_kryo_ni
& filters.command(
"group",
prefixes=DYNO_COMMAND))                     
async def list_voice_chat(client, ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    if voice_chatting.is_connected:
        pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
        await pwn.edit_text("ETR> [░░░       ]")
        await pwn.edit_text("ETR> [░░░░░░    ]")
        await pwn.edit_text("ETR> [░░░░░░░░░░]")  
        await pwn.delete()         
        chat_id = int("-100" + str(voice_chatting.full_chat.id))
        await pwn.delete()
        chat = await client.get_chat(chat_id)
        hawk = await ryui.reply_photo(
            "https://telegra.ph/file/964d42c83b5b2f5c50f43.jpg",   
            caption=f"""
            {XE}
            ᴄᴜʀʀᴇɴᴛʟʏ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏꜰ: \n**{chat.title}**
            """
            )   
    else:
        hawk = await ryui.reply_text("⏳ᴡᴀɪᴛɪɴɢ ᴛᴏ ʙᴇ ᴘʟᴜɢɢᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ⌛️")
    await wait_before_rm((hawk, ryui), Kill_Time)
    
async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
