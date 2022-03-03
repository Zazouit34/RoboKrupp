# Wikibotia - discord bot that searches Wikipedia for you.

import os

import wikipediaapi as wi
from discord.ext import commands



TOKEN = 'OTI4NDMwMTk1NzEzNjcxMjQ5.YdYqAA.YkiTkHjKImz2lUgO2zNCnnBux5o'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='w', aliases=['wiki', 'wikipedia'], help='Searches a term in wikipedia.org. Returns a short note & url.')
async def w(ctx, *args):

    # handling language flag
    args = list(args)
    if args[0][0] == '-':
        language = args[0][1:]
        args.pop(0)
    else:
        language = 'en'

    # searching for a wikipedia page
    wikipedia = wi.Wikipedia(language)
    term = ' '.join(args).title()
    page = wikipedia.page(term)

    # get only first section of an article
    if page.exists():
        end = page.summary.find('\n')
        await ctx.send(page.summary[:end])
        await ctx.send('You can read more here: ' + page.fullurl)
    else:
        await ctx.send(f"I'm sorry, I couldn't find it in this language -> {language}. Try different language or term.")


bot.run(TOKEN)
