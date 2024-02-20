#  Copyright (C) 2020  krishna.n(π.$)
# credits to @itsz_radha_3030
import asyncio
import os
import re

from userbot import Arankub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.utils import reply_id
from userbot.plugins import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_Arankegory = "fun"


@Arankub.Arank_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_Arankegory),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs Arankuserbot ; One of the Popular userbot",
    },
)
async def nekobot(Arank):
    "Fake google search meme"
    text = Arank.pattern_match.group(1)
    reply_to_id = await reply_id(Arank)
    if not text:
        if Arank.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(Arank, "`What should i search in google.`", 5)
    Aranke = await edit_or_reply(Arank, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            Arank,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    Arankfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)


@Arankub.Arank_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_Arankegory),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump Arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(Arank):
    "trump tweet sticker with given custom text_"
    text = Arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(Arank)

    reply = await Arank.get_reply_message()
    if not text:
        if Arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(Arank, "**Trump : **`What should I tweet`", 5)
    Aranke = await edit_or_reply(Arank, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    Arankfile = await trumptweet(text)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)


@Arankub.Arank_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_Arankegory),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi Arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(Arank):
    "modi tweet sticker with given custom text"
    text = Arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(Arank)

    reply = await Arank.get_reply_message()
    if not text:
        if Arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(Arank, "**Modi : **`What should I tweet`", 5)
    Aranke = await edit_or_reply(Arank, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    Arankfile = await moditweet(text)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)


@Arankub.Arank_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_Arankegory),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm Arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(Arank):
    text = Arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(Arank)

    reply = await Arank.get_reply_message()
    if not text:
        if Arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(Arank, "`Give text to write on banner, man`", 5)
    Aranke = await edit_or_reply(Arank, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    Arankfile = await changemymind(text)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)


@Arankub.Arank_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_Arankegory),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna Arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(Arank):
    "kanna chan sticker with given custom text"
    text = Arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(Arank)

    reply = await Arank.get_reply_message()
    if not text:
        if Arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(Arank, "**Kanna : **`What should i show you`", 5)
    Aranke = await edit_or_reply(Arank, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    Arankfile = await kannagen(text)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)


@Arankub.Arank_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_Arankegory),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; Arankuserbot is One of the Popular userbot",
    },
)
async def nekobot(Arank):
    "The desired person tweet sticker with given custom text"
    text = Arank.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(Arank)

    reply = await Arank.get_reply_message()
    if not text:
        if Arank.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                Arank,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            Arank,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    Aranke = await edit_or_reply(Arank, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    Arankfile = await tweets(text, username)
    await Arank.client.send_file(Arank.chat_id, Arankfile, reply_to=reply_to_id)
    await Aranke.delete()
    if os.path.exists(Arankfile):
        os.remove(Arankfile)
