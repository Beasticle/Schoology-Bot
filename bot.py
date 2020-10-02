import schoolopy
import yaml
import webbrowser as wb
import discord
from discord.ext import commands

#with open('config.yml', 'r') as f:
 #   cfg = yaml.load(f)

sc = schoolopy.Schoology(schoolopy.Auth('a09fd862af22d4f1d928d79788567eaf05f7682cc', 'c02d5c0b937de605e20691f12af9c213f'))
sc.limit = 10  # Only retrieve 10 objects max

print(sc.get_buildings('butler tech'))

client = commands.Bot(command_prefix= '~')

@client.event
async def on_ready():
    print('Bot is ready.')
    
    
@client.event
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

client.run('NzYxMzk3MDI1NjMwNzE1OTE2.X3aAPA.jPt5ndp91qFz4M9vkBdg4IyAKVY')