import discord
import asyncio
from datetime import datetime

i=0

client = discord.Client()

token = ''

async def avach():
    pfp_path = f"{i}.jpg"
    with open(pfp_path, "rb") as pfp:
        await client.user.edit(password=None, avatar=pfp.read())
    print("profile picture changed")
    

@client.event
async def on_ready():
    while True:
        global i
        now = datetime.now().time()
        if "21:15" in str(now):
            i=2
            asyncio.run_coroutine_threadsafe(avach(), client.loop)
        await asyncio.sleep(300)


client.run(token)
