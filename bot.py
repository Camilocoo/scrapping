import discord 
import os 
#import search_runpee
from decouple import config




#intialize the client 
client = discord.Client()

hello_message = '''Hello there! I\'m the fidgeting bot from RunPee. Sorry but I really need to go to the bathroom... 
Please read my manual by typing $help or $commands while I\'m away.'''

no_result_message = '''Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, 
but you can subscribe to our news letter for updates of our newest content 
--> https://runpee.com/about-runpee/runpee-movie-newsletter/'''

# asynchronous code means we dont need fot the code to finish to start executing other action of the code 


# discord event to check when the bot is online 

@client.event
async def on_ready():
    print (f'{client.user} is now online !')

@client.event

async def on_message(message):

    #making sure the bot doesnt respond to its own message and aviod and infinit loop 
    if message.author == client.user:
        return 
    message_content = message.content.lower()

    if message.content.startswith(f'$hello'):
        await message.channel.send(f'''{hello_message}''')

    
    



client.run(config('TOKEN'))

