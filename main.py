# coding: utf8
import discord
from datetime import datetime, date, time

TRIAL = 617690428057059338
TOKEN_AUTH = "NDIxNjU4OTg5MjQ0NDQ4Nzc4.X0DZVg.uS4Y53WoBmawtUsOSvdkswagTKA"
prekl = 'Осуждаю!'
blacklist = set()


def start():
    client = discord.Client()
    pref = '*'

    @client.event
    async def on_ready():
        print('ready...')
        t = time(0, 0)
        d = date(2004, 1, 24)
        await client.change_presence(activity=discord.Game('жизнь', start=datetime.combine(d, t)))

    @client.event
    async def on_message(ctx):
        text = ctx.content
        print(text)
        # добавление слов в blacklist
        if text.startswith('bl '):
            t = text.lstrip('bl').lstrip().split('; ')
            for word in t:
                if word.lower() not in blacklist:
                    blacklist.add(word.lower())
            print(blacklist)
            await ctx.add_reaction('👍')
            return
        elif text == 'blacklist':
            print(blacklist)
            if len(blacklist) > 0:
                em = discord.Embed()
                em.add_field(name='Blacklist:', value=' '.join(blacklist), inline=False)
                await ctx.channel.send(embed=em)
                return
            else:
                await ctx.channel.send('Blacklist пуст.')
                return
        # удаление слов из blacklist
        elif text.startswith('cbl '):
            t = text.lstrip('cbl').lstrip().split('; ')
            for word in t:
                if word not in blacklist:
                    blacklist.remove(word)
            print(blacklist)
            await ctx.add_reaction('👍')
            return

        elif any(blw in text.lower().split() for blw in blacklist):
            await ctx.channel.send('осуждаю')
            return

    client.run(TOKEN_AUTH, bot=False)


if __name__ == '__main__':
    print('starting')
    start()
    print('exiting')
