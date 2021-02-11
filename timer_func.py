from iroh_func import *
import json, asyncio

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