import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc, asyncio, os
from discord.ext import tasks
from dateutil import tz

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()
asia = tz.gettz('Asia/Singapore')

client = discord.Client()

async def vegan_day(lunar, now):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today is month {lunar.month} and day {lunar.day}. It\'s vegan day!\nGregorian date is month {now.month}, and day {now.day}.')

async def other_day(lunar, now):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today lunar date is month {lunar.month}, and day {lunar.day}.\nGregorian date is month {now.month}, and day {now.day}.')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content == '!roh':
        response = random.choice(iroh_quotes)
        await message.channel.send(response)
        print(dt.datetime.now(tz=asia).time())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await isLunar.start()

@tasks.loop(minutes=1)
async def isLunar():
    now = dt.datetime.now()
    lunar = lc.Converter.Solar2Lunar(now)
    if(lunar.day in [1,15] and now.hour == 0 and now.minute == 1): 
        await vegan_day(lunar, now)
    elif(now.hour == 0 and now.minute == 0):
        await other_day(lunar, now)
        
while(True):
    try: client.loop.run_until_complete(client.run(os.getenv('TOKEN')))
    except Exception:
        print("Reconnecting, please hold...")
        time.sleep(5)
