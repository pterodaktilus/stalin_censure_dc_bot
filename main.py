import discord as dc
from discord.ext import commands
import csv

intents = dc.Intents.default()
intents.message_content = True
bot = dc.Client(intents=intents)
token = csv.get_token()
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if "mňau" in message.content and message.author != bot.user:
        await message.delete()
        await message.channel.send(f"BAD <@{message.author.id}>!!!\n"+f"https://tenor.com/view/andrew-tate-stare-andrew-tate-andrew-tate-sigma-xafer-gif-10165002945664617941")

bot.run(token)


