import discord,random, pathlib
import pandas as pd
from discord.ext import commands

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()


client = discord.Client()
bot = commands.Bot(command_prefix='!')

@bot.command(name='iroh_says')
async def iroh_says(ctx):
    response = random.choice(iroh_quotes)
    await ctx.send(response)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

bot.run("YOU_TOKEN")
