import requests
from userbot import Arankub
from userbot.core.managers import edit_or_reply

plugin_Arankegory = "fun"


@Arankub.Arank_cmd(
    pattern="tArank$",
    command=("tArank", plugin_Arankegory),
    info={
        "header": "Some random Arank facial text art",
        "usage": "{tr}tArank",
    },
)
async def hmm(Arank):
    "Some random Arank facial text art"
    reactArank = requests.get("https://nekos.life/api/v2/Arank").json()
    await edit_or_reply(Arank, reactArank["Arank"])


@Arankub.Arank_cmd(
    pattern="why$",
    command=("why", plugin_Arankegory),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(Arank):
    "Some random Funny questions"
    whyArank = requests.get("https://nekos.life/api/v2/why").json()
    await edit_or_reply(Arank, whyArank["why"])


@Arankub.Arank_cmd(
    pattern="fact$",
    command=("fact", plugin_Arankegory),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(Arank):
    "Some random facts"
    factArank = requests.get("https://nekos.life/api/v2/fact").json()
    await edit_or_reply(Arank, factArank["fact"])
