import click
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
from fuzzyfinder import fuzzyfinder



__author__ = 'Neil'
__copyright__ = 'Copyright (C) 2018  Neil'
__license__ = 'GPL v3'
__maintainer__ = 'Neil'
__email__ = 'locateneil@gmail.com'
__status__ = 'Development'
__version__ = '0.1'

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



def create_file_structure(bot_name, bot_dir, dirs):
    '''
    This creates directory structure for the bot.
    '''
    bot_dir = "../bots/"
    new_dir = os.path.join(bot_dir, bot_name)
    if os.path.isdir(new_dir): 
        print("Proposed bot name already exists. Try something else.")
        sys.exit() 
    else: 
        os.mkdir(new_dir)
        for d in dirs:
            os.makedirs(os.path.join(bot_dir, bot_name, d))

#def create_stub_files(bot_name, bot_dir):
  
@click.command()
@click.option('--count', default=1, help='Number.')
@click.option('--name', prompt='Bot name', help='Provide Bot name.')
#@click.option('--type', prompt='Bot type', help='Provide Bot type.')

def newbot(count, name):
    #for x in range(count):
        #click.echo('Hello %s!' % name)
    
    if "_" in name: 
        answer = input("""bot names with '_' are problematic. 
                              Is the name %s instead OK? [Y/n]? """% (name.replace("_", "")))
        if answer in ("Y", "y", "Yes", "yes", "YES"): 
            name = name.replace("_", "")
        else:
            print("Bot creation canceled.")
            exit 
    create_file_structure(name, os.getcwd(), dirs)
    #create_stub_files(name, os.getcwd())
	
    print("Bot created. add relation to this %s bot" % name )


if __name__ == '__main__':
    newbot()