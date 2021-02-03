import discord,random, pathlib, pandas as pd, time, datetime as dt, lunarcalendar as lc
from discord.ext import commands, tasks

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()

while(True):
    try: 
        client = discord.Client()
        bot = commands.Bot(command_prefix='!')

        @bot.command(name='iroh_says')
        async def iroh_says(ctx):
            response = random.choice(iroh_quotes)
            await ctx.send(response)

        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')
            # await job.start()
            while(True):
                interval = 1
                now = dt.datetime.now()
                lunar = lc.Converter.Solar2Lunar(now)
                if(lunar.day in [1,15] and now.hour == 0 and now.minute == 0): 
                    await vegan_day(lunar)
                    interval = 2 * 60
                elif(now.hour == 0 and now.minute == 0):
                    await other_day(lunar)
                    interval = 2 * 60
                time.sleep(interval)

        async def vegan_day(lunar):
            await client.wait_until_ready()
            channel = await client.fetch_user(int('YOUR_USER_ID_WITHOUT_QUOTATION_MARK'))
            await channel.send(f'Today is month {lunar.month} and day {lunar.day}. It\'s vegan day!')
        
        async def other_day(lunar):
            await client.wait_until_ready()
            channel = await client.fetch_user(int(266031018295689226))
            await channel.send(f'Today lunar date is month {lunar.month}, and day {lunar.day}.')

        client.run('YOUR_TOKEN')

    except TimeoutError:
        print("Reconnecting, please hold...")
        time.sleep(5)
    
