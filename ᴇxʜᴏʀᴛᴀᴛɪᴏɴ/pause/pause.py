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
"pause",
prefixes=DYNO_COMMAND)) 
async def pause_playing(_, ryui: Message):
    pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
    await pwn.edit_text("ETR> [░░░       ]")
    await pwn.edit_text("ETR> [░░░░░░    ]")
    await pwn.edit_text("ETR> [░░░░░░░░░░]")  
    await pwn.delete()
    ʜᴀᴅᴇ.voice_chatting.pause_playout()
    await ʜᴀᴅᴇ.update_start_time(reset=True)
    hawk = await ryui.reply_photo(
        ZV0,
        caption=f"""{XE}
**⏸ᴘᴀᴜꜱᴇᴅ ᴍᴜꜱɪᴄ**""")
    ʜᴀᴅᴇ.msg['pause'] = hawk
    await ryui.delete()
