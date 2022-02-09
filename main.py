import requests
import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")
TOKEN = open("token.txt", "r").read()
bot.remove_command("help")

def api_request(endpoint: str, parameters: dict):
    return requests.get(f'https://osu.ppy.sh/api/{endpoint}', params=parameters).json()

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
            if filename.endswith(".osr"): # hecks if it is a .osr file
                await message.attachments[0].save(fp="replays/{}".format(filename)) # saves the file


bot.run(TOKEN)