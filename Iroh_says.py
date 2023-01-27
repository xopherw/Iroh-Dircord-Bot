from iroh_func import *
from timer_func import *
import token

path = pathlib.Path('iroh.csv')
iroh_quotes = pd.read_csv(path,header=None,sep='\n')[0].to_list()
asia = tz.gettz('Asia/Singapore')

open('user.json','w').write('{"dummy" : "dummy" }')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user: return

    # Iroh quotes
    if message.content == '!roh':
        response = random.choice(iroh_quotes)
        await message.channel.send(response)
    
    # Iroh rolls dice
    if (re.match(r"^(\!roll) [0-9]{1,3}d[0-9]{1,3}(\s(\+|\-)[0-9]{1,2})?$", message.content)):
        rollnum = len([i for i in message.content.split(' ')])
        roll = [int(i) for i in list(itertools.chain.from_iterable([i.split('d') for i in message.content.split(' ')][1:]))] if(rollnum == 3) else [int(i) for i in message.content.split(' ')[-1].split('d')] 
        await rolling(message, roll)

    # Iroh start default timer
    if (re.match(r"^(\!roh timer)$", message.content)):
        await userCheck(client, 15, message)    
    
    # Iroh start customed timer
    elif(re.match(r"^(\!roh timer) [0-9]{1,2}$", message.content)):
        period = int(message.content.split(' ')[-1])
        await userCheck(client, period, message)
    
    # Iroh help on commands
    elif(message.content == "!roh help"): await message.author.send(embed=myEmbed)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # Lunar Teller
    activity = discord.Game(name="'!roh help' for info")
    await client.change_presence(activity=activity)
    await isLunar.start(client)

while(True):
    # try: client.loop.run_until_complete(client.run(os.getenv('TOKEN')))
    try: client.loop.run_until_complete(client.run(token.api()))
    except Exception:
        print("Reconnecting, please hold...")
        time.sleep(5)
