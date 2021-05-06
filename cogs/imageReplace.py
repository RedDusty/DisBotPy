import discord
from discord.ext import commands
from PIL import Image
from io import BytesIO

class imageReplace(commands.Cog, name='imageReplace'):

	def __init__(self, angela):
		self.angela = angela

	@commands.Cog.listener()
	async def on_ready(self):
		print('---Модуль imageReplace загружен---')

	@commands.command()
	async def bonk(self, ctx, userBonk: discord.Member = None, userAuthor: discord.Member = None):
		try:
			try:
				if ((userBonk == None) and (userAuthor == None)):
					userBonk = ctx.author
					assetBonk = userBonk.avatar_url_as(size = 128)
					userAuthor = self.angela.user
					assetAuthor = userAuthor.avatar_url_as(size = 128)
				else:
					if (userBonk == None):
						userBonk = ctx.author
						assetBonk = userBonk.avatar_url_as(size = 128)
					else:
						assetBonk = userBonk.avatar_url_as(size = 128)
						if (userAuthor != None):
							assetAuthor = userAuthor.avatar_url_as(size = 128)
			except Exception as e:
				await ctx.send("Ошибка. Неверное значение.")
			bonk = Image.open("./images/fun/imageReplace/bonk.png")
			data = BytesIO(await assetBonk.read())
			pfp = Image.open(data)
			pfp = pfp.resize((144,144))
			bonk.paste(pfp, (434, 239))
			bonk.save("imageReplace.png")
			if (userAuthor == None):
				await ctx.send(file = discord.File("imageReplace.png"))
			else:
				bonk = Image.open("./imageReplace.png")
				data = BytesIO(await assetAuthor.read())
				pfp = Image.open(data)
				pfp = pfp.resize((144,144))
				bonk.paste(pfp, (166, 89))
				bonk.save("imageReplace.png")
				await ctx.send(file = discord.File("imageReplace.png"))
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

	@commands.command()
	async def bonkHorny(self, ctx, userBonk: discord.Member = None, userAuthor: discord.Member = None):
		try:
			try:
				if ((userBonk == None) and (userAuthor == None)):
					userBonk = ctx.author
					assetBonk = userBonk.avatar_url_as(size = 128)
					userAuthor = self.angela.user
					assetAuthor = userAuthor.avatar_url_as(size = 128)
				else:
					if (userBonk == None):
						userBonk = ctx.author
						assetBonk = userBonk.avatar_url_as(size = 128)
					else:
						assetBonk = userBonk.avatar_url_as(size = 128)
						if (userAuthor != None):
							assetAuthor = userAuthor.avatar_url_as(size = 128)
			except Exception as e:
				await ctx.send("Ошибка. Неверное значение.")
			bonk = Image.open("./images/fun/imageReplace/bonkHorny.png")
			data = BytesIO(await assetBonk.read())
			pfp = Image.open(data)
			pfp = pfp.resize((144,144))
			bonk.paste(pfp, (434, 239))
			bonk.save("imageReplace.png")
			if (userAuthor == None):
				await ctx.send(file = discord.File("imageReplace.png"))
			else:
				bonk = Image.open("./imageReplace.png")
				data = BytesIO(await assetAuthor.read())
				pfp = Image.open(data)
				pfp = pfp.resize((144,144))
				bonk.paste(pfp, (166, 89))
				bonk.save("imageReplace.png")
				await ctx.send(file = discord.File("imageReplace.png"))
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

	@commands.command()
	async def slap(self, ctx, userBonk: discord.Member = None, userAuthor: discord.Member = None):
		try:
			try:
				if ((userBonk == None) and (userAuthor == None)):
					userBonk = ctx.author
					assetBonk = userBonk.avatar_url_as(size = 128)
					userAuthor = self.angela.user
					assetAuthor = userAuthor.avatar_url_as(size = 128)
				else:
					if (userBonk == None):
						userBonk = ctx.author
						assetBonk = userBonk.avatar_url_as(size = 128)
					else:
						assetBonk = userBonk.avatar_url_as(size = 128)
						if (userAuthor != None):
							assetAuthor = userAuthor.avatar_url_as(size = 128)
			except Exception as e:
				await ctx.send("Ошибка. Неверное значение.")
			bonk = Image.open("./images/fun/imageReplace/slap.png")
			data = BytesIO(await assetBonk.read())
			pfp = Image.open(data)
			pfp = pfp.resize((128,128))
			bonk.paste(pfp, (353, 499))
			bonk.save("imageReplace.png")
			if (userAuthor == None):
				await ctx.send(file = discord.File("imageReplace.png"))
			else:
				bonk = Image.open("./imageReplace.png")
				data = BytesIO(await assetAuthor.read())
				pfp = Image.open(data)
				pfp = pfp.resize((134,134))
				bonk.paste(pfp, (394, 214))
				bonk.save("imageReplace.png")
				await ctx.send(file = discord.File("imageReplace.png"))
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

	@commands.command()
	async def aaam(self, ctx, userBonk: discord.Member = None, userAuthor: discord.Member = None):
		try:
			if (userBonk == None):
				userBonk = ctx.author
				assetBonk = userBonk.avatar_url_as(size = 128)
			if (userAuthor != None):
				userAuthor = None
			assetBonk = userBonk.avatar_url_as(size = 128)
			bonk = Image.open("./images/fun/imageReplace/aaam.png")
			data = BytesIO(await assetBonk.read())
			pfp = Image.open(data)
			pfp = pfp.resize((309,309))
			alpha = Image.new('L', pfp.size, 255)
			pfp.putalpha(alpha)
			maskT = pfp.split()[3].point(lambda i: i * 75 / 100.)
			bonk.paste(pfp, (418, 179), mask = maskT)
			bonk.save("imageReplace.png")
			await ctx.send(file = discord.File("imageReplace.png"))
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

	@commands.command()
	async def eat(self, ctx, userBonk: discord.Member = None, userAuthor: discord.Member = None):
		try:
			if (userBonk == None):
				userBonk = ctx.author
				assetBonk = userBonk.avatar_url_as(size = 128)
			if (userAuthor != None):
				userAuthor = None
			assetBonk = userBonk.avatar_url_as(size = 128)
			bonk = Image.open("./images/fun/imageReplace/eat.png")
			data = BytesIO(await assetBonk.read())
			pfp = Image.open(data)
			pfp = pfp.resize((136,136))
			alpha = Image.new('L', pfp.size, 255)
			pfp.putalpha(alpha)
			maskT = pfp.split()[3].point(lambda i: i * 75 / 100.)
			bonk.paste(pfp, (333, 80), mask = maskT)
			bonk.save("imageReplace.png")
			await ctx.send(file = discord.File("imageReplace.png"))
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")


def setup(angela):
	angela.add_cog(imageReplace(angela))
	print('---Модуль imageReplace загружается---')