"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *




@Client.on_message(
filters.group
& filters.command("group", prefixes="/"))
async def list_voice_chat(client, m: Message):
    group_call = mp.group_call
    if group_call and group_call.is_connected:
        
        print(f"{XEXO}(IN_GROUP)\nUserbot has requested Xeronoidbot to show where the userbot is_plugged ")
        
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}(IN_GROUP)\nUserbot has requested Xeronoidbot to show where the userbot is_plugged"
        )
        
        group_info = await m.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}Userbot is plugged in the voice chat"    
        )
        
        
    else:
        print(f"{XEXO}(IN_GROUP)\nUserbot has requested Xeronoidbot to show where the userbot is_plugged")
        
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}(IN_GROUP)\nUserbot has requested Xeronoidbot to show where the userbot is_plugged but userbot is not plugged yet"
        )
        
        group_info = await m.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}Userbot is not plugged in any voice chat yet")
        
    # delete help info in group chats to keep it clean no matter what 
    await xeronoid_help_purge(
        (group_info,m),
        GROUP_REMOVER)