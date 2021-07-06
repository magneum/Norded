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
"skip",
prefixes=DYNO_COMMAND)) 
async def skip_track(_, ryui: Message):
    playlist = ʜᴀᴅᴇ.playlist
    if len(ryui.command) == 1:
        await ʜᴀᴅᴇ.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(ryui.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"💥 {i}. **{audio}**")
                else:
                    text.append(f"💢 {i}")
            hawk = await ryui.reply_text("\n".join(text))
            await ʜᴀᴅᴇ.send_playlist()
        except (ValueError, TypeError):
            pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
            await pwn.edit_text("ETR> [░░░       ]")
            await pwn.edit_text("ETR> [░░░░░░    ]")
            await pwn.edit_text("ETR> [░░░░░░░░░░]")  
            await pwn.delete()   
            hawk = await ryui.reply_text(f"""{XE}
[🦋]{ZV0}[🦋]
**ɪɴᴠᴀʟɪᴅ ɪɴᴘᴜᴛ.ᴘʟᴇᴀꜱᴇ ʀᴇᴄʜᴇᴄᴋ ꜰɪʟᴇ ᴛʏᴘᴇ.**""",    
                                disable_web_page_preview=True
                                )
        await wait_before_rm((hawk, ryui), Kill_Time)
    
async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()