import random

from userbot import Arankub
from userbot.core.managers import edit_or_reply
from userbot.plugins import fonts

plugin_Arankegory = "extra"


@Arankub.Arank_cmd(
    pattern="fmusical(?:\s|$)([\s\S]*)",
    command=("fmusical", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}fmusical <text>",
            "{tr}fmusical reply this command to text message",
        ],
        "examples": "{tr}fmusical Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="ancient(?:\s|$)([\s\S]*)",
    command=("ancient", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}ancient <text>",
            "{tr}ancient reply this command to text message",
        ],
        "examples": "{tr}ancient Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="vapor(?:\s|$)([\s\S]*)",
    command=("vapor", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}vapor <text>", "{tr}vapor reply this command to text message"],
        "examples": "{tr}vapor Arankuserbot",
    },
)
async def vapor(event):
    "Changes font style of the given text"
    reply_text = []
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(event, "`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await edit_or_reply(event, "".join(reply_text))


@Arankub.Arank_cmd(
    pattern="smallcaps(?:\s|$)([\s\S]*)",
    command=("smallcaps", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}smallcaps <text>",
            "{tr}smallcaps reply this command to text message",
        ],
        "examples": "{tr}smallcaps Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="blackbf(?:\s|$)([\s\S]*)",
    command=("blackbf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}blackbf <text>",
            "{tr}blackbf reply this command to text message",
        ],
        "examples": "{tr}blackbf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="bubbles(?:\s|$)([\s\S]*)",
    command=("bubbles", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}bubbles <text>",
            "{tr}bubbles reply this command to text message",
        ],
        "examples": "{tr}bubbles Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="tanf(?:\s|$)([\s\S]*)",
    command=("tanf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}tanf <text>", "{tr}tanf reply this command to text message"],
        "examples": "{tr}tanf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="boxf(?:\s|$)([\s\S]*)",
    command=("boxf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}boxf <text>", "{tr}boxf reply this command to text message"],
        "examples": "{tr}boxf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="smothtext(?:\s|$)([\s\S]*)",
    command=("smothtext", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}smothtext <text>",
            "{tr}smothtext reply this command to text message",
        ],
        "examples": "{tr}smothtext Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smothtextcharacter = fonts.smothtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smothtextcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="egyptf(?:\s|$)([\s\S]*)",
    command=("egyptf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}egyptf <text>", "{tr}egyptf reply this command to text message"],
        "examples": "{tr}egyptf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            egyptfontcharacter = fonts.egyptfontfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, egyptfontcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="maref(?:\s|$)([\s\S]*)",
    command=("maref", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}maref <text>", "{tr}maref reply this command to text message"],
        "examples": "{tr}maref Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            nightmarecharacter = fonts.nightmarefont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, nightmarecharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="handcf(?:\s|$)([\s\S]*)",
    command=("handcf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}handcf <text>", "{tr}handcf reply this command to text message"],
        "examples": "{tr}handcf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwcapitalcharacter = fonts.hwcapitalfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="doublef(?:\s|$)([\s\S]*)",
    command=("doublef", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": [
            "{tr}doublef <text>",
            "{tr}doublef reply this command to text message",
        ],
        "examples": "{tr}doublef Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            doubletextcharacter = fonts.doubletextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="mock(?:\s|$)([\s\S]*)",
    command=("mock", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}mock <text>", "{tr}mock reply this command to text message"],
        "examples": "{tr}mock Arankuserbot",
    },
)
async def spongemocktext(mock):
    "Changes font style of the given text"
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(mock, "`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and random.randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await edit_or_reply(mock, "".join(reply_text))


@Arankub.Arank_cmd(
    pattern="ghostf(?:\s|$)([\s\S]*)",
    command=("ghostf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}ghostf <text>", "{tr}ghostf reply this command to text message"],
        "examples": "{tr}ghostf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            ghostfontcharacter = fonts.ghostfontfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, ghostfontcharacter)
    await edit_or_reply(event, string)


@Arankub.Arank_cmd(
    pattern="handsf(?:\s|$)([\s\S]*)",
    command=("handsf", plugin_Arankegory),
    info={
        "header": "Font style command.(Changes font style of the given text)",
        "usage": ["{tr}handsf <text>", "{tr}handsf reply this command to text message"],
        "examples": "{tr}handsf Arankuserbot",
    },
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwslcharacter = fonts.hwslfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, hwslcharacter)
    await edit_or_reply(event, string)
