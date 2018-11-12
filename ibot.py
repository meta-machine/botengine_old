import click
import os 
import sys 
from os import walk
from prompt_toolkit import prompt
from action.interpret import interprete
from action.commands import command


bot_path = './bots'
temporalPath = "/awareness/temporal/"
relationalPath = "/awareness/relational/"
contextualPath = "/awareness/contextual/"


cmd = ''
user_input ='start'



bot_dir = "./bots/"
bots = os.listdir(bot_dir)

dirs = [
    'awareness/contextual', 
	'awareness/temporal', 
	'awareness/relational', 
    'communication', 
    'function',
    'state',
	'data',
    'docs/en', 
	'forks',
    'interface/input', 
    'interface/output', 
    'security/global',
    'security/local',    
]




def cli_interpreter(ff_query):
    interprete(ff_query)
    

def queryLoop():
    user_input = prompt(u'iBot>')
    cli_interpreter(user_input)
    queryLoop()

def botCommand(icmd):    
    #print (icmd)
    
    if icmd==':help':
        print('Start typing')
        help()    
    if icmd==':cli':
        print('Start typing')
        queryLoop()         
    else:
        print(icmd + ' command is invalid')
while 1:

    print('Command <type : to list of command bots>')
    user_input = prompt(u'BOT>')
    botCommand(user_input)


