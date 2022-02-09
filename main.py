import requests
import json
import discord
from discord.ext import commands
from ossapi import *
api = OssapiV2("12634", "gF0jEtyf8SYYkIS1wdV1Kj5Ym1MYkoxTJarQKtRS")

from map_downloader import download_beatmap

bot = commands.Bot(command_prefix=".")
TOKEN = open("token.txt", "r").read()
bot.remove_command("help")

def api_request(endpoint: str, parameters: dict):
    return requests.get(f'https://osu.ppy.sh/api/{endpoint}', params=parameters).json()

async def get_beatmap(name):
    name = name.replace("_", " ")
    beatmapset = api.search_beatmapsets(query=name).beatmapsets[0]
    id = beatmapset.id
    title = beatmapset.artist + " - " + beatmapset.title
    return [id, title]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Laffey suck dicks"))
    print("[BOT] Logged into Discord Gateway, starting to look for replays...")

@bot.event
async def on_message(message):
    if message.channel.id == 930823120087023696:
        if str(message.attachments) == "[]": # Checks if there is an attachment on the message
            return
        else: # if there is it gets the filename from message.attachments
            split_v1 = str(message.attachments).split("filename='")[1]
            filename = str(split_v1).split("' ")[0]
            if filename.endswith(".osr"): # checks if it is a .osr file
                await message.attachments[0].save(fp="replays/{}".format(filename)) # saves the file
                beatmap = await get_beatmap(filename)
                beatmapsetid = beatmap[0]
                beatmapsettitle = beatmap[1]
                await download_beatmap(beatmapsetid, "beatmaps/" + beatmapsettitle + ".zip")


bot.run(TOKEN)