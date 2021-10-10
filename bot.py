import discord 
import os 
#import search_runpee
from decouple import config

#intialize the client 
client = discord.Client()


# asynchronous code means we dont need fot the code to finish to start executing other action of the code 


# discord event to check when the bot is online 

@client.event
async def on_ready():
    print (f'{client.user} is now online !')


client.run(config('TOKEN'))

