"""
Created by @itsz_krish_babess
modified by  @itsz_radha_3030
Userbot plugin for ArankUserbot
"""

from userbot import Arankub
from userbot.core.managers import edit_or_reply
from userbot.helpers import fonts as emojify

plugin_Arankegory = "fun"


@Arankub.Arank_cmd(
    pattern="emoji(?:\s|$)([\s\S]*)",
    command=("emoji", plugin_Arankegory),
    info={
        "header": "Converts your text to big emoji text, with some default emojis.",
        "usage": "{tr}emoji <text>",
        "examples": ["{tr}emoji Arankuserbot"],
    },
)
async def itachi(event):
    "To get emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        await edit_or_reply(
            event, "__What am I Supposed to do with this idiot, Give me a text.__"
        )
        return
    result = ""
    for a in args:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.kakashiemoji[emojify.kakashitext.index(a)]
            result += char
        else:
            result += a
    await edit_or_reply(event, result)


@Arankub.Arank_cmd(
    pattern="cmoji(?:\s|$)([\s\S]*)",
    command=("cmoji", plugin_Arankegory),
    info={
        "header": "Converts your text to big emoji text, with your custom emoji.",
        "usage": "{tr}cmoji <emoji> <text>",
        "examples": ["{tr}cmoji 😺 Arankuserbot"],
    },
)
async def itachi(event):
    "To get custom emoji art text."
    args = event.pattern_match.group(1)
    get = await event.get_reply_message()
    if not args and get:
        args = get.text
    if not args:
        return await edit_or_reply(
            event, "__What am I Supposed to do with this idiot, Give me a text.__"
        )
    try:
        emoji, arg = args.split(" ", 1)
    except Exception:
        arg = args
        emoji = "😺"
    result = ""
    for a in arg:
        a = a.lower()
        if a in emojify.kakashitext:
            char = emojify.itachiemoji[emojify.kakashitext.index(a)].format(cj=emoji)
            result += char
        else:
            result += a
    await edit_or_reply(event, result)
