# by:koala @mixiologist
# Lord Userbot

from telethon.events import ChatAction

from userbot import DEVS, bot
from userbot.events import register
from userbot.utils import get_user_from_event, ayiin_cmd

# Ported For Lord-Userbot by liualvinas/Alvin


@bot.on(ChatAction)
async def handler(tele):
    if not tele.user_joined and not tele.user_added:
        return
    try:
        from userbot.modules.sql_helper.gmute_sql import is_gmuted

        guser = await tele.get_user()
        gmuted = is_gmuted(guser.id)
    except BaseException:
        return
    if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):
                chat = await tele.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if admin or creator:
                    try:
                        await client.edit_permissions(
                            tele.chat_id, guser.id, view_messages=False
                        )
                        await tele.reply(
                            f"**ππ½ππ£π£ππ ππ₯π€π©ππ** \n"
                            f"**πππ§π¨π© πππ’π :** [{guser.id}](tg://user?id={guser.id})\n"
                            f"**πΌππ©ππ€π£ :** `π½ππ£π£ππ`"
                        )
                    except BaseException:
                        return


@ayiin_cmd(pattern="gban(?: |$)(.*)")
@register(pattern=r"^\$cgband(?: |$)(.*)", sudo=True)
async def gben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`ππͺπ ππ§π€π¨ππ¨ ππππ£π£ππ£π πππ ππ§ππ£π ππ€π...`")
    else:
        dark = await dc.edit("`πππ’π₯π§π€π¨ππ¨ ππ‘π€πππ‘ π½ππ£π£ππ πππ©ππ¨ππ£ πΏπππππ‘..`")
    me = await userbot.client.get_me()
    await dark.edit("`βοΈ ππ‘π€πππ‘ π½ππ£π£ππ πΌπ ππ£ πΌπ π©ππ ππ€π..`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**πΌπ£πππ£π πππππ‘ ππ‘π€πππ‘ π½ππ£π£ππ :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit("**πππππ‘ ππ‘π€πππ‘ π½ππ£π£ππ ππ€π, πππ§π£π πΏππ πΌπππ‘ππ π½π€π¨π¨ ππͺπ π€ͺ**")
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await dark.edit(
                    r"\\**#ππ½ππ£π£ππ_ππ¨ππ§**//"
                    f"\n\n**πππ§π¨π© πππ’π:** [{user.first_name}](tg://user?id={user.id})\n"
                    f"**ππ¨ππ§ ππΏ:** `{user.id}`\n"
                    f"**πΌππ©ππ€π£:** `ππ‘π€πππ‘ π½ππ£π£ππ`"
                )
            except BaseException:
                b += 1
    else:
        await dark.edit("**π½ππ‘ππ¨ ππ πππ¨ππ£ πππ£πππͺπ£ππ£π?π ππ€ππ‘π€π **")
    try:
        if gmute(user.id) is False:
            return await dark.edit(
                "**#πΌπ‘π§ππππ?_ππ½ππ£π£ππ**\n\nππ¨ππ§ πΌπ‘π§ππππ? ππ­ππ¨π©π¨ ππ£ ππ? ππππ£ πππ¨π©.**"
            )

    except BaseException:
        pass
    return await dark.edit(
        r"\\**#ππ½ππ£π£ππ_ππ¨ππ§**//"
        f"\n\n**πππ§π¨π© πππ’π:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**ππ¨ππ§ ππΏ:** `{user.id}`\n"
        f"**πΌππ©ππ€π£:** `ππ‘π€πππ‘ π½ππ£π£ππ π½π?:{me.first_name}`"
    )


@ayiin_cmd(pattern=r"ungban(?: |$)(.*)")
@register(pattern=r"^\$cungban(?: |$)(.*)", sudo=True)
async def gunben(userbot):
    dc = userbot
    sender = await dc.get_sender()
    me = await dc.client.get_me()
    if sender.id != me.id:
        dark = await dc.reply("`ππ£ππππ£π£ππ£π...`")
    else:
        dark = await dc.edit("`ππ£ππππ£π£ππ£π....`")
    me = await userbot.client.get_me()
    await dark.edit("`πππ’πππ©ππ‘π ππ£ πππ§ππ£π©ππ ππ‘π€πππ‘ π½ππ£π£ππ`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    try:
        user, reason = await get_user_from_event(userbot)
    except BaseException:
        pass
    try:
        if not reason:
            reason = "Private"
    except BaseException:
        return await dark.edit("**πππππ‘ ππ£ππππ£π£ππ :(**")
    if user:
        if user.id in DEVS:
            return await dark.edit(
                "**πΌπ?πππ£ πππππ  π½ππ¨π πππ§π ππ£π πππ§ππ£π©ππ ππ£π, πππ§ππ£π πΏππ πππ’ππͺππ© πππ?π**"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except BaseException:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await dark.edit("`πππ’πππ©ππ‘π ππ£ ππ‘π€πππ‘ π½ππ£π£ππ...`")
            except BaseException:
                b += 1
    else:
        await dark.edit("`π½ππ‘ππ¨ ππ πππ¨ππ£ πππ£πππͺπ£ππ£π?π ππ€ππ‘π€π `")
    try:
        if ungmute(user.id) is False:
            return await dark.edit("**ππ§π§π€π§! πππ£πππͺπ£π πππππ£π πππππ  πΏπ ππ‘π€πππ‘ π½ππ£π£ππ.**")
    except BaseException:
        pass
    return await dark.edit(
        r"\\**#ππ£ππππ£π£ππ_ππ¨ππ§**//"
        f"\n\n**πππ§π¨π© πππ’π:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**ππ¨ππ§ ππΏ:** `{user.id}`\n"
        f"**πΌππ©ππ€π£:** `ππ£ππππ£π£ππ π½π? {me.first_name}`"
    )
