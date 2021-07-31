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
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ.Playlist_Semi import skip_current_playing
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ.XeroPlayer import XePlay
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʜᴏᴍᴇ import *




async def Xero_Server_Stats(context, is_connected: bool):
    if is_connected:
        XePlay.chat_id = MAX_CHANNEL_ID - context.full_chat.id
        ON = await XePlay_Texter(f"{XEXO}🎧 [𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗲𝗱 𝗶𝗻 𝘁𝗵𝗶𝘀 𝗚𝗿𝗼𝘂𝗽'𝘀 𝗩𝗼𝗶𝗰𝗲 𝗖𝗵𝗮𝘁](https://telegra.ph/file/cc35dba04ad629c0771b3.gif)")
        await asyncio.sleep(3)
        await ON.delete()
    else:
        OFF = await XePlay_Texter(f"{XEXO}🎧 [𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗹𝗲𝗳𝘁 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗚𝗿𝗼𝘂𝗽](https://telegra.ph/file/cc35dba04ad629c0771b3.gif)")
        await asyncio.sleep(3)
        await OFF.delete()
        XePlay.chat_id = None




async def playout_ended_handler(_, __):
    await skip_current_playing()



async def XePlay_Texter(text):
    group_call = XePlay.group_call
    client = group_call.client
    chat_id = XePlay.chat_id
    message = await client.send_message(
        chat_id,
        text,
        disable_web_page_preview=False,
        disable_notification=True
    )
    return message



