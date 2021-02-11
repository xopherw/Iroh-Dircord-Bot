import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc, os, re
from discord.ext import tasks
from dateutil import tz

asia = tz.gettz('Asia/Singapore')


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