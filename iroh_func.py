import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc, os, re
from discord.ext import tasks
from dateutil import tz

asia = tz.gettz('Asia/Singapore')

help = """
Hello, I am General Iroh. You may also know me as the Dragon of the West. No? It's more of demonstration really. 
But this is not why I am here for. I am a utility tool for you. Here I have many functions like quoting all my Avatar quotes, set a timer, and rolling dices.

To use the Pomodoro timer, you should use the `!roh timer` command. By default, `!roh timer` will only give you 15 minutes.
However, you can make your own timer from 0 to 99 mintues using command like this:
`!timer start 40` for 40 minutes timer.\n
When the timer is up, it will nudge you every 5 seconds. To stop that, just reply `!done` and it will stop.
Furthermore, you can use `!stop` command to stop the timer in the middle of countdown, and timer will be reset.

If you like to brighten up your day with a quote, you may use the `!iroh` command. I will reply you a random quote from the Avatar show. 

If you have interest in dice rolling, you can use my `!roll` command too! 
However to roll a dice, you need to mention numbers of dice, and numbers of sides on the dice. 
Let me show you:
`!roll 1d10` will generate one random number between 1 to 10.
`!roll 3d10` will generate three random numbers between 1 to 10, and will also show you the sum of the three dices added up.

There will be more functions to be added as my maker is gathering idea for me. So I hope you found some of my functions helpful!

When I'm not doing any task mentioned, I'll go make myself some tea...would you like one? 
Sharing tea with a fascinating stranger is one of life's true delights. :tea:
"""


myEmbed = discord.Embed(title="!roh command guide", description=help, color=0x00ff00)

async def vegan_day(client, lunar, now):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today is month {lunar.month} and day {lunar.day}. It\'s vegan day!\nGregorian date is month {now.month}, and day {now.day}.')

async def other_day(client, lunar, now):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today lunar date is month {lunar.month}, and day {lunar.day}.\nGregorian date is month {now.month}, and day {now.day}.')

@tasks.loop(minutes=1)
async def isLunar(client):
    now = dt.datetime.now(tz=asia)
    lunar = lc.Converter.Solar2Lunar(now)
    if(lunar.day in [1,15] and now.hour == 0 and now.minute == 1): 
        await vegan_day(client, lunar, now)
    elif(now.hour == 0 and now.minute == 0):
        await other_day(client, lunar, now)