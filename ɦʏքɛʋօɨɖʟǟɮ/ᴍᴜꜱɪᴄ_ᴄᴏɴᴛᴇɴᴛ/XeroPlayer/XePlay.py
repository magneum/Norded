"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ʟɪʙʀᴀʀʏ import *
from 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯.ʜᴏᴍᴇ import *



class XeroPlayer(object):
    def __init__(self):
        self.group_call = None 
        self.client = None
        self.chat_id = None
        self.Xero_Clock = None #start_time
        self.playlist = []
        self.msg = {}



    async def send_playlist(self):
        playlist = self.playlist



        if not playlist:
            Xero_Music_List = f"""{XEXO}🎧 𝙢𝙪𝙨𝙞𝙘 𝙡𝙞𝙨𝙩 𝙞𝙨 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙚𝙢𝙥𝙩𝙮 𝙖𝙣𝙙 𝙬𝙖𝙞𝙩𝙞𝙣𝙜 𝙛𝙤𝙧 𝙞𝙣𝙥𝙪𝙩"""

        else:
            if len(playlist) == 1:  
                Xero_Music_List = f"""{XEXO}🎧 [♦  XΣЯӨПӨID DJ   ♦](https://telegra.ph/file/cc35dba04ad629c0771b3.gif)(┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n\n\n"""

            else:
                Xero_Music_List = f"""{XEXO}🎧 [♦  XΣЯӨПӨID DJ   ♦](https://telegra.ph/file/cc35dba04ad629c0771b3.gif)(┛✧Д✧)ヘ♪ 🎧 𝗧𝗵𝗲𝗿𝗲 𝘄𝗲 𝗴𝗼 ♪:-\n\n\n\n"""

            Xero_Music_List += "\n".join([
                f"**{i}**. **[{x.audio.title}]({x.link})**"
                for i, x in enumerate(playlist)])



        if XePlay.msg.get('playlist') is not None:
            await XePlay.msg['playlist'].delete()
        XePlay.msg['playlist'] = await XePlay_Texter(Xero_Music_List)




    async def update_start_time(self, reset=False):
        self.Xero_Clock = (None if reset else datetime.utcnow().replace(microsecond=0))



XePlay = XeroPlayer()



async def XePlay_Texter(text):
    group_call = XePlay.group_call
    client = group_call.client
    chat_id = XePlay.chat_id
    message = await client.send_message(
    chat_id,
    text,
    disable_web_page_preview=False,
    disable_notification=False
    )
    return message