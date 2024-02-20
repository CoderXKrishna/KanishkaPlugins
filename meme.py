import asyncio

from userbot import Arankub
from userbot.core.managers import edit_or_reply

plugin_Arankegory = "fun"


@Arankub.Arank_cmd(
    pattern="^\:/$",
    command=("\:", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": "\:",
    },
)
async def kek(keks):
    "Animation command"
    keks = await edit_or_reply(keks, ":\\")
    uio = ["/", "\\"]
    for i in range(15):
        await asyncio.sleep(0.5)
        txt = f":{uio[i % 2]}"
        await keks.edit(txt)


@Arankub.Arank_cmd(
    pattern="^\-_-$",
    command=("-_-", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": "-_-",
    },
)
async def lol(lel):
    "Animation command"
    lel = await edit_or_reply(lel, "-__-")
    okay = "-__-"
    for _ in range(15):
        await asyncio.sleep(0.5)
        okay = f"{okay[:-1]}_-"
        await lel.edit(okay)


@Arankub.Arank_cmd(
    pattern="^\;_;$",
    command=(";_;", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": ";_;",
    },
)
async def fun(e):
    "Animation command"
    e = await edit_or_reply(e, ";__;")
    t = ";__;"
    for _ in range(15):
        await asyncio.sleep(0.5)
        t = f"{t[:-1]}_;"
        await e.edit(t)


@Arankub.Arank_cmd(
    pattern="oof$",
    command=("oof", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": "{tr}oof",
    },
)
async def Oof(e):
    "Animation command."
    t = "Oof"
    Arankevent = await edit_or_reply(e, t)
    for _ in range(15):
        await asyncio.sleep(0.5)
        t = f"{t[:-1]}of"
        await Arankevent.edit(t)


@Arankub.Arank_cmd(
    pattern="type ([\s\S]*)",
    command=("type", plugin_Arankegory),
    info={
        "header": "Type writter animation.",
        "usage": "{tr}type text",
    },
)
async def typewriter(typew):
    "Type writter animation."
    message = typew.pattern_match.group(1)
    sleep_time = 0.2
    typing_symbol = "|"
    old_text = ""
    typew = await edit_or_reply(typew, typing_symbol)
    await asyncio.sleep(sleep_time)
    for character in message:
        old_text = f"{old_text}{character}"
        typing_text = f"{old_text}{typing_symbol}"
        await typew.edit(typing_text)
        await asyncio.sleep(sleep_time)
        await typew.edit(old_text)
        await asyncio.sleep(sleep_time)


@Arankub.Arank_cmd(
    pattern="repeat (\d*) ([\s\S]*)",
    command=("repeat", plugin_Arankegory),
    info={
        "header": "repeats the given text with given no of times.",
        "usage": "{tr}repeat <count> <text>",
        "examples": "{tr}repeat 10 Arankuserbot",
    },
)
async def _(event):
    "To repeat the given text."
    Arank = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = Arank[1]
    count = int(Arank[0])
    repsmessage = (f"{message} ") * count
    await edit_or_reply(event, repsmessage)


@Arankub.Arank_cmd(
    pattern="meme",
    command=("meme", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": [
            "{tr}meme <emoji/text>",
            "{tr}meme",
        ],
    },
)
async def meme(event):
    "Animation command."
    memeVar = event.text
    sleepValue = 0.5
    memeVar = memeVar[6:]
    if not memeVar:
        memeVar = "✈️"
    event = await edit_or_reply(event, f"-------------{memeVar}")
    await asyncio.sleep(sleepValue)
    await event.edit(f"------------{memeVar}-")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-----------{memeVar}--")
    await asyncio.sleep(sleepValue)
    await event.edit(f"----------{memeVar}---")
    await asyncio.sleep(sleepValue)
    await event.edit(f"---------{memeVar}----")
    await asyncio.sleep(sleepValue)
    await event.edit(f"--------{memeVar}-----")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-------{memeVar}------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"------{memeVar}-------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-----{memeVar}--------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"----{memeVar}---------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"---{memeVar}----------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"--{memeVar}-----------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-{memeVar}------------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"{memeVar}-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-------------{memeVar}")
    await asyncio.sleep(sleepValue)
    await event.edit(f"------------{memeVar}-")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-----------{memeVar}--")
    await asyncio.sleep(sleepValue)
    await event.edit(f"----------{memeVar}---")
    await asyncio.sleep(sleepValue)
    await event.edit(f"---------{memeVar}----")
    await asyncio.sleep(sleepValue)
    await event.edit(f"--------{memeVar}-----")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-------{memeVar}------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"------{memeVar}-------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-----{memeVar}--------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"----{memeVar}---------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"---{memeVar}----------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"--{memeVar}-----------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"-{memeVar}------------")
    await asyncio.sleep(sleepValue)
    await event.edit(f"{memeVar}-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar)


@Arankub.Arank_cmd(
    pattern="give",
    command=("give", plugin_Arankegory),
    info={
        "header": "Animation command",
        "usage": [
            "{tr}give <emoji/text>",
            "{tr}give",
        ],
    },
)
async def give(event):
    "Animation command."
    giveVar = event.text
    sleepValue = 0.5
    lp = giveVar[6:]
    if not lp:
        lp = " 🍭"
    event = await edit_or_reply(event, f"{lp}        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)
    await asyncio.sleep(sleepValue)
    await event.edit(f"{lp}        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)


@Arankub.Arank_cmd(
    pattern="sadmin$",
    command=("sadmin", plugin_Arankegory),
    info={
        "header": "Shouts Admin Animation command",
        "usage": "{tr}sadmin",
    },
)
async def _(event):
    "Shouts Admin Animation command."
    animation_ttl = range(13)
    event = await edit_or_reply(event, "sadmin")
    animation_chars = [
        "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",
        "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",
        "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",
        "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",
        "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",
        "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",
        "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",
        "@aaaaaaddddddmmmmmmiiiiiinnnnnn",
        "@aaaaadddddmmmmmiiiiinnnnn",
        "@aaaaddddmmmmiiiinnnn",
        "@aaadddmmmiiinnn",
        "@aaddmmiinn",
        "@admin",
    ]
    for i in animation_ttl:
        await asyncio.sleep(1)
        await event.edit(animation_chars[i % 13])
