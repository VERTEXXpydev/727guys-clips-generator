import requests
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")

def api_request(endpoint: str, parameters: dict):
    return requests.get(f'https://osu.ppy.sh/api/{endpoint}', params=parameters).json()

async def log(text):
    return requests.get('https://canary.discord.com/api/webhooks/940606033750024193/Xem3TJaZ1DlBfaI4aFLV3hDSvG2x4eh9kRxH9xK7rL_ahydzBjPqafq41KoZO1u3u5oS', params={"content": text}).json()

def disp(text):
    print(text)
    log(text)

@bot.event
async def on_ready():
    disp("Ready.")

bot.run(TOKEN)