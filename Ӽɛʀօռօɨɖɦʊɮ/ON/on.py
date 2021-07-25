""" 
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|----------------------------------------------------------------------------------------|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|----------------------------------------------------------------------------------------|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
"""

'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
from ɦǟռɖʟɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'


@Ӽɛʀօռօɨɖ.on_message(
xeronoid_master_filter
& xeronoid_user_filter
& xerofil.command("on", prefixes="/"))
async def join_group_call(client, xemsg: xeromsg):
    group_call = xeroclip.group_call
    if not group_call:
        xeroclip.group_call = gcfact(client).get_file_group_call()
        xeroclip.group_call.add_handler(network_status_changed_handler,
                                  xeronoid_gcf.NETWORK_STATUS_CHANGED)
        xeroclip.group_call.add_handler(xeronoid_music_over_handler,
                                  xeronoid_gcf.PLAYOUT_ENDED)
        await xeroclip.group_call.start(xemsg.chat.id)
        await xemsg.delete()
    if group_call and group_call.is_connected:
        cprint('🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝘀𝘁𝗮𝗿𝘁 𝘁𝗵𝗲 𝗯𝗼𝘁', 'yellow', attrs=['reverse'])
        xemsg.reply_text("🎧 𝗜𝗻𝗶𝘁𝗶𝗮𝘁𝗲𝗱 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗽𝗼𝘄𝗲𝗿_𝘂𝗽 𝘀𝗲𝗾𝘂𝗲𝗻𝗰𝗲!")
        await xemsg.reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗫𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝘂𝘀𝗲𝗿𝗯𝗼𝘁 𝗵𝗮𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗷𝗼𝗶𝗻𝗲𝗱 𝗮 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁"
        )
        
        await xeronoid_join_purge((xemsg, xemsg), JOIN_REMOVER)