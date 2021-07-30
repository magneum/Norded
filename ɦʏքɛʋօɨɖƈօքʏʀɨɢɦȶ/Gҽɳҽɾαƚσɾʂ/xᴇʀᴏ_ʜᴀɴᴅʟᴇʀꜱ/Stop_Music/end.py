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
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖƈօքʏʀɨɢɦȶ.ʜᴏᴍᴇ import *


@Client.on_message(
filters.group
& ~filters.edited
& Known_admins
& Xero_Singer
& filters.command("end", prefixes="/"))
async def stop_playing(client, XS: XeroSpeak):
    group_call = XePlay.group_call
    group_call.stop_playout()

 
    "Firsly Log this event using Xeronoid Userbot"
    chat_id = int("-100" + str(group_call.full_chat.id))
    chat = await client.get_chat(chat_id) 
    await client.send_animation(
        animation=xerolink,
        duration=10,
        chat_id=LOGGER_ID,
        caption=f"{XEXO}🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻\n**{chat.title}**"
    )
    
    "Now end the music loop and send information in the requested chat"
    reply = await XS.reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝘀𝘁𝗼𝗽𝗽𝗲𝗱 𝗽𝗹𝗮𝘆𝗶𝗻𝗴 𝗺𝘂𝘀𝗶𝗰 𝗶𝗻\n**{chat.title}**",
        reply_markup = MIB
        )
    await XePlay.update_start_time(reset=True)
        
    # Now clean the chat room and player and then idle the player
    XePlay.playlist.clear()
    await xeronoid_end_purge(
        (reply, XS),
        STOP_REMOVER)