"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""
from ɖօօʍ_ʀօօʍ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *





class XeronoidSinger(object):
    def __init__(self):
        self.xemsg = {}
        self.client = None
        self.xeronoid_clock = None
        self.xeronoid_voixe = None
        self.xeronoid_music_list = []
        self.xeronoid_chat_verify = None       
        
        
        
    async def update_start_time(self, reset=False):
        self.xeronoid_clock = (None if reset else datetime.utcnow().replace(microsecond=0))
        
        
        
    async def send_playlist(self):
        xeronoid_music_list = self.xeronoid_music_list
        if not xeronoid_music_list:
            pl = f"{emoji.NO_ENTRY} empty xeronoid_music_list"
        else:
            if len(xeronoid_music_list) == 1:
                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"
            else:
                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}]({x.link})**"
                for i, x in enumerate(xeronoid_music_list)])
        if xep.xemsg.get('xeronoid_music_list') is not None:
            await xep.xemsg['xeronoid_music_list'].delete()
        xep.xemsg['xeronoid_music_list'] = await xero_back_sender(pl)
        
        
xep = XeronoidSinger()






async def xero_back_sender(text):
    xeronoid_voixe = xep.xeronoid_voixe
    client = xeronoid_voixe.client
    xeronoid_chat_verify = xep.xeronoid_chat_verify
    message = await client.send_message(
    xeronoid_chat_verify,
    text,
    disable_web_page_preview=True,
    disable_notification=True)
    return message
