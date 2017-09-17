import discord
from discord.ext.commands import bot
from discord.ext import commands

from google import search

Client = discord.Client()
bot_prefix = ">"
client = commands.Bot(command_prefix=bot_prefix)

#Returns the bot's messages
def is_bot(message):
    return message.author == client.user

#Basic Startup
@client.event
async def on_ready():
    print("VuchiBot v0.02")
    print("Latest Edit 7/1/2017")
    print("Created by Alex Vucicevich")
  
#PingPong Command
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

#Shoghi Command
@client.command(pass_context=True)
async def sex(ctx):
    await client.say("8===D~ ( | )o.o")

#Stock Link Commands
@client.command(pass_context=True)
async def stockinfo(ctx, info):
    info = str(info)
    query = "Stock " + info
    for url in search(query, tld="com", lang = "en", stop = 1):
        await client.say(url)

#Stock Charts Via Google Finance
@client.command(pass_context=True)
async def stockchart(ctx, exchange, ticker):
    exchange = str(exchange)
    ticker = str(ticker)
    await client.say("https://www.google.com/finance?q=" + exchange + "%3A" + ticker)

#Event commands
@client.event
async def on_message(message):
    #Purge
    if message.content.startswith(">purge"):
        await client.purge_from(message.channel, limit=100)

    #Clear Commands
    elif message.content.startswith(">clear"):
        async for msg in client.logs_from(message.channel):
            if message.content.startswith(">clear bot"):
                await client.purge_from(message.channel, limit=100, check=is_bot)
            elif message.content.startswith(">clear user"):
                if msg.content.startswith(">"):
                    await client.delete_message(msg)
            else:
                pass

    #Help command
    elif message.content.startswith(">help"):
        with open('help.txt', 'r') as myfile:
            data = myfile.read()
        await client.send_message(message.author, data)

    #Commands
    else:
        await client.process_commands(message)
            
client.run("MzMwNDk2OTIxNjk5MzUyNTc3.DDh6Pw.U7vi0euhXlP7HvB4_DVkwoYTC9o")


