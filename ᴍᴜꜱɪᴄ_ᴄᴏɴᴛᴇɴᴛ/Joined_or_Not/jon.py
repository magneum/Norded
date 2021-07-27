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
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ.Playlist_Semi import skip_current_playing
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ.XeroPlayer import XePlay
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *




async def Xero_Server_Stats(context, is_connected: bool):
    if is_connected:
        XePlay.chat_id = MAX_CHANNEL_ID - context.full_chat.id

        await XePlay_Texter(f"{XEXO}Xeronoid Userbot has been connected")
    else:
        
        await XePlay_Texter(f"{XEXO}Xeronoid Userbot left the voice chat")
        XePlay.chat_id = None




async def playout_ended_handler(_, __):
    await skip_current_playing()



async def XePlay_Texter(text):
    Xero_Voixe = XePlay.Xero_Voixe
    client = Xero_Voixe.client
    chat_id = XePlay.chat_id
    message = await client.send_message(
        chat_id,
        text,
        disable_web_page_preview=True,
        disable_notification=True
    )
    return message