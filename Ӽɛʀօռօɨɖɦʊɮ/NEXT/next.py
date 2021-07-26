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

'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'
from ɦǟռɖʟɛʀֆ import *
from ɖօօʍ_ʀօօʍ import *
from ǟʊȶօ_քʊʀɢɛʀ import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *
'⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝'

@Ӽɛʀօռօɨɖ.on_message(
xeronoid_master_filter
& xeronoid_user_filter
& xeronoid_chat_check
& xerofil.command("skip", prefixes="/"))
async def skip_track(client, xemsg: xeromsg):
    xeronoid_music_list = xeroclip.xeronoid_music_list
    if len(xemsg.command) == 1:
        await xeronoid_skip_music_handler()
    else:
        try:
            items = list(dict.fromkeys(xemsg.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(xeronoid_music_list) - 1):
                    audio = f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 [{xeronoid_music_list[i].audio.title}]({xeronoid_music_list[i].link})"
                    xeronoid_music_list.pop(i)
                    text.append(f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 {i}. **{audio}**")
                else:
                    text.append(f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 {i}")
            await client.send_animation(
            animation=xerolink,
            chat_id=LOGGER_ID,
            text=f'{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝘀𝗸𝗶𝗽𝗽𝗶𝗻𝗴 𝗮𝘂𝗱𝗶𝗼',
            duration=10
            )        
            cprint(f'{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝘀𝗸𝗶𝗽𝗽𝗶𝗻𝗴 𝗮𝘂𝗱𝗶𝗼', 'yellow', attrs=['reverse'])
            xeronoid_throw = await xemsg.reply_animation(
            animation=xerolink,
            caption="\n".join(text),
            disable_web_page_preview=False
            )
            await xeroclip.xeronoid_show_playlist()
        except (ValueError, TypeError):
            await client.send_animation(
            animation=xerolink,
            chat_id=LOGGER_ID,
            text=f'{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝗳𝗼𝗿 𝘀𝗸𝗶𝗽𝗽𝗶𝗻𝗴 𝗮𝘂𝗱𝗶𝗼 𝗮𝗻𝗱 𝗳𝗮𝗶𝗹𝗲𝗱',
            duration=10
            )
            xeronoid_throw = await xemsg.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n🎧 𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗶𝗻𝗽𝘂𝘁",disable_web_page_preview=False
            )
            
    await xeronoid_skip_purge((xeronoid_throw, xemsg), SKIP_REMOVER)