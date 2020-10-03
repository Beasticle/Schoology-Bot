import schoolopy
import yaml
#import webbrowser as wb
#import discord
#import json
#from discord.ext import commands

f = open(r'D:\\Microsoft VS Code\\Projects\\Random Python Shit\\Discord Bot for school\\config.yml')
cfg = yaml.load(f, Loader=yaml.FullLoader)

sc = schoolopy.Schoology(schoolopy.Auth(cfg['key'], cfg['secret']))
sc.limit  = 100

assignment = sc.get_assignment(section_id=2733685453, assignment_id=3107425856)
assignments = sc.get_assignments(section_id=2733685453)
print(assignment.title)

numassignment = 0
for assignment in assignments:
    numassignment = numassignment + 1
    print(assignments[numassignment].title, assignments[numassignment].due, numassignment)
