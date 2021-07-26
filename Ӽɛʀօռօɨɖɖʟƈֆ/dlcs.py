"""⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|
                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.

                        ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
|••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|       
⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋 Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝"""


from ɖօօʍ_ʀօօʍ import *
from Ӽɛʀօռօɨɖʍʊֆɨƈ.xmp import *
from ʟɨɮʀǟʀʏ_ʀօօʍ import *


async def xeronoid_skip_music_handler():
    group_call = xep.group_call
    if not group_call:
        return
    if len(group_call) == 1:
        await xep.update_start_time()
        return
    client = group_call.client
    download_dir = os.path.join(client.workdir, xeronoid_dl_dir)
    group_call.input_filename = os.path.join(
    download_dir,
    f"{group_call[1].audio.file_unique_id}.raw")
    await xep.update_start_time()
    old_track = group_call.pop(0)
    print(f"• START PLAYING: {group_call[0].audio.title}")
    await xep.send_playlist()
    os.remove(os.path.join(
        download_dir,
        f"{old_track.audio.file_unique_id}.raw")
    )
    if len(group_call) == 1:
        return
    await xeronoid_music_dl_handler(group_call[1])


async def xeronoid_music_dl_handler(xemsg: xeromsg):
    group_call = xep.group_call
    client = group_call.client
    raw_file = os.path.join(client.workdir, xeronoid_dl_dir,
                            f"{xemsg.audio.file_unique_id}.raw")
    if not os.path.isfile(raw_file):
        original_file = await xemsg.download()
        ffmpeg.input(original_file).output(
            raw_file,
            format='s16le',
            acodec='pcm_s16le',
            ac=2,
            ar='48k',
            loglevel='error'
        ).overwrite_output().run()
        os.remove(original_file)