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
& filters.command("clean", prefixes="/"))
async def clean_raw_pcm(client, XS: XeroSpeak):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in XePlay.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    group_call = XePlay.group_call
    chat_id = int("-100" + str(group_call.full_chat.id))
    chat = await client.get_chat(chat_id)


    await client.send_animation(
        animation=xerolink,
        duration=10,
        chat_id=LOGGER_ID,
        caption=f"{XEXO}🎧 𝙓𝙚𝙧𝙤𝙣𝙤𝙞𝙙 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣 **{count}** 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 **{chat.title}**"
    )


    reply = await XS.reply_animation(
        animation=xerolink,
        caption=f"{XEXO}🎧 𝙓𝙚𝙧𝙤𝙣𝙤𝙞𝙙 𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝙝𝙖𝙨 𝙘𝙡𝙚𝙖𝙣 **{count}** 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 **{chat.title}**",
        reply_markup = MIB
        )



    # clean in groups
    await xeronoid_raw_purge(
        (reply, XS),
        CLEAN_REMOVER)