# language python 
import discord
from discord.ext import commands
import aiohttp

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents) # the command prefix u can change it to anything else.

@bot.command()
async def urban(ctx, *, term):
    try:
        response = requests.get(f'https://api.urbandictionary.com/v0/define?term={term}')
        data = response.json()
        if len(data['list']) > 0:
            definition = data['list'][0]['definition']
            await ctx.send(f"Urban definition of **{term}**: {definition}")
        else:
            await ctx.send(f"- No definition found for **{term}** on Urban Dictionary.")
    except Exception as e:
        await ctx.send(f" `An error occurred: {e}` ")
        await ctx.message.delete()
