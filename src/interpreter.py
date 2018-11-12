import time
from datetime import datetime
from datetime import date
import click
import shutil
import random
import os 
import sys 
from os import walk
import stat 
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.contrib.completers import WordCompleter
from os import walk
from commands import command


interpretes_dir = "../core/commands/"

bot_dir = "../bots/"
commands_dir = "../core/commands/"
relations_dir = "../core/relations/"
objects_dir = "../core/objects/"

iInterfacePath = "/interface/input/"
oInterfacePath = "/interface/output/"
temporalPath = "/awareness/temporal/"
relationalPath = "/awareness/relational/"
contextualPath = "/awareness/contextual/"



def valid_commands(words):
    cmds = os.listdir(interpretes_dir)
    match = set(words).intersection(cmds)
    return match

def valid_relations(words):
    cmds = os.listdir(relations_dir)
    match = set(words).intersection(cmds)
    return match    

def valid_objects(words):
    cmds = os.listdir(objects_dir)
    match = set(words).intersection(cmds)
    return match    

def valid_bots(words):
    cmds = os.listdir(bot_dir)
    match = set(words).intersection(cmds)
    return match        





def create_bot(bot_name, bot_type, bot_dir, dirs):
    bot_dir = "../bots/"
    new_dir = os.path.join(bot_dir, bot_name)
    os.mkdir(new_dir)
    for d in dirs:
        os.makedirs(os.path.join(bot_dir, bot_name, d))
    return True


def list_bots():
    bot_dir = "../bots/"
    
    for d in dirs:
        os.makedirs(os.path.join(bot_dir, bot_name, d))
    return True

def interprete(ff_qry):
    words = ff_qry.split(";")
    cmds = valid_commands(words)
    #rels = valid_relations(words)
    #objs = valid_objects(words)
    #bots = valid_bots(words)

    if(len(cmds)):
        for cmd in cmds:
            if(command(cmd)):
                command(cmd)
    
    return 1


def free_interprete(ff_qry):
    bot_dir = "../bots/"
    if(ff_qry=='resolve person'):
        qry1(ff_qry)
    if(ff_qry=='resolve person 600'):
        qry2(ff_qry)
    if(ff_qry=='resolve company'):
        qry3(ff_qry)
    if(ff_qry=='resolve customer'):
        qry4(ff_qry)
    if(ff_qry=='resolve customer 1'):
        qry4_1(ff_qry)
    if(ff_qry=='resolve customer 600'):
        qry4_5(ff_qry)
    if(ff_qry=='create customer as metabot'):
        qry5(ff_qry)
    if(ff_qry=='create metabot as customer'):
        qry5(ff_qry)
    if(ff_qry=='customer is person'):
        qry6(ff_qry)
    if(ff_qry=='customer is like person'):
        qry6(ff_qry)
    if(ff_qry=='customer is company'):
        qry7(ff_qry)
    if(ff_qry=='analyse bots'):
        qry8(ff_qry)
    if(ff_qry=='analyse bots temporal'):
        qry8_1(ff_qry)
    if(ff_qry=='analyse bots relational'):
        qry8_2(ff_qry)
    if(ff_qry=='customer interface as container'):
        qry11(ff_qry)
    if(ff_qry=='customer interface as form'):
        qry11(ff_qry)
    if(ff_qry=='build customer interface'):
        qry12(ff_qry)
    if(ff_qry=='build customer interface 600'):
        qry12_1(ff_qry)
    if(ff_qry=='interface dob as date'):
        qry13(ff_qry)
    if(ff_qry=='dob interface as date'):
        qry13(ff_qry)
    if(ff_qry=='interface dob as text'):
        qry14(ff_qry)
    if(ff_qry=='dob interface as text'):
        qry14(ff_qry)
    


def qry1(ff_qry):
    print('resolving person bot')
    exect(2)
    print('analysing person scope')
    exect(3,1)
    print('[firstname]')
    exect(1,1)
    print('[lastname]')
    exect(1,1)
    print('[address]')
    exect(2,1)
    print('[city]')
    exect(2,1)
    print('[state]')
    exect(3,1)
    print('[zip]')
    exect(6,3)
    print('[country]')
    exect(10,5)
    print('warning: max exec time exceeded.')
    exect(1,1)
    print('terminating..')

