""" 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|----------------------------------------------------------------------------------------|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|----------------------------------------------------------------------------------------|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""

from ɖօօʍ_ʀօօʍ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'



'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
class XeronoidPlayer(xeroobj):
    def __init__(self):
        self.client = None
        self.group_call = None
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.xeronoid_msngr = {}
       
    async def xeronoid_begin_clock(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)) 
           
    async def xeronoid_show_playlist(self, xemsg: xeromsg):
        playlist = self.playlist
        if not playlist:
            xero_playlist = await xemsg.reply_animation(
            animation=xerolink,
            caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙢𝙪𝙨𝙞𝙘 𝙡𝙞𝙨𝙩 𝙞𝙨 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙚𝙢𝙥𝙩𝙮 𝙖𝙣𝙙 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙞𝙣𝙥𝙪𝙩
            """
            )
        else:
            if len(playlist) == 1:
                xero_playlist = f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                """
                # xero_playlist = await xemsg.reply_animation(
                # animation=xerolink,
                # caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n
                # 『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                # (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                # """
                # )
            else:
                xero_playlist = f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n
                『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                """
                # xero_playlist = await xemsg.reply_animation(
                # animation=xerolink,
                # caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n
                # 『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                # (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                # """
                # )
            xero_playlist += "\n".join([
                f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n**{i}**. **[{x.audio.title}]({x.link})"""
                for i, x in enumerate(playlist)
            ])
        if xeroclip.xeronoid_msngr.get('playlist') is not None:
            await xeroclip.xeronoid_msngr['playlist'].delete()
        xeroclip.xeronoid_msngr['playlist'] = await xeronoid_msg_sender(xero_playlist)    


xeroclip = XeronoidPlayer()


async def xeronoid_msg_sender(text):
    group_call = xeroclip.group_call
    client = group_call.client
    chat_id = xeroclip.chat_id
    message = await client.send_message(
    chat_id,
    text,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return message
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'

async def xeronoid_msg_sender(text):
    group_call = xeroclip.group_call
    client = group_call.client
    chat_id = xeroclip.chat_id
    xero_send_msgnr = await client.send_message(
    chat_id,
    text,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return xero_send_msgnr

async def xeronoid_bot_msg_sender(text):
    group_call = xeroclip.group_call
    client = group_call.client
    chat_id = LOGGER_ID
    xero_send_msgnr = await client.send_message(
    chat_id,
    text,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return xero_send_msgnr


async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        xeroclip.chat_id = macid - context.full_chat.id
        await xeronoid_msg_sender(
        f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙥𝙡𝙪𝙜𝙜𝙚𝙙 𝙞𝙣 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥 
        `{CHAT_ID}`'s 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩
        """)
        await xeronoid_bot_msg_sender(
        f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙥𝙡𝙪𝙜𝙜𝙚𝙙"
        )
    else:
        await xeronoid_msg_sender(
        f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙪𝙣𝙥𝙡𝙪𝙜𝙜𝙚𝙙 𝙛𝙧𝙤𝙢 𝙩𝙝𝙚 𝙜𝙧𝙤𝙪𝙥 
        `{CHAT_ID}`'s 𝙫𝙤𝙞𝙘𝙚 𝙘𝙝𝙖𝙩
        """)
        await xeronoid_bot_msg_sender(
        f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙪𝙣𝙥𝙡𝙪𝙜𝙜𝙚𝙙"
				)
        xeroclip.chat_id = None


async def xeronoid_music_over_handler(_, __):
    await xeronoid_show_playlist()


async def xeronoid_skip_music_handler():
    group_call = xeroclip.group_call
    playlist = xeroclip.playlist
    if not playlist:
        return
    if len(playlist) == 1:
        await xeroclip.xeronoid_begin_clock()
        return
    client = group_call.client
    download_dir = os.path.join(client.workdir, xeronoid_dl_dir)
    group_call.input_filename = os.path.join(
        download_dir,
        f"{playlist[1].audio.file_unique_id}.raw"
        )
    await xeroclip.xeronoid_begin_clock()
    old_track = playlist.pop(0)
    print(f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	Ӽɛʀօռօɨɖ ռօա քʟǟʏɨռɢ: {playlist[0].audio.title}")
    await xeroclip.xeronoid_show_playlist()
    os.remove(os.path.join(
        download_dir,
        f"{old_track.audio.file_unique_id}.raw")
        )
    if len(playlist) == 1:
        return
    await xeronoid_music_dl_handler(playlist[1])
    
    
    
async def xeronoid_music_dl_handler(xemsg: xeromsg):
    group_call = xeroclip.group_call
    client = group_call.client
    raw_file = os.path.join(
    client.workdir,
    xeronoid_dl_dir,
    f"{xemsg.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        xeronoid_raw_media = await xemsg.download()
        ffmpeg.input(xeronoid_raw_media).output(
        raw_file,
        format='s16le',acodec='pcm_s16le',ac=2,ar='48k',loglevel='error'
        ).overwrite_output().run()
        os.remove(xeronoid_raw_media)