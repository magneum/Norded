from HEIST import *
from Ӽɛʀօռօɨɖ import *
from ᴄᴏɴᴄᴇᴘᴛ import *


@ɦɖɛ.on_message(
filters.command("server",prefixes="/")) 
async def pong(_, xd: Message):
    start = datetime.now()
    await asyncio.sleep(1)
    end = datetime.now()
    delta_energy1 = (end - start).microseconds / 100000
    drip = await xd.reply_text("💋")   
    await drip.edit("🌟")
    await asyncio.sleep(1)
    await drip.edit("⭐️")  
    await asyncio.sleep(1)
    await drip.delete()
    zeto = await xd.reply_photo(
    ZV0,
    caption=f"""
    一═デ🦋 **Ӽɛʀօռօɨɖ** 🦋デ═一

|   𝚂𝚎𝚛𝚟𝚎𝚛 𝚛𝚎𝚜𝚙𝚘𝚗𝚜𝚎 𝚝𝚒𝚖𝚎 𝚒𝚜   |
📡 **{delta_energy1}** `micro Seconds` 
        ⭛ H¥þêVðïÐ Ìñ¢l. ⭜

{VED}""")
    await delete_server((zeto,xd),12)
    return 

async def delete_server(messages: tuple,delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()