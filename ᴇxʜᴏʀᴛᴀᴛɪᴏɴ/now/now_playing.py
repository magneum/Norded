from Ӽɛʀօռօɨɖ import *
from HEIST import *
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE import *


@Client.on_message(
demon_killer_sigki
& misa_misa
& filters.command(
"now",
prefixes=WHITE_COMMAND))   
async def show_current_playing_time(_, ryui: Message):
    start_time = ʜᴀᴅᴇ.start_time
    playlist = ʜᴀᴅᴇ.playlist
    if not start_time:
        pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
        await pwn.edit_text("ETR> [░░░       ]")
        await pwn.edit_text("ETR> [░░░░░░    ]")
        await pwn.edit_text("ETR> [░░░░░░░░░░]")  
        await pwn.delete()           
        hawk = await ryui.reply_photo(
            ZV0,
            caption="[🦋]**ɴᴏᴛʜɪɴɢ ɪꜱ ɪɴ ᴘʟᴀʏʟɪꜱᴛ ʏᴇᴛ!**[🦋]"
        )
        await wait_before_rm((hawk,), Kill_Time)                 
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if ʜᴀᴅᴇ.msg.get('now') is not None:
        await ʜᴀᴅᴇ.msg['now'].delete()
    ʜᴀᴅᴇ.msg['now'] = await playlist[0].reply_text(
        f"🌈 {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await ryui.delete()
    

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()