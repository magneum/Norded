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
from Ӽɛʀօռօɨɖ.ɖօօʍ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.ǟʊȶօ_քʊʀɢɛʀ import *
from Ӽɛʀօռօɨɖ.ʟɨɮʀǟʀʏ_ʀօօʍ import *
from Ӽɛʀօռօɨɖ.Ӽɛʀօռօɨɖʍʊֆɨƈ import *
from Ӽɛʀօռօɨɖ.ƈʊֆȶօʍ_ʄɨʟȶɛʀֆ import *






"Below code is for the XeronoidBot only and will be used for logging purposes also"
@Ӽɛʀօռօɨɖ.on_message(
xero_self_fils
& xero_xemp_fils
& filters.command("raw", prefixes=DYNO_COMMANDK))
async def clean_raw_pcm(client, xeMsg: XeronoidMessageType):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    xeronoid_voixe = xep.xeronoid_voixe
    xeronoid_voixe.stop_playout()
    xeronoid_chat_verify = int("-100" + str(xeronoid_voixe.full_chat.id))
    chat = await client.get_chat(xeronoid_chat_verify)
    all_fn: list[str] = os.listdir(download_dir)
    for track in xep.xeronoid_music_list[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    replybot = await xeMsg.reply_animation(
    animation=xerolink,
    caption=f"{XEXO} The userbot has successfully cleaned {count} files"
    )
    await client.send_animation(
    animation=xerolink,
    duration=10,
    chat_id=LOGGER_ID,
    caption=f"{XEXO} The userbot has successfully cleaned {count} files in **{chat.title}**"
    )
    await xeronoid_raw_purge((replybot, xeMsg), RAW_REMOVER)