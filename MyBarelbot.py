import discord;
import logging
import time
import os
from datetime import datetime, timedelta
import threading
from threading import Timer
import urllib.request, json
from random import randint

from discord.ext import commands

logging.basicConfig(level=logging.INFO)




animeLinkList =[]
thiccLinkList = []
thighsLinkList = []
client = commands.Bot(description='BarelLord bot', command_prefix='!')


@client.event
async def on_ready():
    scrapeAnimeSubreddit()
    scrapeThiccSubreddit()
    scrapeThighsSubreddit()


@client.event
async def on_message(message):
    if "rozentals" in message.content.lower():
        await client.send_message(message.channel, '"musu carrys"')
    if "olafs" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņš...')
    elif "olafu" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņu...')
    elif "olaf" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņ...')
    elif "olafam" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņam...')
    elif "olafa" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņa...')
    elif "olafā" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņā...')
    elif "olafi" in message.content.lower():
        await client.send_message(message.channel, '*Pūciņi...')

    await client.process_commands(message)


@client.command(pass_context=True)
async def helpMe(ctx):
    embed = discord.Embed(title="BarelLord Documentation", description="--All BarelLord available commands--",
                          color=0x800080)
    embed.add_field(name="!gg [Username(EUNE)]", value="--Gives op.gg link with specified summoner name", inline=False)
    embed.add_field(name="!cc [champion]", value="--Gives champion counter link", inline=False)
    embed.add_field(name="!live [username(EUNE)]", value="--Gives op.gg live game page", inline=False)
    embed.add_field(name="!ggc [champion, lane]", value="--Gives op.gg page with specified champion and lane",
                    inline=False)
    embed.add_field(name="!thiccthighs", value="--Umm yea I guess nothing more to explain :rolling_eyes: ",
                    inline=False)
    embed.add_field(name="!animethighs", value="--Just make sure FBI isn't around the corner", inline=False)
    embed.add_field(name="!thighs", value="--Tons of fun :thinking: ", inline=False)
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def gg(ctx, username: str):
    print(ctx.message.channel == "text")
    await client.send_message(ctx.message.channel, "https://eune.op.gg/summoner/userName=" + username)


@client.command(pass_context=True)
async def cc(ctx, champion: str):
    await client.send_message(ctx.message.channel, "http://www.championcounter.com/" + champion)


@client.command(pass_context=True)
async def live(ctx, username: str):
    await client.send_message(ctx.message.channel, "http://www.lolskill.net/game/EUNE/" + username)


@client.command(pass_context=True)
async def ggc(ctx, champion: str, lane: str):
    await client.send_message(ctx.message.channel, "https://eune.op.gg/champion/" + champion + "/statistics/" + lane)


@client.command(pass_context=True)
async def thiccthighs(ctx):
    embed = discord.Embed()
    imageUrl = thiccLinkList[randint(0, len(animeLinkList) - 1)]
    print(imageUrl)
    embed.set_image(url=imageUrl)
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def animethighs(ctx):
    embed = discord.Embed()
    imageUrl = animeLinkList[randint(0, len(animeLinkList) - 1)]
    print(imageUrl)
    embed.set_image(url=imageUrl)
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context=True)
async def thighs(ctx):
    embed = discord.Embed()
    imageUrl = thighsLinkList[randint(0, len(thighsLinkList) - 1)]
    print(imageUrl)
    embed.set_image(url=imageUrl)
    await client.send_message(ctx.message.channel, embed=embed)



@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await client.send_message(ctx.message.channel, 'Missing argument!')


@client.event
async def delete_message(message):
    client.delete_message(message)

def scrapeReddit(subreddit: str):
    try:
        if (subreddit == "thicc"):
            url = 'https://www.reddit.com/r/ThickThighs/top.json?sort=top&t=week'
        elif (subreddit == "anime"):
            url = 'https://www.reddit.com/r/animelegs/top.json?sort=top&t=week'
        req = urllib.request.Request(url, data=None, headers={'User-Agent': 'BarelLord Bot V1'})

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        linkList = []
        for item in cont['data']['children']:
            linkList.append(item['data']['url'])
        print("First print: ", linkList[randint(0, len(linkList) - 1)])
        return linkList[randint(0, len(linkList) - 1)]



    except Exception:
        print("Something went wrong while scrapping")


def scrapeAnimeSubreddit():
    try:
        url = 'https://www.reddit.com/r/animelegs/top.json?sort=top&t=week'
        req = urllib.request.Request(url, data=None, headers={'User-Agent': 'BarelLord Bot V1'})

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        for item in cont['data']['children']:
            animeLinkList.append(item['data']['preview']['images'][0]['source']['url'])
        print("Done scrapping subreddit Anime")
    except Exception:
        print("Something went wrong while scrapping")

def scrapeThiccSubreddit():
    try:
        url = 'https://www.reddit.com/r/ThickThighs/top.json?sort=top&t=week'
        req = urllib.request.Request(url, data=None, headers={'User-Agent': 'BarelLord Bot V1'})

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        for item in cont['data']['children']:
            thiccLinkList.append(item['data']['preview']['images'][0]['source']['url'])
        print("Done scrapping subreddit Thicc")
    except Exception:
        print("Something went wrong while scrapping")

def scrapeThighsSubreddit():
    try:
        url = 'https://www.reddit.com/r/Thighs/.json?limit=100'
        req = urllib.request.Request(url, data=None, headers={'User-Agent': 'BarelLord Bot V1'})

        r = urllib.request.urlopen(req).read()
        cont = json.loads(r.decode('utf-8'))
        for item in cont['data']['children']:
            thighsLinkList.append(item['data']['preview']['images'][0]['source']['url'])
        print("Done scrapping subreddit Thighs")
    except Exception:
        print("Something went wrong while scrapping")
    
s3 = os.environ['KEY']
client.run(s3)
