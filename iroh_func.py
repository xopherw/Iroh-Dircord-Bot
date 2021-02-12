import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc, os, re
from discord.ext import tasks
from dateutil import tz

asia = tz.gettz('Asia/Singapore')

help = """
Hello, I am General Iroh. You may also know me as the Dragon of the West. 
No? It's more of demonstration really. But this is not why I am here for. 
I am here to help you like how I helped my favorite nephew Zuko.


**"!roh" command: **
This command will return a random quote I have said from the Avatar show.


**"!roh timer" command: **
By default, `!roh timer` will only give you 15 minutes.

However, you can make your own timer from 0 to 99 mintues using command like this:
`!roh timer 40` for 40 minutes timer.

When the timer is up, I will nudge you (in personal message) every 5 seconds. Just reply `!done` and it will stop. 

You can also use `!stop` command to stop the timer in the middle of countdown, and timer will be reset.


**"!roll [number X]d[number Y]" command: **
This command will roll a dice for any RPG event or you lost your dice in your board game.

Let me show you how to use the command:

`!roll 1d10` will generate one random number between 1 to 10
returns: `@username rolls 1d10 and gets 11.`

`!roll 3d10` will generate three random numbers between 1 to 10, and will also retrun the sum of the three dices numbers.
returns: `@username rolls 3d20 and gets 24. [4, 10, 10]`


**More: **
There will be more functions to be added as my maker is gathering new idea for me. 
So I hope you found some of my functions helpful!

When I'm not doing any task, I'll go make myself some tea...would you like one? Sharing tea with a fascinating stranger is one of life's true delights. :tea:
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
    else:
        await other_day(client, lunar, now)

async def rolling(message, roll):
    result = [random.randint(1,roll[-1]) for i in range(roll[0])]
    id = message.author.id
    msg1 = f"<@{id}> rolls {roll[0]}d{roll[-1]} and gets {sum(result)}."
    msg2 = f"<@{id}> rolls {roll[0]}d{roll[-1]} and gets {sum(result)}. " + f"{result if(len(result) > 1) else ''}"
    return await message.channel.send(f"{ msg1 if(len(msg2) > 2000) else  msg2 } ")