import discord
from discord.ext.commands import bot
from discord.ext import commands

Client = discord.Client()
bot_prefix = ">"
client = commands.Bot(command_prefix=bot_prefix)

#Returns the bot's messages
def is_bot(m):
    return m.author == client.user

#Basic Startup
@client.event
async def on_ready():
    print("VuchiBot v0.01")
    print("Latest Edit 6/30/2017")
    print("Created by Alex Vucicevich")


#PingPong Command
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

#Purge Commands
@client.event
async def on_message(message):
    if message.content.startswith(">Purge"):
        await client.purge_from(message.channel, limit=100)
        print(message.channel)
    elif message.content.startswith(">Clear"):
        async for msg in client.logs_from(message.channel):
            if message.content.startswith(">Clear bot"):
                await client.purge_from(message.channel, limit=100, check=is_bot)
            elif message.content.startswith(">Clear user"):
                if msg.content.startswith(">"):
                    await client.delete_message(msg)
            else:
                pass
    else:
        await client.process_commands(message)
            
client.run("MzMwNDk2OTIxNjk5MzUyNTc3.DDh6Pw.U7vi0euhXlP7HvB4_DVkwoYTC9o")

##TODO Tomorrow:
##Add web grabbing software
##Grabs information regarding stocks and spits out link