def qry2(ff_qry):    
    print('resolving person bot')
    exect(2)
    print('analysing person scope')
    exect(3,1)
    print('[firstname]')
    exect(1,1)
    print('[lastname]')
    exect(1,1)
    print('[address]')
    exect(2,1)
    print('[city]')
    exect(2,1)
    print('[state]')
    exect(3,1)
    print('[zip]')
    exect(4,3)
    print('[country]')
    exect(5,3)
    print('[dob]')
    exect(6,3)
    print('[phone]')
    exect(8,4)
    print('[email]')
    exect(10,5)
    print('warning: max exec time exceeded.')
    exect(1,1)
    print('terminating..')

def qry3(ff_qry):
    print('resolving company bot')
    exect(2)
    print('analysing company scope')
    exect(3,1)
    print('[name]')
    exect(1,1)
    print('[registration]')
    exect(1,1)
    print('[address]')
    exect(2,1)
    print('[city]')
    exect(2,1)
    print('[state]')
    exect(3,2)
    print('[website]')
    exect(5,3)
    print('warning: max exec time exceeded.')
    exect(1,1)
    print('terminating..')

def qry4(ff_qry):
    print('resolving customer bot')
    exect(2)
    handle_valid = bot_exist('customer')
    if handle_valid:
        handle_valid2 = rel_exist('customer')
        if handle_valid2:
            free_interprete('resolve customer 600')
        else:
            free_interprete('resolve customer 1')
    else:
        print('warning: customer not found')
        exect(1,1)
        print('terminating..')

def qry4_1(ff_qry):
    exect(2)
    handle_valid = bot_exist('customer')
    if handle_valid:
        print('Resolving customer relation')
        exect(5,3)
        print('No relation defined for Customer')
        exect(1,1)
        print('terminating..')
    else:
        print('warning: customer not found')
        exect(1,1)
        print('terminating..')

def qry4_4(ff_qry):
    print('resolving customer bot')
    exect(2)
    handle_valid = bot_exist('customer')
    if handle_valid:
        print('resolving customer <> person')
        qry1('resolve person')
    else:
        print('warning: customer not found')
        exect(1,1)
        print('terminating..')   

def qry4_5(ff_qry):
    print('resolving customer bot')
    exect(2)
    handle_valid = bot_exist('customer')
    if handle_valid:
        print('resolving customer <> person')
        qry2('resolve person')
    else:
        print('warning: customer not found')
        exect(1,1)
        print('terminating..')        
			
def qry5(ff_qry):
    print('Creating Metabot')
    exect(1)
    clone_bot('test', 'customer')
    exect(1,1)
    print('initalizing resolve')
    exect(3,1)
    print('resolving customer bot')
    exect(1)
    print('resolve finished.')

def qry5_5(ff_qry):
    print('Re-configuring customer')
    exect(3,2)
    clone_bot('xe', 'customer')
    exect(3,1)
    print('initalizing resolve')
    exect(3,1)
    print('resolving customer bot')
    exect(1)
    print('resolve finished.')

def qry6(ff_qry):
    print('checking rel bots')
    exect(2)
    print('[customer][person] bots validated')
    exect(5,3)
    print('"is" relation validated')
    exect(2)
    print('timestamp updated')
    exect(4)
    print('relation updated')
    exect(1)
    dele = delete_bot('customer')
    exect(10,10)
    if(dele):
        qry5_5('re-issue customer')


def qry7(ff_qry):
    print('checking bots')
    exect(2)
    print('[customer][company] bots valid')
    exect(5,3)
    print('"has" relation validated')
    exect(2)
    print('timestamp updated')
    exect(4)
    print('relation updated')

def qry8(ff_qry):
    bots = os.listdir(bot_dir)
    for bot in bots:
        print(' analysing '+bot, end=',')
        exect(1)
    print('\n')
    return 1    

def qry8_1(ff_qry):
    bots = os.listdir(bot_dir)
    for bot in bots:
        print(' analysing temporal for '+bot, end=',')
        exect(1)
    print('\n')
    return 1    

def qry8_2(ff_qry):
    bots = os.listdir(bot_dir)
    for bot in bots:
        print(' analysing relation for '+bot, end=',')
        exect(1)
    print('\n')
    return 1    

def qry10(ff_qry):
    pass
def qry11(ff_qry):
    print('resolving customer bot')
    exect(2)
    handle_valid = bot_exist('customer')
    if handle_valid:
        print('adding container interface')
        handle = add_interface('customer', 'container')
        if(handle):
            print('container interface added to customer')
        else:
            print('unexpected error')
    else:
        print('bot missing ')        

