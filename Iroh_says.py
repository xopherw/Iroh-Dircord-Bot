import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc
from discord.ext import tasks

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()

while(True):
    try: 
        client = discord.Client()

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            
            if message.content == '!roh':
                response = random.choice(iroh_quotes)
                await message.channel.send(response)

        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')
            await isLunar.start()
        

        async def vegan_day(lunar):
            await client.wait_until_ready()
            channel = await client.fetch_user(int("YOUR_ID_WITHOUT_QUOTATION_MARK"))
            await channel.send(f'Today is month {lunar.month} and day {lunar.day}. It\'s vegan day!')
        
        async def other_day(lunar):
            await client.wait_until_ready()
            channel = await client.fetch_user(int("YOUR_ID_WITHOUT_QUOTATION_MARK"))
            await channel.send(f'Today lunar date is month {lunar.month}, and day {lunar.day}.')

        @tasks.loop(minutes=1)
        async def isLunar():
            now = dt.datetime.now()
            lunar = lc.Converter.Solar2Lunar(now)
            if(lunar.day in [1,15] and now.hour == 0 and now.minute == 1): 
                await vegan_day(lunar)
            elif(now.hour == 0 and now.minute == 0):
                await other_day(lunar)

        client.run('YOUR_TOKEN')

    except TimeoutError:
        print("Reconnecting, please hold...")
        time.sleep(5)
    
