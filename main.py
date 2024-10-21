import discord as dc
from discord.ext import commands
import csv

intents = dc.Intents.default()
intents.message_content = True
bot = dc.Client(intents=intents)




with open('token.csv', 'r') as csvfile:  # this will close the file automatically.
    reader = csv.reader(csvfile)
    row = next(reader) 
    token = str(row[1]).strip() if row[0]=="token" else exit(1)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    
    target_messages = ["mňau"]
    message_to_send = f"BAD <@{message.author.id}>!!!\n"+f"https://tenor.com/view/andrew-tate-stare-andrew-tate-andrew-tate-sigma-xafer-gif-10165002945664617941"
    
    for target in target_messages:
        if target in message.content and message.author != bot.user:
            await message.delete()
            await message.channel.send(message_to_send)

bot.run(token)


