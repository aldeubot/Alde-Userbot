# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**𝙃𝙖𝙙𝙞𝙧 𝙙𝙤𝙣𝙜 𝙏𝙤𝙙** 😁",
    "**𝙃𝙖𝙙𝙞𝙧 𝙆𝙖𝙠𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 😉",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘾𝙤𝙣𝙩𝙤𝙡** 😁",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 🥵",
    "**𝙃𝙖𝙙𝙞𝙧 𝙉𝙜𝙖𝙗** 😎",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘼𝙗𝙖𝙣𝙜** 🥺",
    "**𝙎𝙞 𝘾𝙖𝙠𝙚𝙥 𝙃𝙖𝙙𝙞𝙧 𝘽𝙖𝙣𝙜** 😎",
    "**Hadir kak maap telat** 🥺",
    "**Hadir Tuan** 🙏🏻",
    "**Hadir Majikan** 🙏🏻",
    "**Hadir Sayang** 😳",
    "**Hadir Bro Mapand** 😁",
    "**Maaf ka habis nemenin ka Alde** 🥺",
    "**Maaf ka habis disuruh Tuan Alde** 🥺🙏🏻",
    "**Hadir Mapand Sayang** 😘",
    "**Hadir Mapand Akuuuuhhh** ☺️",
    "**Hadir Mapand brother Aku** 🥰",
]

kazucakep = [
    "**𝙄𝙮𝙖 mapand 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝙆𝙖𝙢𝙪 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣 pand** 😍",
    "**𝙄𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙆𝙖𝙢𝙪 𝙅𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]


@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**㋡ ᴀʟᴅᴇ ᴜꜱᴇʀʙᴏᴛ ㋡**\n\n㋡ **ᴘɪɴɢᴇʀ :** `{} ms`\n㋡ **ᴜᴘᴛɪᴍᴇ :** `{}`\n㋡ **ᴏᴡɴᴇʀ :** `{}`\n㋡ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^Absen$")
async def kazuabsen(ganteng):
    await ganteng.reply(choice(absen))

@register(incoming=True, from_users=DEVS, pattern=r"^aldean$")
async def naya(naya):
    await naya.reply("**Aldean Tampan**🤩")

@register(incoming=True, from_users=DEVS, pattern=r"^Aku ganteng kan$")
async def kazu(ganteng):
    await ganteng.reply(choice(kazucakep))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `Mapandping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs ᴍᴀᴘᴀɴᴅ ᴜsᴇʀʙᴏᴛ Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
