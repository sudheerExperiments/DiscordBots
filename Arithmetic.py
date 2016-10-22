#!/usr/bin/python3

import discord

client = discord.Client()

async def connectionTest(message):
	print('Connection is working good')
	msg = await client.send_message(message.channel, 'Hi')
	
async def join(message):
	print('In join method')
	join_link = message.content.strip('!join')
	if(join_link):
		print('This is a join link, {}'.format(join_link))
		await client.accept_invite(join_link)
		await client.send_message(message.channel, 'The bot has joined')
	else:
		print('Joining link is not proper...')

async def arithmetic(message):
	expression = message.content.strip('!math ')
	try:
		if(expression.find('-')):
			evaluate = eval(expression)
			await client.send_message(message.channel, str(evaluate))
		elif(expression.find('+')):
			evaluate = eval(expression)
			await client.send_message(message.channel, str(evaluate))
		elif(expression.find('*')):
			evaluate = eval(expression)
			await client.send_message(message.channel, str(evaluate))
		elif(expression.find('/')):
			evaluate = eval(expression)
			await client.send_message(message.channel, str(evaluate))
		else:
			print('Cannot evaluate expression')

	except ValueError as e:
		print(e)

@client.event
async def on_message(message):
	#Reference data start
	print(message)
	author = message.author
	print(author)
	#Reference data end

	if(message.content.startswith('!join')):
                await join(message)
	if(message.content.startswith('!test')):
		await connectionTest(message)
	if(message.content.startswith('!math')):
		await arithmetic(message)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

def main():
	#Login username and password
	client.run('MjM5MjkwNjg5NDI1Mzc1MjM0.Cu0VEw.oZoByRPzCHbSe9QHm9RGry2zF0U')

if __name__ == '__main__': main()
