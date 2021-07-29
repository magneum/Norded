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
from ɦʏքɛʋօɨɖʟǟɮ.xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ɦʏքɛʋօɨɖʟǟɮ.ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ɦʏքɛʋօɨɖʟǟɮ.ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from ɦʏքɛʋօɨɖʟǟɮ.xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʟɪʙʀᴀʀʏ import *
from ɦʏքɛʋօɨɖʟǟɮ.ʜᴏᴍᴇ import *


@Client.on_message(
filters.group
& ~filters.edited
& Xero_Music_Admins
& filters.chat(CHAT_ID)
& filters.command("group", prefixes="/"))
async def list_voice_chat(client, XS: XeroSpeak):
    group_call = XePlay.group_call
    if group_call and group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧 (IN_GROUP)\n𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝗼𝗳:**{chat.title}**"
            )


        group_info = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗶𝘀 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗶𝗻 𝘁𝗵𝗲 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝗼𝗳 **{chat.title}**",
            reply_markup = MIB    
        )
       
    else:
        # await client.send_animation(
        #     animation=xerolink,
        #     duration=10,
        #     chat_id=LOGGER_ID,
        #     caption=f"{XEXO}🎧 (IN_GROUP)\nXeronoid Userbot has not been plugged yet"
        #     )


        
        group_info = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗽𝗹𝘂𝗴𝗴𝗲𝗱 𝗶𝗻 𝗮𝗻𝘆 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁 𝘆𝗲𝘁",
            reply_markup = MIB
            )
        

    # delete help info in group chats to keep it clean no matter what 
    await xeronoid_help_purge(
        (group_info,XS),
        GROUP_REMOVER)