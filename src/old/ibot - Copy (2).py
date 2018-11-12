import time
import click
import shutil
import random
import os 
import sys 
#from jinja2 import Environment, FileSystemLoader
import settings 
from settings import author
from datetime import date
import stat 
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.contrib.completers import WordCompleter
from fuzzyfinder import fuzzyfinder
from win32com.client import Dispatch
import winshell


base_completer = WordCompleter([':create', ':delete', ':clone', ':context', ':parent', ':relation', ':list'])
botype_completer = WordCompleter([':databot', ':metabot'])

BOTKeywords = ['create', 'delete', 'add', 'remove', 'context', 'relation', 'reset']

dirs = [
    'awareness/global/contextual', 
	'awareness/global/temporal', 
	'awareness/global/relational/children', 
	'awareness/global/relational/siblings', 
	'awareness/global/relational/parents', 
    'docs/en/about', 
	'docs/en/commands', 
	'docs/en/NLP', 
    'forks/0/',
    'interface/input', 
    'interface/output', 
    'security/global',
    'security/local',    
    'skills',
    'states/global',
    'states/local',
	'data',
]


def exect(n=3):
    time.sleep(random.randint(1,n))


class BotCompleter(Completer):
    def get_completions(self, document, complete_event):
        yield Completion('completion', start_position=0)

class BotBuilder(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, BOTKeywords)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))



def bot_exist(bot_name, bot_dir):
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        if os.path.isdir(new_dir): 
            return True
   
def create_bot(bot_name, bot_type, bot_dir, dirs):
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        os.mkdir(new_dir)
        for d in dirs:
            os.makedirs(os.path.join(bot_dir, bot_name, d))
        return True

def delete_bot(bot_name, bot_dir):
        
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        
        if os.path.isdir(new_dir): 
            shutil.rmtree(new_dir)
            print('Deleted <'+bot_name+'>')
        else: 
            print(bot_name + " does not exist.")

def clone_bot(bot1, bot2, bot_dir):
        
        bot_dir = "../bots/"
        bot1_dir = os.path.join(bot_dir, bot1)
        bot2_dir = os.path.join(bot_dir, bot2)
        
        if os.path.isdir(bot2_dir): 
            print("Bot with "+ bot2 +" name already exists. Try something else.")
        elif os.path.isdir(bot1_dir): 
            shutil.copytree(bot1_dir, bot2_dir, False, None)
        else: 
            print("Source bot <" + bot1 + "> is missing.")

#create shorcut of bot
def create_relation(self, tool_name, exe_path, startin, icon_path):
        shell = Dispatch('WScript.Shell')
        shortcut_file = os.path.join(winshell.desktop(), tool_name + '.lnk')
        shortcut = shell.CreateShortCut(shortcut_file)
        shortcut.Targetpath = exe_path
        shortcut.WorkingDirectory = startin
        shortcut.IconLocation = icon_path
        shortcut.save()

#def create_stub_files(bot_name, bot_dir):
    



cmd = ''
user_input ='start'

def botCommand(icmd):
    
    #print (icmd)

    if icmd[0]==':create':
        print('Add name for new Bot')
        bot_name = prompt(u'>')        
        #check if bot exist
        while bot_exist(bot_name, os.getcwd()):
            print('Bot already exists. Try another name')
            bot_name = prompt(u'>')
        
        print('What kind of bot it is? <type : for options>')
        bot_type = prompt(u'>', completer=botype_completer)
        print('Creating new '+ bot_type +' named '+ bot_name)
        check = create_bot(bot_name, bot_type, os.getcwd(), dirs)
        if check:
            print(bot_name+bot_type+' created successfully.')
        else:
            print('Error: Could not create '+bot_name+bot_type)

    elif icmd[0]==':delete':
        print('Deleting Bot <'+icmd[1]+'>')
        delete_bot(icmd[1], os.getcwd())
    elif icmd[0]=='clone':
        print('Clonning Bot <'+icmd[1]+'> as <'+icmd[2]+'>')
        clone_bot(icmd[1], icmd[2], os.getcwd())
    elif icmd[0]=='clone':
        print('Clonning Bot <'+icmd[1]+'> as <'+icmd[2]+'>')
        clone_bot(icmd[1], icmd[2], os.getcwd())
        


while 1:
    comd = user_input.split()[:1]
    #print (comd)

    if comd[0]=='create':
        user_input = prompt(u'>')
        
    elif comd[0]=='delete':
        user_input = prompt(u'BOT>',
                            history=FileHistory('commandhistory.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                            completer=BotBuilder(),
                            )
    elif comd[0]=='clone':
        user_input = prompt(u'BOT>',
                            history=FileHistory('commandhistory.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                            completer=BotBuilder(),
                            )
    elif comd[0]=='parent':
        user_input = prompt(u'BOT>',
                            history=FileHistory('commandhistory.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                            completer=BotBuilder(),
                            )    
    else:
        # print('Commands:\n\tcreate <bot> as databot' +
        # '\n\tdelete <bot>'+
        # '\n\tclone <bot> <newbot>'+
        # '\n\tcontext <bot1>'+
        # '\n\tparent <parentBot> : <childBot> <childBot> .. <childBot>'+
        # #'\n\tchild <child> : <parent>'+
        # #'\n\tsibling <bot> : <bot> : <bot> : <bot>'+
        # '\n\trelation <bot> : <bot>'+
        # '\n\texplore <bot>'+
        # '\n\tlist all'+
        # '\n\treset <bot>')

        #user_input = prompt(u'BOT>', completer=BotBuilder(),)
        #user_input = prompt('BOT> ', completer=BotCompleter())
        print('Express your command <type : for options>')
        user_input = prompt(u'BOT>', completer=base_completer)

    botCommand(user_input)


