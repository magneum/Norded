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
from .xmp import xep
from Ӽɛʀօռօɨɖ.ɖօօʍ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.ʟɨɮʀǟʀʏ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.Ӽɛʀօռօɨɖ_ɖʟƈֆ import *



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

async def network_status_changed_handler(context, is_connected: bool):
    if is_connected:
        xep.xeronoid_chat_verify = MAX_CHANNEL_ID - context.full_chat.id
        await xero_back_sender(f"{emoji.CHECK_MARK_BUTTON} joined the voice chat")
    else:
        await xero_back_sender(f"{emoji.CROSS_MARK_BUTTON} left the voice chat")
        xep.xeronoid_chat_verify = None


async def playout_ended_handler(_, __):
    await skip_current_playing()
