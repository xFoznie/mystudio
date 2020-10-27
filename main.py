from datetime import datetime, time, date

from time import sleep

from config import settings

import discord
from discord.ext import commands

import os


def start():
    bot = commands.Bot(command_prefix=settings['prefix'])

    @bot.event
    async def on_ready():
        print('ready')
        t = time(0, 0)
        d = date(2004, 1, 24)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                            name="за вами!"))

    @bot.event
    @commands.has_permissions(manage_messages=True)
    async def on_message(ctx):
        text = ctx.content
        if text.startswith('erase'):
            if ctx.channel.permissions_for(ctx.author).manage_messages:
                try:
                    t = int(text.lstrip('erase').lstrip())
                    if t > 20:
                        raise ValueError
                    await ctx.channel.purge(limit=t + 1)
                except ValueError:
                    await ctx.channel.send('Слишком большое число!')
                except Exception:
                    await ctx.channel.send('Возникла непредвиденная ошибка!')
            else:
                await ctx.channel.send('Хуй тебе')

        if text == 'call':
            curr = ctx.author.voice.channel
            channels = []
            for i in ctx.guild.voice_channels:
                if i.id != curr.id:
                    channels.append(i)
            try:
                await curr.connect()
            except ClientException:
                bot.voice_clients[0].disconnect()
                await curr.connect()
            
            vc = bot.voice_clients[0]
            for _ in range(10):
                await vc.move_to(curr)
                await vc.move_to(channels[0])

            await vc.disconnect()

    print()
    bot.run(token)


if __name__ == '__main__':
    print('starting')
    token = os.environ.get('BOT_TOKEN')
    start()
