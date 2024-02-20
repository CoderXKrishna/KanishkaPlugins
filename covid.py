# corona virus stats for Arankuserbot
from userbot.plugins import Arankub, covidindia, edit_delete, edit_or_reply

from covid import Covid

plugin_Arankegory = "extra"


@Arankub.Arank_cmd(
    pattern="covid(?:\s|$)([\s\S]*)",
    command=("covid", plugin_Arankegory),
    info={
        "header": "To get latest information about covid-19.",
        "description": "Get information about covid-19 data in the given country/state(only Indian States).",
        "usage": "{tr}covid <state_name/country_name>",
        "examples": ["{tr}covid andhra pradesh", "{tr}covid india", "{tr}covid world"],
    },
)
async def corona(event):
    "To get latest information about covid-19."
    input_str = event.pattern_match.group(1)
    country = (input_str).title() if input_str else "World"
    Arankevent = await edit_or_reply(event, "`Collecting data...`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️ Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔 Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️ Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕 Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊 Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉 Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺 New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟 New Deaths : <code>{country_data['new_deaths']}</code>"
        await Arankevent.edit(
            f"<b>Corona Virus Info of {country}:\n{data}</b>", parse_mode="html"
        )
    else:
        data = await covidindia(country)
        if data:
            Arank1 = int(data["new_positive"]) - int(data["positive"])
            Arank2 = int(data["new_death"]) - int(data["death"])
            Arank3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️ Confirmed   : <code>{data['new_positive']}</code>\
                \n😔 Active           : <code>{data['new_active']}</code>\
                \n⚰️ Deaths         : <code>{data['new_death']}</code>\
                \n😊 Recovered   : <code>{data['new_cured']}</code>\
                \n🥺 New Cases   : <code>{Arank1}</code>\
                \n😟 New Deaths : <code>{Arank2}</code>\
                \n😃 New cured  : <code>{Arank3}</code> </b>"
            await Arankevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                Arankevent,
                f"`Corona Virus Info of {country} is not avaiable or unable to fetch`",
                5,
            )
