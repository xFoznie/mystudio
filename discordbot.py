import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "")

clientpref = commands.Bot(command_prefix = "-")

allroles=['Великие правители','Суровые выживальщики и строители','Верные слуги Германии','Заднеприводные танкисты Панцерваффе','Рыцари ЧСВешного стола','Овердрочеры','Буу блять','Коэсер','ДотоРотер','Изучатели черных дыр', 'факинг ю рашен геймерс жта фор ЮСА']

@client.event
async def on_ready():
	await client.change_presence(status = discord.Status.online, activity = discord.Game('Напиши Начать'))
	print('Bot is online!')


@client.command()
async def Начать(ctx):
	await ctx.send("Приветствую тебя на нашей базе, {memb.mention}! \n Для того, чтобы ты смог заходить в голосовые чаты своей игры, тебе нужно иметь определеную роль, которую ты можешь получить набрав    giverole \"роль без кавычек\" \n Список доступных ролей: \n Minecraft - {r1.mention} \n Civilization - {r0.mention} \n WoT/WoW/WarThunder - {r3.mention} \n Garry s Mod - {r2.mention} \n Dota2 - {r8.mention} \n CS:GO - {r7.mention} \n Paladins - {r5.mention} \n Deceit - {r6.mention} \n GTA5 - {r10.mention} \n ASTRONEER - {r9.mention} \n Важно копировать названия ролей без изменений!".format(memb = ctx.message.author, r0 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[0]), r1 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[1]), r2 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[2]), r3 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[3]), r4 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[4]), r5 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[5]), r6 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[6]), r7 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[7]), r8 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[8]), r9 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[9]), r10 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[10])))

@client.command()
async def начать(ctx):
	await ctx.send("Приветствую тебя на нашей базе, {memb.mention}! \n Для того, чтобы ты смог заходить в голосовые чаты своей игры, тебе нужно иметь определеную роль, которую ты можешь получить набрав    giverole \"роль без кавычек\" \n Список доступных ролей: \n Minecraft - {r1.mention} \n Civilization - {r0.mention} \n WoT/WoW/WarThunder - {r3.mention} \n Garry s Mod - {r2.mention} \n Dota2 - {r8.mention} \n CS:GO - {r7.mention} \n Paladins - {r5.mention} \n Deceit - {r6.mention} \n GTA5 - {r10.mention} \n ASTRONEER - {r9.mention} \n Важно копировать названия ролей без изменений!".format(memb = ctx.message.author, r0 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[0]), r1 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[1]), r2 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[2]), r3 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[3]), r4 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[4]), r5 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[5]), r6 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[6]), r7 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[7]), r8 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[8]), r9 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[9]), r10 = discord.utils.get(ctx.message.author.guild.roles, name = allroles[10])))



@client.command()
async def ping(ctx):
	await ctx.send('Pong!')


@client.command()
async def кто(ctx, *, message):
	lenght = len(message)
	if (message[lenght-1] == '?'):
		message = message[:-1]
	await ctx.send('{text} пидрила!'.format(text = message))
	
@client.command()
async def Кто(ctx, *, message):
	lenght = len(message)
	if (message[lenght-1] == '?'):
		message = message[:-1]
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
@commands.has_role('Сверхмикрочелик')
async def clear(ctx, *, message):
	count = int(message) + 1
	allow_role = 'Сверхмикрочелик'
	print ('Удалено {c} сообщений.'.format(c = count))
	await ctx.channel.purge(limit = count)

@client.command()
async def giverole(ctx, *, message):
	author = ctx.message.author
	
	user = ctx.message.author
	role = discord.utils.get(user.guild.roles, name = message)
	if (role in allroles):
		await discord.Member.add_roles(user, role)
	else:
		await ctx.send('Роль "{name}" недоступна, либо возникла опечатка.'.format(name = message))
	

"""@client.command()
async def role(ctx):
	member = ctx.author
	game = member.activity[game]
	print(game)
"""
token = os.environ.get('BOT_TOKEN')
client.run(token)
