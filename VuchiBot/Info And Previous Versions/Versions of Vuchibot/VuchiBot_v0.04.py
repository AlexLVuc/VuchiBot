import discord
from discord.ext.commands import bot
from discord.ext import commands
from googlefinance import getQuotes
import json
import datetime
from google import search

Client = discord.Client()
bot_prefix = ">"
client = commands.Bot(command_prefix=bot_prefix)

now = datetime.datetime.now()

#Returns the bot's messages
def is_bot(message):
    return message.author == client.user

#Basic Startup
@client.event
async def on_ready():
    print("VuchiBot v0.03")
    print("Latest Edit 7/2/2017")
    print("Created by Alex Vucicevich")
    print(now)
  
#PingPong Command
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

#Stock Link Commands
@client.command(pass_context=True)
async def stocklinks(ctx, info: str):
    query = "Stock " + info
    for url in search(query, tld="com", lang = "en", stop = 1):
        await client.say(url)

##Stock Info Grouping##
#Original Stock Info Command
@client.group(pass_context=True)
async def stockinfo(ctx):
    if ctx.invoked_subcommand is None:
        await client.say("Refer to >help for stockinfo command info.")

#Takes only ticker
@stockinfo.command()
async def default(ticker: str):
    await client.say(json.dumps(getQuotes(ticker), indent=2))

#Takes ticker and exchange
@stockinfo.command()
async def exchange(ticker: str, trade: str):
    await client.say(json.dumps(getQuotes(trade + ':' + ticker), indent=2))

##@stockinfo.command()
##async def autopost(ticker: str, trade:str):
##    await client.say(content = json.dumps(getQuotes(trade + ':' + ticker), indent=2), 1000)
##
    
#Stock Charts Via Google Finance
@client.command(pass_context=True)
async def stockchart(ctx, exchange: str, ticker: str):

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


