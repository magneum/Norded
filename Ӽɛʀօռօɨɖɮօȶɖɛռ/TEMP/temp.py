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
xeronoid_bot_master_filter 
& xerofil.chat(CHAT_ID)
& xerofil.command("temp", prefixes="/"))
async def clean_raw_pcm(client, xemsg: xeromsg):
    download_dir = os.path.join(client.workdir, xeronoid_dl_dir)
    all_fn: list[str] = os.listdir(download_dir)
    for track in xeroclip.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    await xemsg.reply_chat_action("choose_contact")
    await client.send_animation(
    chat_id=LOGGER_ID,
    animation=xerolink,
    duration=10,
    text=f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝗨𝘀𝗲𝗿 𝗮𝘀𝗸𝗲𝗱 𝘁𝗼 𝗰𝗹𝗲𝗮𝗻 𝘁𝗵𝗲 𝗿𝗮𝘄 𝗳𝗶𝗹𝗲𝘀 𝗼𝗳 𝘁𝗵𝗲 𝗯𝗼𝘁"
    )
    xemsg.reply_text("🎧 𝗜𝗻𝗶𝘁𝗶𝗮𝘁𝗲𝗱 𝘅𝗲𝗿𝗼𝗻𝗼𝗶𝗱 𝗰𝗹𝗲𝗮𝗻𝘂𝗽 𝘀𝗲𝗾𝘂𝗲𝗻𝗰𝗲!")            
    xeronoid_throw = await xemsg.reply_animation(
    animation=xerolink,
    caption=f"""{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	🎧 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙘𝙡𝙚𝙖𝙣𝙚𝙙 {count} 𝙧𝙖𝙬 𝙛𝙞𝙡𝙚𝙨    
    """)
    
    await xeronoid_throw_purge((xeronoid_throw, xemsg), CLEAN_REMOVER)