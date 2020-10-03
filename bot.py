import schoolopy
import yaml
import webbrowser as wb
import discord
import json
from discord.ext import commands

f = open(r'D:\\Microsoft VS Code\\Projects\\Random Python Shit\\Discord Bot for school\\config.yml')
cfg = yaml.load(f, Loader=yaml.FullLoader)

sc = schoolopy.Schoology(schoolopy.Auth(cfg['key'], cfg['secret']))

#print('Your name is %s' % sc.get_me().name_display)
#print(sc.get_assignment(section_id=2733685453, assignment_id=2897150593), output)
assignment = sc.get_assignment(section_id=2733685453, assignment_id=2897150593)
#assignment = json.loads(x)
print(assignment.title, assignment.due)

client = commands.Bot(command_prefix= '/')

@client.event
async def on_ready():
    print('Bot is ready.')
    
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command()
async def assignment(ctx):
    global assignment
    await ctx.send(f'Here is an assignment {assignment.title, assignment.due}')



client.run('NzYxMzk3MDI1NjMwNzE1OTE2.X3aAPA.jPt5ndp91qFz4M9vkBdg4IyAKVY')