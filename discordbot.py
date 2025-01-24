import discord
import token

client = discord.client()
client.run( token.token )

@client.event
async def on_ready():
		print('bot esta pronto!.')
		
@client.event
async def on_message(message):
		if message.author == client.user:
			return
	
		if message.content.startswith('$hello'):
			await message.channel.send('Hello!')
			
comandos = {}