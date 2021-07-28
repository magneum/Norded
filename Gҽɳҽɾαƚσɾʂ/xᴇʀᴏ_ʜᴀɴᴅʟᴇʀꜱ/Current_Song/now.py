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
& filters.chat(CHAT_ID)
& ~filters.edited
& ~filters.via_bot
& Xero_Singer
& filters.command("now", prefixes="/"))
async def show_current_playing_time(_, XS: XeroSpeak):
    Xero_Clock = XePlay.Xero_Clock
    playlist = XePlay.playlist
    if not Xero_Clock:
        empty = await XS.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 No Song is in xeronoid music server yet",
            reply_markup = MIB
        )
        await xeronoid_now_purge(
            (empty, XS),
            CURRENT_REMOVER)
        return
    

    
    if XePlay.msg.get('now') is not None:
        await XePlay.msg['now'].delete()
        
        
    XePlay.msg['now'] = await playlist[0].reply_text(
        f"{utcnow - Xero_Clock} / {timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    
    await XS.delete()