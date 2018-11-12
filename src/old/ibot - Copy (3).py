import time
from datetime import datetime
from datetime import date
import click
import shutil
import random
import os 
import sys 
#from jinja2 import Environment, FileSystemLoader
import settings 
from settings import author
import stat 
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.contrib.completers import WordCompleter
from os import walk
from fuzzyfinder import fuzzyfinder
from win32com.client import Dispatch
import winshell

bot_path = '../bots'
temporalPath = "/awareness/global/temporal/"
relationalPath = "/awareness/global/relational/"
contextualPath = "/awareness/global/contextual/"

BOTKeywords = ['create', 'delete', 'add', 'remove', 'context', 'relation', 'reset']

relation_type = ['is a', 'has a', 'is', 'has', 'part of', 'type of', 'kind of', 'attribute of', 'piece of', 'member of', 'is like']
#relation_type = [':is a', ':has a', ':is', ':has', ':part of', ':type of', ':kind of', ':attribute of', ':piece of', ':member of', ':is like']
relation_completer = WordCompleter(['is a', 'has a', 'is', 'has', 'part of', 'type of', 'kind of', 'attribute of', 'piece of', 'member of', 'is like'])

base_completer = WordCompleter([':create', ':delete', ':clone', ':define', ':analyse', ':list', ':freeform'])
bottype_completer = WordCompleter([':databot', ':metabot',':relationbot'])
deleter_completer = WordCompleter([':list'])
cloner_completer = WordCompleter([':list'])


define_completer = WordCompleter([':relation', ':context'])
#relation_completer = WordCompleter([':inherited', ':composited', ':associative', ':aggregative'])



bot_dir = "../bots/"
bots = os.listdir(bot_dir)
#bots = bots + relation_type
vbots = WordCompleter(bots)

global_cmd = ''

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





class BotBuilder(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=False)
        #relation_type
        #print(bots)
        matches = fuzzyfinder(word_before_cursor, bots)
        #print(word_before_cursor)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))



class BotBuilderX(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, BOTKeywords)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))

def switch(icmd, param1, param2, param3):
    return {
        ':list': list_bots(),
        ':exist': bot_exist(param1)
    }.get(icmd, False)

#def isValidCmdx(icmd):

def validate_input(icmd):
    if ':' in icmd:
        return 'command'
    else:
        handle_valid = bot_exist(icmd, os.getcwd())
        if handle_valid:
            return 'bot'
    return False

def list_bots():
        bot_dir = "../bots/"
        bots = os.listdir(bot_dir)
        for bot in bots:
            print('['+bot, end=']')
        print('\n')




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
                global_cmd = user_input
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

def handle_relation(cmd=''):
        #[':inherited', ':composited', ':associative', ':aggregative'])
        if cmd=='-ex':
            print('Relation Types:')
            print('\tInheritance: “Apple is a fruit”, “Ferrari is a car”, "Customer is a person"')
            print('\tComposited: “Engine is partof Suzuki”, “Suzuki is a typeof Car”, "Company is a kindof lead"')
            print('\tAssociative: “Company has employees”, "Milestones have tasks"')
            print('\tAggregative: “Person has a name”, "Task has a enddate"')
        #user_input = prompt('relation> ', completer=BotCompleter())
        print('Define Relations: type -ex for examples')
        user_input = prompt(u'Bot>',completer=BotBuilder(),)
        bot1 = user_input
        if user_input=='-ex':
            handle_relation('-ex')
        
        user_input = prompt(u'Relation>',completer=relation_completer)
        relation = user_input
        if user_input=='-ex':
            handle_relation('-ex')
        
        user_input = prompt(u'Bot>',completer=BotBuilder(),)
        bot2 = user_input
        if user_input=='-ex':
            handle_relation('-ex')
        
        print('Relation Query: '+bot1+' '+relation+' '+bot2)
        user_input = prompt(u'Apply? y, n>')
        if user_input=='y':
            create_relation(bot1, bot2, relation)
            print(bot1 + ' ' + relation + ' ' + bot2 + ' relation is created.')
        elif user_input=='n':
            print('Cancelled')
        
        user_input = prompt(u'Add another Relation? y, n>')
        if user_input=='y':
            handle_relation()
        
        

