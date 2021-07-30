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
& filters.chat(CHAT_ID)
& filters.command("next", prefixes="/"))
async def skip_track(_, XS: XeroSpeak):
    playlist = XePlay.playlist
    if len(XS.command) == 1:
        await skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(XS.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{i}. **{audio}**")
                else:
                    text.append(f"{i}")
            reply = await XS.reply_text(
                "\n".join(text),
                disable_web_page_preview=True
            )
            await XePlay.send_playlist()
        except (ValueError, TypeError):
            reply = await XS.reply_animation(
                animation=xerolink,
                caption=f"{XEXO}🎧 𝗥𝗲𝗰𝗶𝘃𝗲𝗱 𝗪𝗿𝗼𝗻𝗴 𝗜𝗻𝗽𝘂𝘁.𝗧𝗿𝘆 𝗣𝗿𝗼𝗽𝗲𝗿𝗹y",
                reply_markup = MIB,
                disable_web_page_preview=True
                )
            
            
        await xeronoid_next_purge(
            (reply, XS),
            SKIP_REMOVER)