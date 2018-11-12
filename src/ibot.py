import click
import os 
import sys 
from os import walk
from prompt_toolkit import prompt
from interpret import interprete

from commands import command

bot_path = '../bots'
temporalPath = "/awareness/temporal/"
relationalPath = "/awareness/relational/"
contextualPath = "/awareness/contextual/"


cmd = ''
user_input ='start'



bot_dir = "../bots/"
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
    

def handle_valid(_completer):
        bot_dir = "../bots/"
        user_input = prompt(u'>', completer=_completer)
        new_dir = ''
        #check if command
        if(':' in user_input): 
            botCommand(user_input)
            print('Enter Bot name or type : for options')
            handle_valid(_completer)
        else:
            new_dir = os.path.join(bot_dir, user_input)
            if os.path.isdir(new_dir): 
                #global_cmd = user_input
                return user_input
            else:
                print('No bot named '+user_input + ' found, try something else.')
                handle_valid(_completer)
            
def handle_exist(_completer):
        bot_dir = "../bots/"
        user_input = prompt(u'>', completer=_completer)
        new_dir = os.path.join(bot_dir, user_input)
        if os.path.isdir(new_dir): 
            print('bot named '+user_input + ' already exist, try new name')
            handle_exist(_completer)
        else:
            return user_input



#create shorcut of bot
#def create_relation(self, tool_name, exe_path, startin, icon_path):


def freeformQuery():
    user_input = prompt(u'iBot>')
    cli_interpreter(user_input)
    freeformQuery()





def botCommand(icmd):    
    #print (icmd)
    
    if icmd==':help':
        print('Start typing')
        help()    
    if icmd==':cli':
        print('Start typing')
        freeformQuery()         
    else:
        print(icmd + ' command is invalid')


while 1:

    print('Command <type : to list of command bots>')
    user_input = prompt(u'BOT>')
    botCommand(user_input)


