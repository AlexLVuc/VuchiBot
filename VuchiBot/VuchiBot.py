import discord
import json
import datetime
import time
import asyncio

from discord.ext.commands import bot
from discord.ext import commands

from googlefinance import getQuotes
from google import search

Client = discord.Client()

bot_prefix = ">"
client = commands.Bot(command_prefix=bot_prefix)


#Returns the bot's messages
def is_bot(message):
    return message.author == client.user


#Async Waiting Times
async def timeToWait(timeset, startup):
    if(startup == False):
        if(timeset == "hour"):
            await asyncio.sleep(3600)
        if(timeset == "halfhour"):
            await asyncio.sleep(1800)
        if(timeset == "quarterhour"):
            await asyncio.sleep(900)
        if(timeset == "test"):
            await asyncio.sleep(5)
    else:
        if(timeset == "hour"):
            while(datetime.datetime.now().minute != 0):
                pass
        if(timeset == "halfhour"):
            while(datetime.datetime.now().minute%30 != 0):
                pass
        if(timeset == "quarterhour"):
            while(datetime.datetime.now().minute%15 != 0):
                pass
        if(timeset == "test"):
            while(datetime.datetime.now().second%30 != 0):
                pass


#Stocktracking loop
async def stockTracker(ticker: str, trade: str, timeset: str):
    await client.wait_until_ready()
    channel = discord.Object(id='330503480492163072')

    await timeToWait(timeset, True)
    
    while not client.is_closed:
        if(datetime.datetime.now().hour >= 20 or datetime.datetime.now().hour <= 8):
            await client.send_message(channel, "The markets are currently closed. This bot will not post information until the next opening.")
            await timeToWait(timeset, False)
        else:
            await client.send_message(channel, json.dumps(getQuotes(trade + ':' + ticker), indent=2))
            await timeToWait(timeset, False )

#Basic Startup
@client.event
async def on_ready():
    print("VuchiBot v0.05")
    print("Latest Edit 7/2/2017")
    print("Created by Alex Vucicevich")
    print(datetime.datetime.now())


#PingPong Command
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True)
async def count(ctx):
    num = 2
    channel = discord.Object(id='330503480492163072')

    while True:
        await client.send_message(channel, num)
        await asyncio.sleep(1)
        num = num - 1

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


#Autoposts information at given times
@stockinfo.command()
async def autopost(ticker: str, trade:str, timeset:str):
    client.loop.create_task(stockTracker(ticker, trade, timeset))

##Autoposts off
##@stockinfo.command()
##async def autopoststop(ticker: str, trade:str):
##    client.loop.close(stockTracker(ticker, trade))


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


