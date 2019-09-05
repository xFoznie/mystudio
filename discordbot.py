import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
	print('Bot is online.')

@client.command()
async def ping(ctx):
	await ctx.send('Pong!')
roll=['Великие правители','Суровые выживальщики и строители','Верные слуги Германии','Заднеприводные танкисты Панцерваффе','Рыцари ЧСВешного стола','Овердрочеры','Буу блять','Коэсер','ДотоРотер','Изучатели черных дыр','опущеный']

@client.command()
async def кто(ctx, *, message):
	await ctx.send('{text} пидрила!'.format(text = message))
	
@client.command()
async def "кто я"(ctx):
	await ctx.send('Ты пидрила!')
	
@client.command()
async def "кто ты"(ctx):
	await ctx.send('Я не пидр!')
	
@client.command()
async def Кто(ctx, *, message):
	await ctx.send('{text} пидрила!'.format(text = message))

@client.command()
async def creeper(ctx):
	await ctx.send('Aww maan')

@client.command()
async def Косурина(ctx):
	await ctx.send('= миллион домашки. Беги, глупец!')

@client.command()
async def Повтори(ctx, *, message):
	await ctx.send('{t}'.format(t = message))



@client.command()
async def giverole(ctx, *, message):
	author = ctx.message.author
	
	user = ctx.message.author
	role = discord.utils.get(user.guild.roles, name = message)
	await discord.Member.add_roles(user, role)

token = os.environ.get('BOT_TOKEN')
client.run(str(token))
