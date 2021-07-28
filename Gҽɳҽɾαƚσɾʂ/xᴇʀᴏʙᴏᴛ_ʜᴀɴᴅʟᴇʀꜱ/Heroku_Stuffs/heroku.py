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
            return await replay_text("`HEROKU_API_KEY` is wrong. Re-Check in config vars.")
        await replay_text(f"✅ **Restarted Dynos** \n**Type** `ping` **after 1 minute to check if I am working !**")
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
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)

@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("(set|get|del)", prefixes="/"))
async def variable(client, XS: XeroSpeak):
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await XS.reply_text( "`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**")
    exe = hell.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        event = await XS.reply_text( "Getting Variable Info...")
        await asyncio.sleep(1.5)
        cap = "Logger me chala jaa bsdk."
        capn = "Saved in LOGGER_ID !!"
        try:
            variable = hell.pattern_match.group(2).split()[0]
            if variable in ("HELLBOT_SESSION", "BOT_TOKEN", "HEROKU_API_KEY"):
                if Config.ABUSE == "ON":
                    await bot.send_file(hell.chat_id, cjb, caption=cap)
                    await event.delete()
                    await bot.send_message(lg_id, f"#HEROKU_VAR \n\n`{heroku_var[variable]}`")
                    return
                else:
                    await event.edit(f"**{capn}**")
                    await bot.send_message(lg_id, f"#HEROKU_VAR \n\n`{heroku_var[variable]}`")
                    return
            if variable in heroku_var:
                return await event.edit(
                    "**Heroku Var** :" f"\n\n`{variable}` = `{heroku_var[variable]}`\n"
                )
            else:
                return await event.edit(
                    "**Heroku Var** :" f"\n\n__Error:__\n-> I doubt `{variable}` exists!"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await hell.client.send_file(
                        hell.chat_id,
                        "configs.json",
                        reply_to=hell.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await event.edit(
                        "**Heroku Var :**\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        event = await XS.reply_text( "Setting Heroku Variable...")
        variable = hell.pattern_match.group(2)
        if not variable:
            return await event.edit(f"`set var <Var Name> <Value>`")
        value = hell.pattern_match.group(3)
        if not value:
            variable = variable.split()[0]
            try:
                value = hell.pattern_match.group(2).split()[1]
            except IndexError:
                return await event.edit(f"`set var <Var Name> <Value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await event.edit(
                f"`{variable}` **successfully changed to**  ->  `{value}`"
            )
        else:
            await event.edit(
                f"`{variable}` **successfully added with value**  ->  `{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        event = await XS.reply_text( "Getting info to delete Variable")
        try:
            variable = hell.pattern_match.group(2).split()[0]
        except IndexError:
            return await event.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await event.edit(f"**Successfully Deleted** \n`{variable}`")
            del heroku_var[variable]
        else:
            return await event.edit(f"`{variable}`  **does not exists**")


@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("usage", prefixes="/"))
async def dyno_usage(client, XS: XeroSpeak):
    event = await edit_or_reply(hell, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
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
        f" ➠ __Dyno usage for__ • **{Config.HEROKU_APP_NAME}** • :\n"
        f"     ★  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  `{AppPercentage}`**%**"
        "\n\n"
        " ➠ __Dyno hours remaining this month__ :\n"
        f"     ★  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  `{percentage}`**%**"
        f"\n\n**Owner :** {hell_mention}"
    )


@Client.on_message(
filters.group
& Xero_Music_Admins
& ~filters.edited
& Known_User
& Xero_Singer
& filters.command("logs", prefixes="/"))
async def _(dyno):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await replay_text(dyno, f"Make Sure Your HEROKU_APP_NAME & HEROKU_API_KEY are filled correct. Visit {hell_grp} for help.", link_preview=False)
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(f"Make Sure Your Heroku AppName & API Key are filled correct. Visit {hell_grp} for help.", link_preview=False)
    hell_data = app.get_log()
    await replay_text(dyno, hell_data, deflink=True, linktext=f"**🗒️ Heroku Logs of 💯 lines. 🗒️**\n\n🌟 **Bot Of :**  {hell_mention}\n\n🚀** Pasted**  ")
    

def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)