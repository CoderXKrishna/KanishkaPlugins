import asyncio
import json
import random

import requests
from userbot import Arankub
from userbot.core.managers import edit_delete, edit_or_reply
from userbot.helpers.utils import reply_id

plugin_Arankegory = "fun"

game_code = ["ttt", "ttf", "ex", "cf", "rps", "rpsls", "rr", "c", "pc"]
game_name = [
    "Tic-Tac-Toe",
    "Tic-Tac-Four",
    "Elephant XO",
    "Connect Four",
    "Rock-Paper-Scissors",
    "Rock-Paper-Scissors-Lizard-Spock",
    "Russian Roulette",
    "Checkers",
    "Pool Checkers",
]

game = dict(zip(game_code, game_name))
Arankegory = ["classic", "kids", "party", "hot", "mixed"]


async def get_task(mode, choice):
    url = "https://psyArankgames.com/api/tod-v2/"
    data = {
        "id": "truth-or-dare",
        "language": "en",
        "Arankegory": Arankegory[choice],
        "type": mode,
    }
    headers = {
        "referer": "https://psyArankgames.com/app/truth-or-dare/?utm_campaign=tod_website&utm_source=tod_en&utm_medium=website"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()["results"]
    return random.choice(result)


@Arankub.Arank_cmd(
    pattern="(task|truth|dare)(?: |$)([1-5]+)?$",
    command=("task", plugin_Arankegory),
    info={
        "header": "Get a random truth or dare task.",
        "description": "if no input is given then task will be from classic or kids Arankegory. if you want specific Arankegory then give input.",
        "note": "U need to give input as 1 for classic , 2 for kids , 3 for party , 4 for hot and 5 for mixed. if you want to give multiple Arankgories then use numbers without space like 12",
        "example": [
            "{tr}task",
            "{tr}task 2",
            "{tr}task 123",
        ],
    },
)
async def truth_dare_task(event):
    "Get a random task either truth or dare."
    taskmode = event.pattern_match.group(1)
    if taskmode == "task":
        Arankevent = await edit_or_reply(event, "Getting a random task for you.....")
        taskmode = random.choice(["truth", "dare"])
    else:
        Arankevent = await edit_or_reply(
            event, f"Getting a random {taskmode} task for you....."
        )
    Arankegory = event.pattern_match.group(2)
    Arankegory = int(random.choice(Arankegory)) if Arankegory else random.choice([1, 2])
    try:
        task = await get_task(taskmode, Arankegory)
        if taskmode == "truth":
            await Arankevent.edit(f"**The truth task for you is**\n`{task}`")
        else:
            await Arankevent.edit(f"**The dare task for you is**\n`{task}`")
    except Exception as e:
        await edit_delete(Arankevent, f"**Error while getting task**\n`{e}`", 7)


@Arankub.Arank_cmd(
    command=("truth", plugin_Arankegory),
    info={
        "header": "Get a random truth task.",
        "description": "if no input is given then task will be from classic or kids Arankegory. if you want specific Arankegory then give input.",
        "note": "U need to give input as 1 for classic , 2 for kids , 3 for party , 4 for hot and 5 for mixed. if you want to give multiple Arankgories then use numbers without space like 12",
        "example": [
            "{tr}truth",
            "{tr}truth 2",
            "{tr}truth 123",
        ],
    },
)
async def truth_task(event):
    "Get a random truth task."
    # just to show in help menu as seperate


@Arankub.Arank_cmd(
    command=("dare", plugin_Arankegory),
    info={
        "header": "Get a random dare task.",
        "description": "if no input is given then task will be from classic or kids Arankegory. if you want specific Arankegory then give input.",
        "note": "U need to give input as 1 for classic , 2 for kids , 3 for party , 4 for hot and 5 for mixed. if you want to give multiple Arankgories then use numbers without space like 12",
        "example": [
            "{tr}dare",
            "{tr}dare 2",
            "{tr}dare 123",
        ],
    },
)
async def dare_task(event):
    "Get a random dare task."
    # just to show in help menu as seperate


@Arankub.Arank_cmd(
    pattern="game(?:\s|$)([\s\S]*)",
    command=("game", plugin_Arankegory),
    info={
        "header": "Play inline games",
        "description": "Start an inline game by inlinegamebot",
        "Game code & Name": game,
        "usage": "{tr}game <game code>",
        "examples": "{tr}game ttt ",
    },
)
async def igame(event):
    "Fun game by inline"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    game_list = "".join(
        f"**{i}.** `{item}` :- __{game[item]}__\n"
        for i, item in enumerate(game, start=1)
    )
    if not input_str:
        await edit_delete(
            event, f"**Available Game Codes & Names :-**\n\n{game_list}", time=60
        )
        return
    if input_str not in game_code:
        Arankevent = await edit_or_reply(event, "`Give me a correct game code...`")
        await asyncio.sleep(1)
        await edit_delete(
            Arankevent, f"**Available Game Codes & Names :-**\n\n{game_list}", time=60
        )
    else:
        await edit_or_reply(
            event,
            f"**Game code `{input_str}` is selected for game:-** __{game[input_str]}__",
        )
        await asyncio.sleep(1)
        bot = "@inlinegamesbot"
        results = await event.client.inline_query(bot, input_str)
        await results[game_code.index(input_str)].click(
            event.chat_id, reply_to=reply_to_id
        )
        await event.delete()
