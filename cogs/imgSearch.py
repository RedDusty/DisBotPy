import discord
import datetime
import json
import random
from py3pin.Pinterest import Pinterest
from discord.ext import commands

class imgSearch(commands.Cog, name='imgSearch'):

	def __init__(self, angela):
		self.angela = angela

	@commands.Cog.listener()
	async def on_ready(self):
		print('---Модуль imgSearch загружен---')

	@commands.command()
	async def imgSearch(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedSearch: 
			data_blockedSearch = json.load(json_blockedSearch)
			  
			blockedSearch_ids = data_blockedSearch['blockedSearch']
		if ctx.author.id not in blockedSearch_ids:
			async with ctx.channel.typing():
				try:
					pinterest = Pinterest(email='levan8up@gmail.com', password='101201po12', username='levan8up', cred_root='data')
					pinterest.login()
					search_batch = pinterest.search(scope='boards', query=ctx.message.content[11:])
					search_batch = random.choice(search_batch)
					await ctx.send(search_batch['image_cover_hd_url'])
				except Exception as e:
					if (e == "Message: unknown error: DevToolsActivePort file doesn't exist"):
						await ctx.send("Драйвер поиска был обновлён. Повторите запрос ещё раз.")
					else:
						await ctx.send(e)
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def imgSearchBomb(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedSearch: 
			data_blockedSearch = json.load(json_blockedSearch)
			  
			blockedSearch_ids = data_blockedSearch['blockedSearch']
		if ctx.author.id not in blockedSearch_ids:
			number = 4
			async with ctx.channel.typing():
				try:
					pinterest = Pinterest(email='levan8up@gmail.com', password='101201po12', username='levan8up', cred_root='data')
					pinterest.login()
					search_batch = pinterest.search(scope='boards', query=ctx.message.content)
					send_result = ""
					while number > 0:
						number = number - 1
						send_result = send_result + " " + str(random.choice(search_batch)['image_cover_hd_url'])
					await ctx.send(send_result)
				except Exception as e:
					await ctx.send(e)
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def mutePin(self, ctx, userMute: discord.Member = None):
		creators = [341647130294747137, 485033648672735253]
		with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
			data_admins = json.load(json_admins)
			  
			admin_ids = data_admins['admins']
		if ctx.author.id in admin_ids:
			if (userMute != None):
				if userMute.id not in creators:
					def write_json(data, filename='./messages/blocked.json'): 
						with open(filename,'w', encoding='utf-8') as f: 
							json.dump(data, f, indent=4, ensure_ascii=False) 

					with open('./messages/blocked.json', encoding='utf-8') as json_file:
						data = json.load(json_file)
						temp = data['blockedSearch']
						temp.append(userMute.id)
							  
					write_json(data)
					await ctx.send(f'{userMute} больше не может использовать команды модуля imgSearch.')
				else:
					await ctx.send("Нельзя использовать на этого пользователя.")
			else:
				await ctx.send("Пользователь не найден.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

	@commands.command()
	async def unmutePin(self, ctx, userMute: discord.Member = None):
		with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
			data_admins = json.load(json_admins)
			  
			admin_ids = data_admins['admins']
		if ctx.author.id in admin_ids:
			if (userMute != None):
				def write_json(data, filename='./messages/blocked.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/blocked.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['blockedSearch']
					temp.remove(userMute.id)
						  
				write_json(data)
				await ctx.send(f'{userMute} теперь может использовать команды модуля imgSearch.')
			else:
				await ctx.send("Пользователь не найден.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

def setup(angela):
	angela.add_cog(imgSearch(angela))
	print('---Модуль imgSearch загружается---')