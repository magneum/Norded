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

from ʟɨɮʀǟʀʏ_ʀօօʍ import *
from ɖօօʍ_ʀօօʍ import *
from .xeroobj import xeroclip


async def xeronoid_skip_music_handler():
    xeronoid_musical_xhat = xeroclip.xeronoid_musical_xhat
    xeronoid_music_list = xeroclip.xeronoid_music_list
    if not xeronoid_music_list:
        return
    if len(xeronoid_music_list) == 1:
        await xeroclip.xeronoid_begin_clock()
        return
    client = xeronoid_musical_xhat.client
    download_dir = os.path.join(client.workdir, xeronoid_dl_dir)
    xeronoid_musical_xhat.input_filename = os.path.join(
        download_dir,
        f"{xeronoid_music_list[1].audio.file_unique_id}.raw"
        )
    await xeroclip.xeronoid_begin_clock()
    old_track = xeronoid_music_list.pop(0)
    print(f"{XEXO}🚀🔥 ΉYPΣ VӨID LΛB 🔥🚀\n\n|========	Ӽɛʀօռօɨɖ ռօա քʟǟʏɨռɢ: {xeronoid_music_list[0].audio.title}")
    await xeroclip.xeronoid_show_playlist()
    os.remove(os.path.join(
        download_dir,
        f"{old_track.audio.file_unique_id}.raw")
        )
    if len(xeronoid_music_list) == 1:
        return
    await xeronoid_music_dl_handler(xeronoid_music_list[1])
    
    
    
async def xeronoid_music_dl_handler(xemsg: xeromsg):
    xeronoid_musical_xhat = xeroclip.xeronoid_musical_xhat
    client = xeronoid_musical_xhat.client
    raw_file = os.path.join(
    client.workdir,
    xeronoid_dl_dir,
    f"{xemsg.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        xeronoid_raw_media = await xemsg.download()
        ffmpeg.input(xeronoid_raw_media).output(
        raw_file,
        format='s16le',acodec='pcm_s16le',ac=2,ar='48k',loglevel='debug'#'error'
        ).overwrite_output().run()
        os.remove(xeronoid_raw_media)