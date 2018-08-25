
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
from discord import ChannelType

   
logging.basicConfig(level=logging.INFO)
DJtimeReady = None
isLegacyDJReady = True
hasLegacyDJPlayedMusic = False;
areDJsLoaded = False;


#await client.say(embed=embed)





LegacyDJs = [
    "",
    "",
    "",
    ]
client = commands.Bot(description='BarelLord bot', command_prefix='!')

@client.event
async def on_ready():

    loadDJs()

def loadDJs():
    try:
      file = open("DJs.txt", "r")
      if(os.path.getsize("DJs.txt")) > 0:
          with open("DJs.txt", "r") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            if((len(content) - 1) != 0):
                for i in range(0, len(content)):
                    LegacyDJs[i] = content[i]
            else:
                LegacyDJs[0] = content[0]
            f.close()
      else:
          print("empty")
      file.close()
    except Exception as e:
        print("Something went wrong while loading")
        print(e)

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

    global hasLegacyDJPlayedMusic
    #storage = await self.get_storage(member.server)
    #role_names = await storage.smembers('roles')
    #if "?play" in message.content.lower() and message.author == "coolkix":
        #await client.send_message(message.channel, 'DJ BORO...')
    if "dj_dima pretty please let me play song" in message.content.lower():
        if (message.author.name == LegacyDJs[0] or message.author.name == LegacyDJs[1] or message.author.name == LegacyDJs[2]):
            global isLegacyDJReady
            if (isLegacyDJReady == True):
                isLegacyDJReady = False;
                hasLegacyDJPlayedMusic = False;
                #channel = discord.utils.get(client.get_all_channels(), name="general" ,type=ChannelType.voice)
                #await client.join_voice_channel(channel);
                ##role = discord.role("DJ")
                role = discord.utils.get(message.server.roles, name="DJ")
                roles = [
                    "282221347730489344",
                    ]
                #for member in client.get_all_members():
                #    for role in member.roles:
                #        if(role.name == "DJ"):
                            #roles[0] = role.id
                            #print(roles[0])
                            #break
                 #         print(role.id + "  " + role.server.name + " " + role.server.id)
                ##client.add_roles(message.author, role)
                await client.add_roles(message.author, role)
                await client.send_message(message.channel, 'Welcome LegacyDJ! You can use your power now.')
            else:
                await client.send_message(message.channel, "DJ_DIMA thinks that you are not ready yet!")
    #if ("?play" in message.content.lower() and hasLegacyDJPlayedMusic == False):
    #    
    #    hasLegacyDJPlayedMusic = True;
    #    role = discord.utils.get(message.server.roles, name="DJ")
    #    roles = [
    #               "282221347730489344",
    #                ]
    #    
    #        #for i in range(0, 2):
    #        #    if (message.author.name == LegacyDJs[i]):
    #        #        LegacyDJs[i] = ""
    #    await client.remove_roles(message.author, role)
    #    dj_startTime()
    #    await client.send_message(message.channel, "You have used your LegacyDJ power! :musical_note: \n" + checkTime() + " - Next available song" )
    await client.process_commands(message)

@client.command(pass_context = True)
async def helpMe(ctx):
    em=discord.Embed(title="BarelLord Documentation", description="All BarelLord available commands.", color=0x8000ff)
    em.add_field(name="User commands:", value="!ggc champion line  -  returns op.gg link with specified champion information", inline=False)
    em.add_field(name="", value="?play  - (legacyDJs) plays one song before cooldown", inline=False)
    em.add_field(name="", value="!gg champion  -  return op.gg link with specified champion with main lane", inline=False)
    em.add_field(name="", value="DJ_DIMA pretty please let me play song  -  enables LegacyDJ power", inline=True)
    em.add_field(name="", value="", inline=False)
    em.add_field(name="Admin commands:", value="!addLegacyDJ discord_username  -  adds news LegacyDJ", inline=True)
    em.set_footer(text="Bot made by Roboobox")
    await client.send_message(LegacyDJs[0], "Testing")

@client.command(pass_context = True)
async def gg(ctx, username : str):
    print (ctx.message.channel == "text")
    await client.send_message(ctx.message.channel, "https://eune.op.gg/summoner/userName=" + username)

@client.command(pass_context = True)
async def cc(ctx, champion : str):
    await client.send_message(ctx.message.channel, "http://www.championcounter.com/" + champion)

@client.command(pass_context = True)
async def live(ctx, username : str):
    await client.send_message(ctx.message.channel, "http://www.lolskill.net/game/EUNE/" + username)

@client.command(pass_context = True)
async def ggc(ctx, champion : str, line : str):
    await client.send_message(ctx.message.channel, "https://eune.op.gg/champion/" + champion + "/statistics/" + line)
	
@client.command(pass_context = True)
async def thiccthighs(ctx):
	embed = discord.Embed
	embed.set_image(scrapeReddit("thicc"))
	await client.send_message(message.channel, embed=embed)

