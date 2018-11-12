import time
from datetime import datetime
from datetime import date
import click
import shutil
import random
import os 
import sys 
import stat 
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
#from prompt_toolkit.contrib.completers import WordCompleterselect
from os import walk
#from fuzzyfinder import fuzzyfinder




bot_dir = "../bots/"
commands_dir = "../core/commands/"
relations_dir = "../core/relations/"
objects_dir = "../core/objects/"

temporalPath = "/awareness/temporal/"
relationalPath = "/awareness/relational/"
contextualPath = "/awareness/contextual/"



dirs = [
    'awareness/contextual', 
	'awareness/temporal', 
	'awareness/relational', 
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


def command(cmd):
    print('entering '+cmd+' mode...')
    eval(cmd+'()')



# def create(user_input = ''):
#     print('Databot <1> or Metabot <2>')
#     cmds = os.listdir(commands_dir+'create/')
#     user_input = prompt(u'create>')
    
#     if(user_input=='1'):
#         print('Provide Name for Databot')
#         bot_name = prompt(u'name>')
#         createDatabot(bot_name)
#     elif (user_input=='2'):
#         print('Provide Name for Metabot')
#         bot_name = prompt(u'name>')
#         createMetabot(bot_name)
    
#     print('Continue create mode?')
#     user_input = prompt(u'y or n>')
#     if(user_input=='y'):
#         create('')
#     else:
#         pass


