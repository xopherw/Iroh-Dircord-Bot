from iroh_func import *
import json, asyncio

#----------- constants -----------#

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

#----------- async defs -----------#

# Perform a user check to prevent double timer set. If no existing user, continue to "async def timer"
async def userCheck(client, period, message):
    if(json.loads(open('user.json' , 'r').read()).get(str(message.author.id)) != None): 
        await sender(message, "Only one timer is allowed. Stop & reset if necessary.")  
    else:
        await sender(message, f"{period} minutes set! Focus on your element bend!" if(period != 15) else "No time set, default timer is 15 minutes! Focus on your element bend!") 
        await timer(client, period, message) 

# Does the countdown work as well as remove user once "stop" command is used, or "done" command when time is up.
async def timer(client, period, message):
    try:
        temp_data = json.loads(open('user.json' , 'r').read())
        temp_data.update(json.loads(assigner(message.author.id)))
        open('user.json', 'w').write(json.dumps(temp_data))
        def stop(m): return m.content == '!stop' and m.author.id == message.author.id
        await waiter(client, period * 60, stop)
        await sender(message, "Timer is stopped and reset.")
        removeID(message.author.id) 

    except asyncio.TimeoutError:
        while(True):
            try: 
                await sender(message, 'Times Up!!!')
                def done(m): return m.content == '!done' and m.author.id == message.author.id
                await waiter(client, 5, done)
                await sender(message, 'Looks like you\'ve completed your training! Go reward yourself a nice warm tea.')
                removeID(message.author.id)
                break
            except asyncio.TimeoutError:
                pass

#----------- normal defs -----------#

def assigner(id):
    return json.dumps( { id : str(dt.datetime.now())} )

def sender(message, string):
    return message.author.send(string)

def waiter(client, timeout, check):
    return client.wait_for('message', timeout=timeout, check=check)

def removeID(id):
    try:
        temp_data = json.loads(open('user.json' , 'r').read())
        temp_data.pop(str(id))
        open('user.json', 'w').write(json.dumps(temp_data))
    except:
        pass