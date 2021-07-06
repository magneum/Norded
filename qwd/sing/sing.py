import os
import asyncio
from Ӽɛʀօռօɨɖ import *
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as fmedaddyy
from pyrogram.types import Message
from ᴠᴏᴋᴀʟɪᴢᴇ import *
from ᴇᴘɪꜱᴛʟᴇ import *
from Importing import *


@Ӽɛռ.on_message(
filters.group
& ~filters.edited
& misa_misa
& (filters.command(
"sing",
prefixes=WHITE_COMMAND) | filters.audio | filters.video))
async def play_track(client, ryui: Message):
    voice_chatting = ʜᴀᴅᴇ.voice_chatting
    playlist = ʜᴀᴅᴇ.playlist
    if ryui.audio:
        if ryui.audio.duration > (Auto_Add2Play_TimeM * 60):
            pwn = await ryui.reply_text("Syncing with @hypevoids 's servers", True)
            await pwn.edit_text("ETR> [░░░       ]")
            await pwn.edit_text("ETR> [░░░░░░    ]")
            await pwn.edit_text("ETR> [░░░░░░░░░░]")  
            await pwn.delete()                     
            hawk = await ryui.reply_text(
                f"ᴀᴜᴅɪᴏ ᴡʜɪᴄʜ ᴅᴜʀᴀᴛɪᴏɴ ʟᴏɴɢᴇʀ ᴛʜᴀɴ "
                f"{str(Auto_Add2Play_TimeM)} ᴍɪɴ ᴡᴏɴ'ᴛ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ "
                "**ʜᴀꜱ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ ᴛᴏ ᴘʟᴀʏʟɪꜱᴛ**\n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
        media_aud = ryui
    elif ryui.reply_to_message and ryui.reply_to_message.audio:
        media_aud = ryui.reply_to_message
        if media_aud.audio.duration > (Kill_Hour * 60 * 60):
            pwn = await ryui.reply_text("Syncing with @tronxli", True)
            await pwn.edit_text("and it's servers...")
            await pwn.edit_text("ETR: > sec[░░░░░░              ]")
            await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░        ]")
            await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░░░░░░░░░]")  
            await pwn.delete()           
            hawk = await ryui.reply_text(
                f"ᴀᴜᴅɪᴏ ᴡʜɪᴄʜ ᴅᴜʀᴀᴛɪᴏɴ ʟᴏɴɢᴇʀ ᴛʜᴀɴ "
                f"{str(Kill_Hour)} ʜᴏᴜʀꜱ ᴡᴏɴ'ᴛ ʙᴇ ᴀᴅᴅᴇᴅ ᴛᴏ ᴘʟᴀʏʟɪꜱᴛ\n"
            )
            await wait_before_rm((hawk,), Kill_Time)
            return
    else:
        await ʜᴀᴅᴇ.send_playlist()
        await ryui.delete()
        return
    if playlist and playlist[-1].audio.file_unique_id \
            == media_aud.audio.file_unique_id:
        hawk = await ryui.reply_text(f"""{XE}
**ᴛʜᴀᴛ ꜰɪʟᴇ ʜᴀꜱ ᴀʟʀᴇᴀᴅʏ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ**
""")
        await wait_before_rm((hawk, ryui), Kill_Time)
        return
    playlist.append(media_aud)
    if len(playlist) == 1:
        pwn = await ryui.reply_text("Syncing with @tronxli", True)
        await pwn.edit_text("and it's servers...")
        await pwn.edit_text("ETR: > sec[░░░░░░              ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░        ]")
        await pwn.edit_text("ETR: > sec[░░░░░░░░░░░░░░░░░░░░]")
        await pwn.delete() 
        m_status = await ryui.reply_text(f"""{XE}
[🦋]{ZV0}[🦋]                          
**ᴀɴᴀʟʏᴢɪɴɢ ᴀᴜᴅɪᴏ ʙɪᴛʀᴀᴛᴇ & ꜱᴇɴᴅɪɴɢ ᴛᴏ ꜱᴇʀᴠᴇʀ**
        """)
        await ʜᴀᴅᴇ.download_audio(playlist[0])
        voice_chatting.input_filename = os.path.join(
            client.workdir,
            fmedaddyy,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await ʜᴀᴅᴇ.update_start_time()
        await m_status.delete()
        print(f"- PLAYING: {playlist[0].audio.title}")
    await ʜᴀᴅᴇ.send_playlist()
    for track in playlist[:2]:
        await ʜᴀᴅᴇ.download_audio(track)
    if not ryui.audio:
        await ryui.delete()

async def wait_before_rm(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()