def qry12(ff_qry):
    
    qry4_4(ff_qry)
    #qry2(ff_qry)
    exect(2)
    print('.')
    exect(5,3)
    print('.')
    exect(3)
    print('.')
    exect(2)
    print('fetching child interfaces')
    exect(4)
    print('warning: type undefined')
    exect(1)
    print('generating container')
    exect(10,5)
    print('success..')
    shutil.copyfile('vz.html', bot_dir+'customer'+iInterfacePath+'container/container.html')
    exect(1)
    print('timestamp updated')
    exect(1)
    print('terminating..')

def qry12_1(ff_qry):
    qry4_5(ff_qry)
    exect(2)
    print('.')
    exect(5,3)
    print('.')
    exect(3)
    print('.')
    exect(2)
    print('fetching child interfaces')
    exect(4)
    print('warning: type undefined')
    exect(1)
    print('generating container')
    exect(10,5)
    print('success..')
    shutil.copyfile('vz600.html', bot_dir+'customer'+iInterfacePath+'container/container.html')
    exect(1)
    print('timestamp updated')
    exect(1)
    print('terminating..')

def qry12_2X(ff_qry):
    qry4_5(ff_qry)
    exect(2)
    print('.')
    exect(5,3)
    print('.')
    exect(3)
    print('.')
    exect(2)
    print('fetching child interfaces')
    exect(4)
    print('warning: type undefined')
    exect(1)
    print('generating container')
    exect(10,5)
    print('success..')
    shutil.copyfile('vz600.html', bot_dir+'customer'+iInterfacePath+'container/container.html')
    exect(1)
    print('timestamp updated')
    exect(1)
    print('terminating..')

def qry12_1(ff_qry):
    qry4_5(ff_qry)
    exect(2)
    print('.')
    exect(5,3)
    print('.')
    exect(3)
    print('.')
    exect(2)
    print('fetching child interfaces')
    exect(4)
    print('warning: type undefined')
    exect(1)
    print('generating container')
    exect(10,5)
    print('success..')
    tp = interface_check('dob')
    if(tp=='date'):
        shutil.copyfile('vz601.html', bot_dir+'customer'+iInterfacePath+'container/container.html')
    else:
        shutil.copyfile('vz600.html', bot_dir+'customer'+iInterfacePath+'container/container.html')
    exect(1)
    print('timestamp updated')
    exect(1)
    print('terminating..')


def qry13(ff_qry):
    print('resolving dob bot')
    exect(2)
    handle_valid = bot_exist('dob')
    if handle_valid:

        handle = add_interface('dob', 'date')
        if(handle):
            print('date interface added to dob')
        else:
            print('unexpected error')
    else:
        print('bot missing ')        

def qry14(ff_qry):
    print('resolving dob bot')
    exect(2)
    handle_valid = bot_exist('dob')
    if handle_valid:
        handle = add_interface('dob', 'text')
        if(handle):
            print('date interface added to dob')
        else:
            print('unexpected error')
    else:
        print('bot missing ')       

def qry15(ff_qry):
    pass
def qry16(ff_qry):
    pass
def qry17(ff_qry):
    pass
def qry18(ff_qry):
    pass
def qry19(ff_qry):
    pass
def qry20(ff_qry):
    pass



def exect(n=3, p=1):
    time.sleep(random.randint(p,n))
    

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




def bot_exist(bot_name):
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        if os.path.isdir(new_dir): 
            return True

def rel_exist(bot_name):
        bot_dir = "../bots/"
        botrel = bot_dir + bot_name + relationalPath
        rels = os.listdir(botrel)
        if(len(rels)):
            print('relation validated')
            return True

def delete_bot(bot_name):
        bot_dir = "../bots/"
        new_dir = os.path.join(bot_dir, bot_name)
        
        if os.path.isdir(new_dir): 
            shutil.rmtree(new_dir)
            #print('Bot <'+bot_name+'> deleted successfully..')
            return True
        else: 
            print(bot_name + " does not exist.")


def add_interface(bot, iname):
    bot_dir = "../bots/"+bot+"/interface/input/"
    fl = interface_check(bot)
    #os.rmdir(bot_dir+fl)
    

    new_dir = os.path.join(bot_dir, iname)
    os.mkdir(new_dir)
    return True

def interface_check(bot):
    bot_dir = "../bots/"+bot+"/interface/input/"
    obs = os.listdir(bot_dir)
    for o in obs:
        if (o=='date'):
            return 'date'
        else:
            return 'text'



def find_relations(bot_name):
    
    botrel = bot_dir + bot_name + relationalPath
    rels = os.listdir(botrel)
    print(rels)
    bots = list()
    
    (dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
    ts = dt+'.'+micro
    
    if(len(rels)):
        for rel in rels:
            obs = os.listdir(botrel + rel + '/')
            bots.append(obs)
            print(obs, ts)
    return bots    