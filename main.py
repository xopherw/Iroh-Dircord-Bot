from iroh_func import *
# from timer_func import *
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('token')
intents = discord.Intents.default()
intents.message_content = True

iroh_quotes = open('iroh.csv', 'r').read().split('\n')
asia = tz.gettz('Asia/Singapore')

client = discord.Client(intents=intents)

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
    
    # # Iroh start customed timer
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
    try: client.run(token)
    except Exception as e:
        print("Reconnecting, please hold...")
        print(e)
        time.sleep(5)