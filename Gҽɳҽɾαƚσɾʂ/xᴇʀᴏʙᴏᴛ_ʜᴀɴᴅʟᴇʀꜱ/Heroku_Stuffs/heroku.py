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
from xᴇʀᴏꜰɪʟᴇᴛꜱ.butts import MIB,SIB
from ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
heroku_api = "https://api.heroku.com"
Heroku = heroku3.from_key(HEROKU_API_KEY)
lg_id = LOGGER_ID



async def restart(client, XS: XeroSpeak):
    if HEROKU_APP_NAME and HEROKU_API_KEY:
        try:
            Heroku
        except BaseException:
            return await XS.replay_text("`HEROKU_API_KEY` is wrong. Re-Check in config vars.")
        await XS.replay_text(f"✅ **Restarted Dynos** \n**Type** /xero **after 1 minute to check if I am working !**")
        app = Heroku.apps()[HEROKU_APP_NAME]
        app.restart()
    else:
        os.system("python3 hypefile.py")


@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("restart", prefixes="/"))
async def re(client, XS: XeroSpeak):
    event = await XS.reply_text( "Restarting Dynos ...")
    if HEROKU_API_KEY:
        await restart(event)
    else:
        await event.edit("Please Set Your `HEROKU_API_KEY` to restart Ӽɛʀօռօɨɖ")


@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("shutdown", prefixes="/"))
async def down(client, XS: XeroSpeak):
    event = await XS.reply_text( "`Turing Off Heroku Dynos...`")
    await asyncio.sleep(2)
    await event.edit("**[ ⚠️ ]** \n**Ӽɛʀօռօɨɖ Dynos is now turned off. Manually turn it on to start again.**")
    if HEROKU_APP_NAME is not None:
        HEROKU_APP_NAME.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)
@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("usage", prefixes="/"))
async def dyno_usage(client, XS: XeroSpeak):
    event = await XS.reply_text( "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await event.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)

    """ - Current - """
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await event.edit(
        "⚡ **Dyno Usage** ⚡:\n\n"
        f" ➠ __Dyno usage for__ • **{HEROKU_APP_NAME}** • :\n"
        f"     ★  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  `{AppPercentage}`**%**"
        "\n\n"
        " ➠ __Dyno hours remaining this month__ :\n"
        f"     ★  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  `{percentage}`**%**"
        f"\n\n**Owner :** {OWNER_USERNAME}"
    )