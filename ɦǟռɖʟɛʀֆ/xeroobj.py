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

from ʟɨɮʀǟʀʏ_ʀօօʍ import *
from ɖօօʍ_ʀօօʍ import *
from .class_room import *

async def xeronoid_msg_sender(text):
    xeronoid_musical_xhat = xeroclip.xeronoid_musical_xhat
    client = xeronoid_musical_xhat.client
    xeronoid_chatid = xeroclip.xeronoid_chatid
    message = await client.send_message(
    xeronoid_chatid,
    text,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return message


async def xeronoid_begin_clock(self, reset=False):
        self.xeronoid_begin = (
            None if reset
            else datetime.utcnow().replace(microsecond=0))
        
        
           
async def xeronoid_show_playlist(self, xemsg: xeromsg):
        xeronoid_music_list = self.xeronoid_music_list
        if not xeronoid_music_list:
            xero_playlist = await xemsg.reply_animation(
            animation=xerolink,
            caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙢𝙪𝙨𝙞𝙘 𝙡𝙞𝙨𝙩 𝙞𝙨 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙚𝙢𝙥𝙩𝙮 𝙖𝙣𝙙 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙞𝙣𝙥𝙪𝙩
            """
            )
        else:
            if len(xeronoid_music_list) == 1:
                xero_playlist = await xemsg.reply_animation(
                animation=xerolink,
                caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n
                『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                """
                )
            else:
                xero_playlist = await xemsg.reply_animation(
                animation=xerolink,
                caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n
                『  𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗡𝗼𝘄-𝗣𝗹𝗮𝘆𝗶𝗻𝗴 𝗟𝗶𝘀𝘁  』[❄️ ʜʏᴘᴇᴠᴏɪᴅ ɪɴᴄʟ.](https://telegra.ph/file/136c238b287f9c7d5174c.jpg) 
                (┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n
                """
                )
            xero_playlist += "\n".join([
                f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n**{i}**. **[{x.audio.title}]({x.link})"""
                for i, x in enumerate(xeronoid_music_list)
            ])
        if xeroclip.xeronoid_msngr.get('xeronoid_music_list') is not None:
            await xeroclip.xeronoid_msngr['xeronoid_music_list'].delete()
        xeroclip.xeronoid_msngr['xeronoid_music_list'] = await xeronoid_msg_sender(xero_playlist)
        

xeroclip = xeronoid_player()