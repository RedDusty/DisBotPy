import discord
from discord.ext import commands
import ctypes
import ctypes.util
import youtube_dl
import os
import json

class musicModule(commands.Cog, name='musicModule'):
	
	def __init__(self, angela):
		self.angela = angela


	@commands.Cog.listener()
	async def on_ready(self):
		print('---Модуль musicModule загружен---')

	@commands.command()
	async def join(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			channel = ctx.author.voice.channel
			await channel.connect()
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def leave(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			channel = discord.utils.get(self.angela.voice_clients)
			await channel.disconnect()
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def play(self, ctx, url):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			try:
				YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
				FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
				voice = discord.utils.get(self.angela.voice_clients, guild=ctx.guild)
				if not voice.is_playing():
					with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
						info = ydl.extract_info(url, download=False)
					URL = info['formats'][0]['url']
					discord.opus.load_opus(ctypes.util.find_library('opus'))
					voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
					voice.is_playing()
				else:
					await ctx.send("Подождите своей очереди.")
					return
			except Exception as e:
				await ctx.send("Ошибка.")
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def stop(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			server = ctx.message.guild
			voice_client = server.voice_client

			voice_client.stop()
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def resume(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			server = ctx.message.guild
			voice_client = server.voice_client

			voice_client.resume()
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def pause(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_blockedMusic: 
			data_blockedMusic = json.load(json_blockedMusic)
			  
			blockedMusic_ids = data_blockedMusic['blockedMusic']
		if ctx.author.id not in blockedMusic_ids:
			server = ctx.message.guild
			voice_client = server.voice_client

			voice_client.pause()
		else:
			await ctx.send("Вы не можете использовать команды этого модуля.")

	@commands.command()
	async def muteMusic(self, ctx, userMute: discord.Member = None):
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
						  
						temp = data['blockedMusic']
						temp.append(userMute.id)
						  
					write_json(data)
					await ctx.send(f'{userMute} больше не может использовать команды модуля musicModule.')
				else:
					await ctx.send("Нельзя использовать на этого пользователя.")
			else:
				await ctx.send("Пользователь не найден.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

	@commands.command()
	async def unmuteMusic(self, ctx, userMute: discord.Member = None):
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
					  
					temp = data['blockedMusic']
					temp.remove(userMute.id)
					  
				write_json(data)
				await ctx.send(f'{userMute} теперь может использовать команды модуля musicModule.')
			else:
				await ctx.send("Пользователь не найден.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")


def setup(angela):
	angela.add_cog(musicModule(angela))
	print('---Модуль musicModule загружается---')