def bot_exist(bot_name):
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

def delete_bot(bot_name):
        
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        
        if os.path.isdir(new_dir): 
            shutil.rmtree(new_dir)
            print('Bot <'+bot_name+'> deleted successfully..')
        else: 
            print(bot_name + " does not exist.")

def clone_bot(bot1, bot2):
        
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
#def create_relation(self, tool_name, exe_path, startin, icon_path):

def create_relation(bot1, bot2, relation):
    tempo = []
    bot_dir = "../bots/"
    fp = bot_dir + bot1 + relationalPath
    
    b1 = fp+'/' + relation
    b2 = bot_dir + bot2

    #tempo.append(bot_dir + bot1 + temporalPath)
    #tempo.append(bot_dir + bot2 + temporalPath)

    #if not os.path.exists(fp):
    if not os.path.isdir(fp+'/' + relation + '/' +bot2): 
        os.makedirs(os.path.join(fp, relation, bot2))
        
        # os.symlink(b2, b1)

        # shell = Dispatch('WScript.Shell')
        # shortcut_file = os.path.join(winshell.desktop(), bot2 + '.lnk')
        # shortcut = shell.CreateShortCut(shortcut_file)
        # shortcut.Targetpath = fp
        # shortcut.WorkingDirectory = fp
        # shortcut.save()
    
    addTimestamp(bot1)
    addTimestamp(bot2)

def ff_interpreter(txt):
    qry = txt.split(' ')
    for q in qry:
        print(q)

cmd = ''
user_input ='start'

def addTimestamp(bot):
    bot_dir = "../bots/" + bot + temporalPath
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
    ts = dt+'.'+micro
    f= open(bot_dir+ts,"w+")

def freeformQuery():
    print('Write freeform: eg. <person has name>')
    user_input = prompt(u'FF>')
    ff_interpreter(user_input)  
 #   print(user_input)



def botCommand(icmd):    
    #print (icmd)
    if icmd==':create':
        print('Provide name for new Bot')
        user_input = handle_exist(cloner_completer)
        print('What kind of bot it is? <type : for select from option>')
        bot_type = prompt(u'>', completer=bottype_completer)

        print('Creating new '+ bot_type +' named '+ user_input)
        check = create_bot(user_input, bot_type, os.getcwd(), dirs)
        if check:
            addTimestamp(user_input)
            print(user_input+bot_type+' created successfully.')
        else:
            print('Error: Could not create '+user_input+bot_type)

    elif icmd==':delete':
        #print('<Delete> bot called')
        print('Provide name for Bot you wish to delete. or type : for options')
        user_input = handle_valid(deleter_completer)
        delete_bot(user_input)
        
    elif icmd==':clone':
        print('Which Bot you want to clone? type : for options')
        sourceBot = handle_valid(cloner_completer)
        print('Name for clone bot')
        cloneBot = handle_exist(cloner_completer)
        print(sourceBot +' == '+ cloneBot)
        clone_bot(sourceBot, cloneBot)

    elif icmd==':list':
        print('List of available bots')
        list_bots()
    elif icmd==':freeform':
        freeformQuery()         
    elif icmd==':define':
        print('Type : for Defition types')
        def_type = prompt(u'>', completer=define_completer)
        print(def_type)
        if def_type==':relation':
            #print('Type : to select Relationship types')
            handle_relation()
            #rel_type = prompt(u'>', completer=relation_completer)

        elif def_type==':context':
            print('Type : to select Relationship types')
            context = prompt(u'>')
        else:
            pass
    else:
        print(icmd + ' command is invalid')


while 1:

    print('Command <type : to list of command bots>')
    user_input = prompt(u'BOT>', completer=base_completer)
    botCommand(user_input)


