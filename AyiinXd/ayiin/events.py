import pybase64
from telethon.tl.functions.channels import JoinChannelRequest as Get
from telethon.tl.types import MessageEntityMentionName
from telethon.errors import rpcerrorlist
from .logger import logging
from .tools import edit_delete
import sys
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

LOGS = logging.getLogger(__name__)

async def get_user_from_event(
    event, yinsevent=None, secondgroup=None, nogroup=False, noedits=False
):
    if yinsevent is None:
        yinsevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-") and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        LOGS.error(f"Error in get_user_from_event: {str(e)}")

    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.sender_id is None:
                if not noedits:
                    await edit_delete(yinsevent, "**ERROR: Dia adalah anonymous admin!**", 60)
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        if not args:
            if not noedits:
                await edit_delete(
                    yinsevent,
                    "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
                    60,
                )
            return None, None
    except Exception as e:
        LOGS.error(f"Error in get_user_from_event: {str(e)}")

    if not noedits:
        await edit_delete(
            yinsevent,
            "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
            60,
        )
    return None, None


async def ajg():
    try:
        print("🔄 Trying to join channels...")
        if bot is not None:
            await bot(Get("juale"))
            await bot(Get("aldesupport"))
            print("✅ Successfully joined channels")
        else:
            print("⚠️ Bot instance is None! Make sure bot is running correctly.")
    except rpcerrorlist.ChannelPrivateError:
        print("❌ Wah Lu Diban Dari Alde Support! Coba ngadu ke @jmany.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

async def checking(client):
    try:
        gocheck = pybase64.b64decode("QGp1YWxl").decode("utf-8").strip()
        checker = pybase64.b64decode("QGFsZGVzdXBwb3J0").decode("utf-8").strip()

        print(f"🔍 Checking channel: {gocheck}, {checker}")

        if client:
            await client(Get(gocheck))
            await client(Get(checker))
        else:
            print("⚠️ Client instance is None! Make sure the client is running correctly.")
    except rpcerrorlist.ChannelPrivateError:
        print("❌ Wah Lu Diban Dari Alde Support!!! Coba Sono Lu Ngadu Ke @jmany Biar Di Unban.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
