import schoolopy
import yaml
import discord
from discord.ext import commands, tasks
from gpiozero import CPUTemperature
import datetime

f = open(r'config.yml')
cfg = yaml.load(f, Loader=yaml.FullLoader)

sc = schoolopy.Schoology(schoolopy.Auth(cfg['key'], cfg['secret']))
sc.limit = 100

assignments = sc.get_assignments(section_id=2733685453)
totalAssignments = []
numassignment = -1
cpu = CPUTemperature()

for assignment in assignments:
    numassignment = numassignment + 1
    totalAssignments.append(assignments[numassignment].title)

message = f'Title: {assignments[numassignment].title}, Due: {assignments[numassignment].due}'

client = commands.Bot(command_prefix= '/')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command()
async def assignment(ctx):
    await ctx.send(f'Here is the most recent assignment, {message}')
    
@client.command()
async def assignments(ctx):
    await ctx.send(f'Here are all {numassignment+1} of your assignments. {totalAssignments}')

@client.command()
async def system(ctx):
    await ctx.send(f'CPU temp is: {cpu.temperature}C')
    
async def background_task():
    await client.wait_until_ready()
    print(cpu.temperature)
    channel = client.get_channel(761395444773027860) # Insert channel ID here
    if datetime.datetime.today().weekday() == 0:
            await channel.send(f'Here is the most current assignment: {message}')

client.loop.create_task(background_task())
client.run('NzYxMzk3MDI1NjMwNzE1OTE2.X3aAPA.jPt5ndp91qFz4M9vkBdg4IyAKVY')