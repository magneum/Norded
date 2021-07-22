from HEIST import *
from VEhJU0lTVVNFREZPUlhFUk9OT0lE.Importing.krpt import *


class DeathCharm(object):
    def __init__(self):
        self.voice_chatting = GroupCall(None, path_to_log_file='')
        self.chat_id = None
        self.start_time = None
        self.playlist = []
        self.msg = {}
    async def update_start_time(self, reset=False):
        self.start_time = (
            None if reset
            else datetime.utcnow().replace(microsecond=0)
        )
    async def send_playlist(self):
        playlist = self.playlist
        if not playlist:
            listtrip = LST
        else:
            if len(playlist) == 1:
                listtrip = LSS
            else:
                listtrip = LSS
            listtrip += "\n".join([
                f"**{i}**. **[{x.audio.title}({x.link})**"
                for i, x in enumerate(playlist)
            ])
        if self.msg.get('playlist') is not None:
            await self.msg['playlist'].delete()
        self.msg['playlist'] = await self.send_text(
            listtrip
            )

        if len(playlist) == 1:
            return
        await self.download_audio(playlist[1])
    async def send_text(self, text):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        chat_id = self.chat_id
        message = await client.send_message(
            chat_id,
            text,
            disable_web_page_preview=False,
            disable_notification=False
        )
        return message
    async def skip_current_playing(self):
        voice_chatting = self.voice_chatting
        playlist = self.playlist
        if not playlist:
            return
        if len(playlist) == 1:
            await self.update_start_time()
            return
        client = voice_chatting.client
        raw_hug = os.path.join(client.workdir, fmedaddyy)
        voice_chatting.input_filename = os.path.join(
            raw_hug,
            f"{playlist[1].audio.file_unique_id}.raw"
        )
        await self.update_start_time()
        old_track = playlist.pop(0)
        print(f"- START PLAYING: {playlist[0].audio.title}")
        await self.send_playlist()
        os.remove(os.path.join(
            raw_hug,
            f"{old_track.audio.file_unique_id}.raw")
        )
    async def download_audio(self, ryui: Message):
        voice_chatting = self.voice_chatting
        client = voice_chatting.client
        raw_file = os.path.join(client.workdir, fmedaddyy,
                                f"{ryui.audio.file_unique_id}.raw")
        if not os.path.isfile(raw_file):
            original_file = await ryui.download()
            ffmpeg.input(original_file).output(
                raw_file,
                format='s16le',
                acodec='pcm_s16le',
                ac=2,
                ar='48k',
                loglevel='error'
            ).overwrite_output().run()
            os.remove(original_file)
ʜᴀᴅᴇ = DeathCharm()