@client.command(pass_context = True)
async def addLegacyDJ(ctx, * , member):
    memberFound = False
    authorizedToCommand = False;
    for role in ctx.message.author.roles:
        if(role.permissions.manage_server):
            authorizedToCommand = True


    for memberSelected in client.get_all_members():
        if (member == memberSelected.name):
            
            memberFound = True;
    if(authorizedToCommand == False):
        await client.say(":no_entry: You do not have permission to use this command! :no_entry: ")
    elif(member is None):
        await client.say("Please enter LegacyDJs username!")
    elif(memberFound == False):
        await client.say("There is no such user in this server!")
    else:
        await client.say('|'+ member + '|' + " is now a LegacyDJ")
        if(LegacyDJs[0] == ""):
            LegacyDJs[0] = member
            save(member)
            print(LegacyDJs[1])
        elif(LegacyDJs[1] == ""):
            LegacyDJs[1] = member
            save(member)
        elif(LegacyDJs[2] == ""):
            LegacyDJs[2] = member
            save(member)
        else:
            await client.say("No free space for new LegacyDJ")

@client.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await client.send_message(ctx.message.channel,'Missing argument!')


def dj_startTime():
    hourlater = datetime.now() + timedelta(hours=1)
    global DJtimeReady
    DJtimeReady = hourlater.strftime("%d-%m-%Y %H:%M")
    print(DJtimeReady)
    t = Timer(20, enableLegacyDJ)
    t.start()

@client.event
async def delete_message(message):
    client.delete_message(message)

    
def enableLegacyDJ():
    if(LegacyDJs[0] != ""):
        pass

    for i in range(0, 2):
        for user in client.get_all_members():
            if(LegacyDJs[i] == user.name):
                userToSend = user    
    global isLegacyDJReady
    isLegacyDJReady = True
    if(LegacyDJs[0] != ""):
        print(LegacyDJs[0])

@client.command(pass_context = True)
async def checkTime(ctx):
    if(ctx.message.author.name == LegacyDJs[0] or ctx.message.author == LegacyDJs[1] or ctx.message.author == LegacyDJs[2]):
        if(isLegacyDJReady == True):
            await client.send_message(ctx.message.author, "DJ_DIMA already awaits you.")

        elif(DJtimeReady == None):
            await client.send_message(ctx.message.author, "LegacyDJ power not started...")
        else:
            await client.send_message(ctx.message.author, "LegacyDJ power ready at - " + DJtimeReady)
    else:
        await client.send_message(ctx.message.author, "Only for LegacyDJs... :no_entry: ")
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def getLegacyDJs(ctx):
    await client.send_message(ctx.message.channel, "**1. " + LegacyDJs[0] + "\n2. " + LegacyDJs[1] + "\n3. " + LegacyDJs[2] +"**")


def save(info : str):
    try:
      file = open("DJs.txt", "a")
      file.write(info)
      file.write("\n")
      file.close()
    except Exception:
        print("Something went wrong while saving")
		
def scrapeReddit(subreddit : str):
	try:
		if(subreddit == "thicc"):
			url = 'https://www.reddit.com/r/ThickThighs/top.json?sort=top&t=week'
			req = urllib.request.Request(url, data = None, headers={'User-Agent': 'BarelLord Bot V1'})

			r = urllib.request.urlopen(req).read()
			cont = json.loads(r.decode('utf-8'))
			linkList = []
			for item in cont['data']['children']:
				linkList.append(item['data']['url'])
			return linkList[randint(0, len(linkList)-1)]
	except Exception:
		print("Something went wrong while scrapping")


@client.command(pass_context = True)
async def deleteLegacyDJ(ctx, member):
    memberFound = False
    authorizedToCommand = False;
    for role in ctx.message.author.roles:
        if(role.permissions.manage_server):
            authorizedToCommand = True

    for memberSelected in client.get_all_members():
        if (member == memberSelected.name):
            
            memberFound = True;
    if(authorizedToCommand == False):
        await client.say(":no_entry: You do not have permission to use this command! :no_entry: ")
    elif(member is None):
        await client.say("Please enter LegacyDJs username!")
    elif(memberFound == False):
        await client.say("There is no such user in this server!")
    else:
        if(LegacyDJs[0] == member):
            LegacyDJs[0] = ""
            await client.say('|'+ member + '|' + " is no longer a LegacyDJ")
        elif(LegacyDJs[1] == member):
            LegacyDJs[1] = ""
            await client.say('|'+ member + '|' + " is no longer a LegacyDJ")
        elif(LegacyDJs[2] == member):
            LegacyDJs[2] = ""
            await client.say('|'+ member + '|' + " is no longer a LegacyDJ")
        else:
            await client.say("No such LegacyDJ found!")
    try:
      with open("DJs.txt", "r") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        file = open("DJs.txt", "w")
        for i in range(0, len(content)):
            if(member != content[i]):
                file.write(content[i])
                        
      f.close()
      file.close()
    except Exception as e:
        print("Something went wrong while loading")
        print(e)
    
s3 = os.environ['KEY']
client.run(s3)
