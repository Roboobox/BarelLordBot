
import discord;
import logging

from discord.ext import commands

   
logging.basicConfig(level=logging.INFO)



client = commands.Bot(description='BarelLord bot', command_prefix='*')


@client.event
async def on_message(message):
    if "olafs" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejs...')
    elif "olafu" in message.content.lower():
        await client.send_message(message.channel, '*Alekseju...')
    elif "olafam" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejam...')
    elif "olafa" in message.content.lower():
        await client.send_message(message.channel, '*Alekseja...')
    elif "olafā" in message.content.lower():
        await client.send_message(message.channel, '*Aleksejā...')
    elif "olafi" in message.content.lower():
        await client.send_message(message.channel, '*Alekseji...')
    elif "olaf" in message.content.lower():
        await client.send_message(message.channel, '*Aleksej...')

client.run('Mjk3NDQ1Mjc5NTI1ODk2MTkz.DDBYZg.arP3Qh43pDTyDb5Jpsxh5ISjQWs')
