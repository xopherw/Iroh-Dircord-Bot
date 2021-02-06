import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc, asyncio
from discord.ext import tasks

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()

client = discord.Client()

async def vegan_day(lunar):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today is month {lunar.month} and day {lunar.day}. It\'s vegan day!')

async def other_day(lunar):
    await client.wait_until_ready()
    channel = await client.fetch_user(int(266031018295689226))
    await channel.send(f'Today lunar date is month {lunar.month}, and day {lunar.day}.')

@client.event
async def on_message(message):
    if message.author == client.user: return

    if message.content == '!roh':
        response = random.choice(iroh_quotes)
        await message.channel.send(response)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await isLunar.start()

@tasks.loop(minutes=1)
async def isLunar():
    now = dt.datetime.now()
    lunar = lc.Converter.Solar2Lunar(now)
    if(lunar.day in [1,15] and now.hour == 0 and now.minute == 1): 
        await vegan_day(lunar)
    elif(now.hour == 0 and now.minute == 0):
        await other_day(lunar)

while(True):
    try: client.loop.run_until_complete(client.run('NzkzNjY4NzI2Nzk1OTI3NTcy.X-vnmg.-RCiG0VznvxtU8KpoGjNN_TvKm4'))
    except Exception:
        print("Reconnecting, please hold...")
        time.sleep(5)
