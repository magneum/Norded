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
        self.client = None
        self.xeronoid_msngr = {}
        self.xeronoid_begin = None
        self.xeronoid_voixe = None
        self.xeronoid_chatid = None 
        self.xeronoid_musical_xhat = []
              
                
        
    async def xeronoid_begin_clock(self, reset=False):
        self.xeronoid_begin = (None if reset else datetime.utcnow().replace(microsecond=0))
        
                
    async def xeronoid_show_playlist(self):
        xeronoid_musical_xhat = self.xeronoid_musical_xhat
        if not xeronoid_musical_xhat:
            pl = f"empty xeronoid_musical_xhat"
        else:
            if len(xeronoid_musical_xhat) == 1:
                pl = f" **Playlist**:\n"
            else:
                pl = f" **Playlist**:\n"
            pl += "\n".join([
                f"**{i}**. **[{x.audio.title}]({x.link})**"
                for i, x in enumerate(xeronoid_musical_xhat)])
        if xep.xeronoid_msngr.get('xeronoid_musical_xhat') is not None:
            await xep.xeronoid_msngr['xeronoid_musical_xhat'].delete()
        xep.xeronoid_msngr['xeronoid_musical_xhat'] = await xero_back_sender(pl)
        
        
xep = XeronoidSinger()






async def xero_back_sender(text):
    xeronoid_voixe = xep.xeronoid_voixe
    client = xeronoid_voixe.client
    xeronoid_chatid = xep.xeronoid_chatid
    message = await client.send_message(
    xeronoid_chatid,
    text,
    disable_web_page_preview=True,
    disable_notification=True)
    return message
