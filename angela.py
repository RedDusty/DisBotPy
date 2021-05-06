import discord
import random
import datetime
import json
import os
from discord.ext import commands

intents = discord.Intents.all()

# angela = commands.Bot( command_prefix = ['Анджела, ', 'Анджела,', 'Анджела ', 'Анджела', 'анджела, ', 'анджела,', 'анджела ', 'анджела', 'Анджелочка, ', 'Анджелочка,', 'Анджелочка ', 'Анджелочка', 'анджелочка, ', 'анджелочка,', 'анджелочка ', 'анджелочка'] )

angela = commands.Bot( command_prefix='.', intents=intents)
angela.remove_command('help')

client = discord.Client(intents=intents)


initial_extensions = ['cogs.welcomeModule', 'cogs.imageReplace', 'cogs.randomModule', 'cogs.imgSearch', 'cogs.musicModule']

error_extensions = ""
mega_error = ""

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			angela.load_extension(extension)
			try:
				def write_json(data, filename='./messages/modulesOff.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
					data = json.load(json_file)
					  
					temp = data['modules']

					temp.remove(str(extension)[5:])
					  
				write_json(data)
			except Exception as e:
				pass
		except Exception as e:
			error_extensions = error_extensions + str(extension)[5:]
			mega_error = mega_error + str(e) + "\n===================\n===================\n==================="
			angela.unload_extension(extension)
			try:
				def write_json(data, filename='./messages/modulesOff.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['modules']

					temp.append(str(extension)[5:])
					  
				write_json(data)
			except Exception as e:
				pass
			continue
			# print(f'Не удалось загрузить модуль - {extension}', file=sys.stderr)
			# traceback.print_exc()

with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
	data_admins = json.load(json_admins)
	  
	admin_ids = data_admins['admins']


creators = [341647130294747137, 485033648672735253]

@angela.command()
async def ping(ctx):
	embed = discord.Embed(colour=discord.Colour.purple())
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
	embed.set_author(name="Состояние серверов", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
	embed.set_footer(text="os:/system/server/latency.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
	latency = round((angela.latency * 1000),1)
	msgMain = "Задержка - " + str(latency) + " мс"
	if (latency < 350):
		msgValue = "Все сервера работают без какой-либо задержки."
	if (latency >= 350):
		msgValue = "Похоже сервера испытывают небольшую нагрузку." 
	if (latency >= 1000):
		msgValue = "Похоже сервера испытывают нагрузку." 
	if (latency >= 5000):
		msgValue = "Похоже сервера испытывают серьёзную нагрузку. Почему информационный отдел не действует?" 
	if (latency >= 10000):
		msgValue = "Похоже сервера испытывают огромную нагрузку. Самое время звать Йесода." 
	if (latency >= 25000):
		msgValue = "Похоже аномалии уничтожают наши сервера, иначе такую задержку не объяснить." 
	embed.add_field(name=msgMain, value=msgValue, inline=False)

	embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
	
	await ctx.send(embed=embed)

@angela.command()
async def code(ctx):
	if ctx.author.id in creators:
		file = discord.File("code.rar")
		await angela.get_channel(797762330805010442).send("Прочитайте token.txt перед созданием или редактированием бота", file=file)
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")


@angela.command()
async def coinflip(ctx, first = 0, second = 1, roundN = 0):
	try:
		randomN = round(random.uniform(first, second), roundN)
		if (roundN == 0):
			randomN = int(randomN)
		await ctx.send(randomN)
	except Exception as e:
		ctx.send("Ошибка. Неверное значение.")

@angela.command()
async def version(ctx, versions="0"):
	try:
		embed = discord.Embed(colour=discord.Colour.red())
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
		embed.set_author(name="Версия " + versions, icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
		embed.set_footer(text="os:/system/versions/v" + versions + ".info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

		f = open('./messages/version.json', 'r', encoding='utf-8')
		versionJson=json.loads(f.read())
		versionMsg = ""
		for versionOne in versionJson[versions]:
			versionMsg = versionMsg + versionOne + "\n"
		embed.add_field(name="Список изменений", value=versionMsg, inline=False)
		await ctx.send(embed=embed)
	except Exception as e:
		embed = discord.Embed(colour=discord.Colour.red())
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
		embed.set_author(name="Версии бота", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
		embed.set_footer(text="os:/system/versions.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

		f = open('./messages/version.json', 'r', encoding='utf-8')
		versionJson=json.loads(f.read())
		versionMsg = "| "
		for versionMain in versionJson:
			versionMsg = versionMsg + versionMain + " | "
		embed.add_field(name="Версии бота", value=versionMsg, inline=False)
		await ctx.send(embed=embed)

@angela.command()
async def help(ctx, block = "0"):
	try:
		embed = discord.Embed(colour=discord.Colour.gold())
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
		embed.set_author(name="Помощь", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907486635982888/help.png")
		embed.set_footer(text="os:/general/manual.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

		f = open('./messages/help.json', 'r', encoding='utf-8')

		helpJson=json.loads(f.read())
		helpPack = helpJson[block]
		helpMsg = ""
		# print(ctx.author.id)
		for helpOne in helpPack:
			helpMsg = helpMsg + helpOne + "\n"
		embed.add_field(name=block, value=helpMsg, inline=False)
		await ctx.send(embed=embed)
	except Exception as e:
		embed = discord.Embed(colour=discord.Colour.gold())
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
		embed.set_author(name="Помощь", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907486635982888/help.png")
		embed.set_footer(text="os:/general/manual.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

		f = open('./messages/help.json', 'r', encoding='utf-8')

		helpJson=json.loads(f.read())
		helpMsg = "| "
		for helpMain in helpJson:
			# print(ctx.author.id)
			helpMsg = helpMsg + helpMain + " | "
		embed.add_field(name="Разделы", value=helpMsg, inline=False)
		await ctx.send(embed=embed)

@angela.command()
async def modules(ctx):
	try:
		embed = discord.Embed(colour=discord.Colour.green())
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
		embed.set_author(name="Модули", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907489131069450/modules.png")
		embed.set_footer(text="os:/system/modules.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

		f = open('./messages/modules.json', 'r', encoding='utf-8')
		modulesJson=json.loads(f.read())
		for moduleMain in modulesJson:
			modulePack = modulesJson[moduleMain]
			moduleMsg = ""
			for moduleOne in modulePack:
				moduleMsg = moduleMsg + moduleOne + "\n"
			embed.add_field(name=moduleMain, value=moduleMsg, inline=False)
		f = open('./messages/modulesOff.json', 'r', encoding='utf-8')
		modulesJson=json.loads(f.read())
		moduleMsg = "| "
		for modulesPack in modulesJson:
			modules = modulesJson[modulesPack]
			for module in modules:
				moduleMsg = moduleMsg + module + " | "

		embed.add_field(name="Выключены: ", value=moduleMsg, inline=False)
		await ctx.send(embed=embed)
	except Exception as e:
		await ctx.send("<@341647130294747137>, кажется в главном модуле произошла ошибка.")

@angela.command()
async def load(ctx, extension="0"):
	if ctx.author.id in admin_ids:
		if (extension != "0"):
			try:
				if (extension == "iR"):
					extension = "imageReplace"
				elif (extension == "iS"):
					extension = "imgSearch"
				elif (extension == "mM"):
					extension = "musicModule"
				elif (extension == "rM"):
					extension = "randomModule"
				elif (extension == "wM"):
					extension = "welcomeModule"
				else:
					pass
				angela.load_extension(f"cogs.{extension}")
				await ctx.send(f"Модуль {extension} загружен...")
				modulesOffed = extension
				def write_json(data, filename='./messages/modulesOff.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['modules']

					temp.remove(extension)
					  
				write_json(data)
			except:
				await ctx.send(f"Модуль {extension} не существует или написан неправильно.")
		else:
			await ctx.send("Напишите название модуля после команды! .load название_модуля\n Список доступных модулей: .modules")
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

@angela.command()
async def unload(ctx, extension="0"):
	if ctx.author.id in admin_ids:
		if (extension == "iR"):
			extension = "imageReplace"
		elif (extension == "iS"):
			extension = "imgSearch"
		elif (extension == "mM"):
			extension = "musicModule"
		elif (extension == "rM"):
			extension = "randomModule"
		elif (extension == "wM"):
			extension = "welcomeModule"
		else:
			pass
		with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
			data = json.load(json_file) 
		if extension in data['modules']:
			await ctx.send("Модуль уже выключен.")
		else:
			if (extension != "0"):
				try:
					angela.unload_extension(f"cogs.{extension}")
					if (extension == "musicModule"):
						try:
							server = ctx.message.server
							voice_client = client.voice_client_in(server)
							await voice_client.disconnect()
						except Exception as e:
							pass
					modulesOffed = extension
					await ctx.send(f"Модуль {extension} отгружен...")
					def write_json(data, filename='./messages/modulesOff.json'): 
						with open(filename,'w', encoding='utf-8') as f: 
							json.dump(data, f, indent=4, ensure_ascii=False) 

					with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
						data = json.load(json_file) 
						  
						temp = data['modules']

						temp.append(modulesOffed)
						  
					write_json(data)
				except:
					await ctx.send(f"Модуль {extension} не существует или написан неправильно.")
			else:
				await ctx.send("Напишите название модуля после команды! .unload название_модуля\n Список доступных модулей: .modules")
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

@angela.command()
async def reload(ctx, extension="0"):
	if ctx.author.id in admin_ids:
		if (extension != "0"):
			try:
				if (extension == "iR"):
					extension = "imageReplace"
				elif (extension == "iS"):
					extension = "imgSearch"
				elif (extension == "mM"):
					extension = "musicModule"
				elif (extension == "rM"):
					extension = "randomModule"
				elif (extension == "wM"):
					extension = "welcomeModule"
				else:
					pass
				angela.unload_extension(f"cogs.{extension}")
				if (extension == "musicModule"):
					try:
						server = ctx.message.server
						voice_client = client.voice_client_in(server)
						await voice_client.disconnect()
					except Exception as e:
						pass
				await ctx.send(f"Модуль {extension} отгружен...")
				modulesOffed = extension
				def write_json(data, filename='./messages/modulesOff.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['modules']

					temp.append(modulesOffed)
					  
				write_json(data)
				angela.load_extension(f"cogs.{extension}")
				await ctx.send(f"Модуль {extension} перезагружен...")
				modulesOffed = extension
				def write_json(data, filename='./messages/modulesOff.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/modulesOff.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['modules']

					temp.remove(extension)
					  
				write_json(data)
			except:
				await ctx.send(f"Модуль {extension} не существует или написан неправильно.")
		else:
			await ctx.send("Напишите название модуля после команды! .reload название_модуля\n Список доступных модулей: .modules")
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

@angela.command()
async def addAdmin(ctx, newAdmin: discord.Member = None):
	with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
		data_admins = json.load(json_admins)
		  
		admin_ids = data_admins['admins']
	if ctx.author.id in admin_ids:
		if (newAdmin != None):
			def write_json(data, filename='./messages/blocked.json'): 
				with open(filename,'w', encoding='utf-8') as f: 
					json.dump(data, f, indent=4, ensure_ascii=False) 

			with open('./messages/blocked.json', encoding='utf-8') as json_file: 
				data = json.load(json_file) 
				  
				temp = data['admins']
				temp.append(newAdmin.id)
					  
			write_json(data)
			await ctx.send(f'{newAdmin} теперь может использовать команды управляющего.')
		else:
			await ctx.send("Пользователь не найден.")
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")


@angela.command()
async def removeAdmin(ctx, removeAdmin: discord.Member = None):
	with open('./messages/blocked.json', encoding='utf-8') as json_admins: 
		data_admins = json.load(json_admins)
		  
		admin_ids = data_admins['admins']
	if ctx.author.id in admin_ids:
		if (removeAdmin != None):
			if removeAdmin.id not in creators:
				def write_json(data, filename='./messages/blocked.json'): 
					with open(filename,'w', encoding='utf-8') as f: 
						json.dump(data, f, indent=4, ensure_ascii=False) 

				with open('./messages/blocked.json', encoding='utf-8') as json_file: 
					data = json.load(json_file) 
					  
					temp = data['admins']
					temp.remove(removeAdmin.id)
						  
				write_json(data)
				await ctx.send(f'{removeAdmin} больше не может использовать команды управляющего.')
			else:
				await ctx.send("Нельзя использовать на этого пользователя.")
		else:
			await ctx.send("Пользователь не найден.")
	else:
		await ctx.send("Ваш уровень доступа не подходит для использования этой команды...")

@angela.command()
async def blockList(ctx):
	embed = discord.Embed(colour=discord.Colour.dark_blue())
	# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/797111195738832926/797907862868197386/Astand.png")
	# embed.set_author(name="Информация", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
	embed.set_footer(text="os:/general/blockList.info", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

	f = open('./messages/blocked.json', 'r', encoding='utf-8')

	blockedJson=json.loads(f.read())
	for blockedMain in blockedJson:
		blockedPack = blockedJson[blockedMain]
		if (blockedMain == "blockedMusic"):
			blockedName = "Не могут использовать модуль musicModule:"
		if (blockedMain == "blockedSearch"):
			blockedName = "Не могут использовать модуль imgSearch:"
		if (blockedMain == "admins"):
			blockedName = "Управляющие:"
		blockedMsg = ""
		if not blockedPack:
			continue
		for blockedOne in blockedPack:
			user = str(angela.get_user(blockedOne))
			if (user == "None"):
				continue
			else:
				blockedMsg = blockedMsg + user + "\n"
		embed.add_field(name=blockedName, value=blockedMsg, inline=False)
	await ctx.send(embed=embed)

@angela.event
async def on_ready():
	print( ' Logged as {0.user}'.format(angela) )
	print(angela.user.name)
	print(angela.user.id)
	print('--------')
	print('---Главный модуль загружен---')
	if (error_extensions != ""):
		await angela.get_channel(797762330805010442).send(f'<@341647130294747137>, модули - {error_extensions} дали сбой. Эти модули были отключены и будут включены при повторном запуске бота или с помощью команды .reload название_модуля')
		await angela.get_channel(797762330805010442).send(f'```{mega_error}```')
	return await angela.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за вами"))
	
	

# @angela.event
# async def on_message(message):
# 	msg = message.content.lower()

token = open( 'token.txt', 'r').readline()

angela.run( token )