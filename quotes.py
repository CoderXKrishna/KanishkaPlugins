# inspired from uniborg Quotes plugin
import random

from userbot import Arankub
from userbot.core.logger import logging
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers import Arankmemes
from userbot.helpers.functions import random_quote, search_quotes
from userbot.helpers.utils import parse_pre

LOGS = logging.getLogger(__name__)
plugin_Arankegory = "extra"


@Arankub.Arank_cmd(
    pattern="quote(?:\s|$)([\s\S]*)",
    command=("quote", plugin_Arankegory),
    info={
        "header": "To get random quotes on given topic.",
        "description": "An api that Fetchs random Quote from `goodreads.com`",
        "usage": "{tr}quote <topic>",
        "examples": "{tr}quote love",
    },
)
async def quote_search(event):
    "shows random quotes on given topic."
    input_str = event.pattern_match.group(1)
    try:
        response = await search_quotes(input_str) if input_str else await random_quote()
    except Exception:
        return await edit_delete(event, "`Sorry Zero results found`", 5)
    await edit_or_reply(event, response, parse_mode=parse_pre)


@Arankub.Arank_cmd(
    pattern="pquote$",
    command=("pquote", plugin_Arankegory),
    info={
        "header": "To get random quotes on programming.",
        "usage": "{tr}pquote",
    },
)
async def _(event):
    "Shows random programming quotes"
    txt = random.choice(Arankmemes.PROGQUOTES)
    await edit_or_reply(event, txt)
