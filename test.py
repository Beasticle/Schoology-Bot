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
totalUpdates = []
assignment = sc.get_assignment(section_id=2733685453, assignment_id=3107425856)
assignments = sc.get_assignments(section_id=2733685453)
print(assignment.title)

updates = sc.get_section_updates(section_id=2733685453)
print(updates)

numassignment = -1
for assignment in assignments:
    numassignment = numassignment + 1
    #print(assignments[numassignment].title, assignments[numassignment].due, numassignment)
for update in updates:
    numupdates =+ 1
    totalUpdates.append(updates[numupdates])   
#print(assignments[numassignment].title)
