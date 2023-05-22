import discord
from discord.ext import commands

intents = discord.Intents.default()  # crée une instance de discord.Intents avec les valeurs par défaut
intents.message_content = True  # active l'intention "Privileged message content"

TOKEN = ''# mettre son token

bot = commands.Bot(command_prefix='$', intents=intents)  # passe les 'intents' à la création du bot

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(TOKEN)
