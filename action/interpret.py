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

def interprete(ff_qry):
    words = ff_qry.split(";")
    cmds = valid_commands(words)
    print(cmds)
    if(len(cmds)):
        for cmd in cmds:
            if(command(cmd)):
                command(cmd)
            else:
                print(cmd + " command not found..")
    return 1


