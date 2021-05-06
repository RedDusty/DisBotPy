import discord
import random
import datetime
import json
from discord.ext import commands

class welcomeModule(commands.Cog, name='welcomeModule'):

	def __init__(self, angela):
		self.angela = angela

	@commands.Cog.listener()
	async def on_ready(self):
		print('---Модуль welcomeModule загружен---')

	# Просмотр строк в welcome.json
	@commands.command()
	async def welcome_check(self, ctx):
		f = open('./messages/welcome.json', 'r', encoding='utf-8')
		welcomeJson=json.loads(f.read())
		welcomeMsg = "```json\nwelcome.json\n"
		numstr = 0
		for welcomePack in welcomeJson["welcome"]:
			numstr = numstr + 1
			welcomeMsg = welcomeMsg + "id=" + str(numstr) + ": "
			for welcomeOne in welcomePack:
				if (welcomeOne == "https://cdn.discordapp.com/emojis/797459037670211614.png?v=1"):
					welcomeOne = '<:Astand:797761734026461185>'
					welcomeMsg = welcomeMsg + welcomeOne + " -- "
				elif (welcomeOne == "https://cdn.discordapp.com/emojis/797459037671260190.png?v=1"):
					welcomeOne = '<:Alooking:797761792964165633>'
					welcomeMsg = welcomeMsg + welcomeOne + " -- "
				else:
					welcomeMsg = welcomeMsg + welcomeOne + "\n"
		welcomeMsg = welcomeMsg + "```"
		await ctx.send(welcomeMsg)

	# Удаление строки из welcome.json
	@commands.command()
	async def welcome_del(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
			data_admins = json.load(json_admins)
			  
			admin_ids = data_admins['admins']
		if ctx.author.id in admin_ids:
			f = open('./messages/welcome.json', 'r', encoding='utf-8')
			welcomeJson=json.loads(f.read())
			welcomes=welcomeJson["welcome"]
			
			welcomeMsg = "**Укажите id удаляемой строки. Напишите только число!**```json\nwelcome.json\n"
			numstr = 0
			for welcomePack in welcomeJson["welcome"]:
				numstr = numstr + 1
				welcomeMsg = welcomeMsg + "id=" + str(numstr) + ": "
				for welcomeOne in welcomePack:
					if (welcomeOne == "https://cdn.discordapp.com/emojis/797459037670211614.png?v=1"):
						welcomeOne = '<:Astand:797761734026461185>'
						welcomeMsg = welcomeMsg + welcomeOne + " -- "
					elif (welcomeOne == "https://cdn.discordapp.com/emojis/797459037671260190.png?v=1"):
						welcomeOne = '<:Alooking:797761792964165633>'
						welcomeMsg = welcomeMsg + welcomeOne + " -- "
					else:
						welcomeMsg = welcomeMsg + welcomeOne + "\n"
			welcomeMsg = welcomeMsg + "```"
			await ctx.send(welcomeMsg)
			def check(user):
				if user.author.id in admin_ids:
					return True
			message = await self.angela.wait_for('message', check=check)
			try:
				welcomes.remove(welcomes[int(message.content)-1])
				welcomeMsg = f"**Строка с id={message.content} была удалена!**```json\nwelcome.json\n"
				numstr = 0
				for welcomePack in welcomes:
					numstr = numstr + 1
					welcomeMsg = welcomeMsg + "id=" + str(numstr) + ": "
					for welcomeOne in welcomePack:
						if (welcomeOne == "https://cdn.discordapp.com/emojis/797459037670211614.png?v=1"):
							welcomeOne = '<:Astand:797761734026461185>'
							welcomeMsg = welcomeMsg + welcomeOne + " -- "
						elif (welcomeOne == "https://cdn.discordapp.com/emojis/797459037671260190.png?v=1"):
							welcomeOne = '<:Alooking:797761792964165633>'
							welcomeMsg = welcomeMsg + welcomeOne + " -- "
						else:
							welcomeMsg = welcomeMsg + welcomeOne + "\n"
				welcomeMsg = welcomeMsg + "```"
				await ctx.send(welcomeMsg)
				f.close
				new_data = {'welcome': welcomes}
				f = open("./messages/welcome.json", "w", encoding='utf-8')
				json.dump(new_data, f, ensure_ascii=False, indent=4)
				f.close
			except Exception as e:
				await ctx.send("Ошибка. Неверное значение.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

	# Добавление новой строки в welcome.json
	creators = [341647130294747137, 485033648672735253]
	@commands.command()
	async def welcome_add(self, ctx):
		with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
			data_admins = json.load(json_admins)
			  
			admin_ids = data_admins['admins']
		if ((ctx.author.id in admin_ids) or (ctx.author.id in creators)):
			await ctx.send('Напишите приветствие следующим сообщением.\nЧтобы добавить никнейм, напишите - {} в сообщении.\nЭмодзи допустимы. В конце команду можно отменить.\nПример: Здравствуй, сотрудник {}, не забудь забрать свое снаряжение. <:egoSuit:797761960695300096>')
			def check(user):
				if user.author.id in admin_ids:
					return True
			message = await self.angela.wait_for('message', check=check)
			mbd = discord.Embed(
				colour = discord.Colour.blurple(),
				title = 'Новый сотрудник - ' + str(ctx.author),
				description = message.content.format(ctx.author)
			)

			mbd.timestamp = datetime.datetime.now(datetime.timezone.utc)
			mbd.set_footer(text="os:/general/modules/welcome/welcome_test.lc", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

			await ctx.send(embed=mbd)
			await ctx.send("А теперь добавим эмоцию. Доступные эмоции: Astand, Alooking.\nПример: Alooking")
			def check(user):
				if user.author.id in admin_ids:
					return True
			emotion = await self.angela.wait_for('message', check=check)
			if (emotion.content == "Alooking"):
				emotion = "https://cdn.discordapp.com/emojis/797459037671260190.png?v=1"
			elif (emotion.content == "Astand"):
				emotion = "https://cdn.discordapp.com/emojis/797459037670211614.png?v=1"
			else: # Стандартно - Astand
				emotion = "https://cdn.discordapp.com/emojis/797459037670211614.png?v=1"
			mbd = discord.Embed(
				colour = discord.Colour.blurple(),
				title = 'Новый сотрудник - ' + str(ctx.author),
				description = message.content.format(ctx.author)
			)
			mbd.set_thumbnail(url=emotion)
			mbd.timestamp = datetime.datetime.now(datetime.timezone.utc)
			mbd.set_footer(text="os:/general/modules/welcome/welcome_test.lc", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

			await ctx.send(embed=mbd)
			await ctx.send("Добавлять в список приветствий это? Напишите: \'Да\' или Любое сообщение - для отмены.")
			okay = await self.angela.wait_for('message', check=check)
			if (okay.content == "Да"):
				new_welcome = [
					emotion, message.content
				]
				def write_json(data, filename='./messages/welcome.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/welcome.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['welcome']

					temp.append(new_welcome)
					  
				write_json(data)
				await ctx.send("Приветствие было добавлено в список.")
			else:
				await ctx.send("Приветствие не было добавлено.")
		else:
			await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

	# Приветствие нового сотрудника
	@commands.Cog.listener()
	async def on_member_join(self, member):
		print(f'Новый сотрудник - {member}')
		try:
			f = open('./messages/welcome.json', 'r', encoding='utf-8')
			text=json.loads(f.read())
			welcomes=text["welcome"]
			welcomes = random.choice(welcomes)

			mbd = discord.Embed(
				colour = discord.Colour.blurple(),
				title = 'Новый сотрудник - ' + str(member),
				description = welcomes[1].format(member)
			)
			mbd.set_thumbnail(url=welcomes[0])

			mbd.timestamp = datetime.datetime.now(datetime.timezone.utc)
			mbd.set_footer(text="os:/general/modules/welcome.lc", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
			channel = self.angela.get_channel(702246093211041943)

			await channel.send(embed=mbd)
		except Exception as e:
			await self.angela.get_channel(702246093211041943).send("Кажется в модуле приветствия ошибка, но мы всё же надеемся, что {} покажет себя с лучшей стороны.".format(member))
			await self.angela.get_channel(797762330805010442).send('<@341647130294747137> - welcome.py дал сбой')
			await self.angela.get_channel(797762330805010442).send(f'```{e}```')

def setup(angela):
	angela.add_cog(welcomeModule(angela))
	print('---Модуль welcomeModule загружается---')