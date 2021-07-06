from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
import shutil
from pyrogram import Client as mapple, idle
from Importing import *


Ӽɛռ = mapple(
    session_name=SN,
    api_id=AD,
    api_hash=AH,
    plugins=ᴄᴇᴘᴛ,
    workers=20
    )
from ᴇᴘɪꜱᴛʟᴇ import *
from Importing import *
LOGS = getLogger(__name__)