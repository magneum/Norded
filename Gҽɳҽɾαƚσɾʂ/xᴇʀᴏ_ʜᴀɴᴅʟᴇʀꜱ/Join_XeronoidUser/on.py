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
from xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *


@Client.on_message(
filters.group
& Xero_Music_Admins
& filters.chat(CHAT_ID)
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("on", prefixes="/"))
async def join_group_call(client, XS: XeroSpeak):
    group_call = XePlay.group_call
    if not group_call:
        XePlay.group_call = GroupCallFactory(client).get_file_group_call()
        XePlay.group_call.add_handler(
        Xero_Server_Stats,
        GroupCallFileAction.NETWORK_STATUS_CHANGED)
        XePlay.group_call.add_handler(
        playout_ended_handler,
        GroupCallFileAction.PLAYOUT_ENDED)
        await XePlay.group_call.start(XS.chat.id)
        await XS.delete()
        
        
        
        
    if group_call and group_call.is_connected:
        "First Log this event using the userbot"
        group_call = XePlay.group_call
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)        
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧 Userbot has already joined group voice chat in **{chat.title}**"
        )
        
        
        "Now Send the joined info to the requested group"
        await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 Userbot has already joined group voice chat in **{chat.title}**",
            reply_markup = MIB
        )
        
        