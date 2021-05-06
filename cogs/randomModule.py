import discord
import aiohttp
import datetime
# from googletrans import Translator
from discord.ext import commands

class randomModule(commands.Cog, name='randomModule'):

	def __init__(self, angela):
		self.angela = angela

	@commands.Cog.listener()
	async def on_ready(self):
		print('---Модуль randomModule загружен---')

	@commands.command()
	async def randomImage(self, ctx):
		await ctx.send("Введите животное из списка: dog, cat, panda, fox, red_panda, koala, birb, racoon, kangaroo")
		try:
			animal = await self.angela.wait_for('message')
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://some-random-api.ml/animal/" + str(animal.content)) as r:
						data = await r.json()

						mbd = discord.Embed(
							title = str(animal.content).title(),
							colour = discord.Colour.blurple()
						)

						mbd.timestamp = datetime.datetime.now(datetime.timezone.utc)
						mbd.set_footer(text=f"os:/general/modules/fun/randomImage/{animal.content}.pic", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")
						mbd.set_image(url=data['image'])

						await ctx.send(embed=mbd)
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

	@commands.command()
	async def randomFact(self, ctx):
		await ctx.send("Введите животное из списка: dog, cat, panda, fox, red_panda, koala, birb, racoon, kangaroo")
		try:
			animal = await self.angela.wait_for('message')
			async with ctx.channel.typing():
				async with aiohttp.ClientSession() as cs:
					async with cs.get("https://some-random-api.ml/animal/" + str(animal.content)) as r:
						data = await r.json()
						print(data['fact'])
						mbd = discord.Embed(
							title = str(animal.content).title(),
							colour = discord.Colour.blurple()
						)
						mbd.add_field(name=data['fact'], value="English", inline=False)
						# translator = Translator()
						# result = translator.translate(data['fact'], src='english', dest='russian')
						
						# mbd.add_field(name=result.text, value="Русский", inline=False)
						mbd.timestamp = datetime.datetime.now(datetime.timezone.utc)
						mbd.set_footer(text=f"os:/general/modules/fun/randomFact/{animal.content}.lc", icon_url="https://cdn.discordapp.com/attachments/797111195738832926/797907483929739274/footer_icon.png")

						await ctx.send(embed=mbd)
		except Exception as e:
			await ctx.send("Ошибка. Неверное значение.")

def setup(angela):
	angela.add_cog(randomModule(angela))
	print('---Модуль randomModule загружается---')