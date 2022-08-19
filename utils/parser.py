from ast import Call
import os
import sys
import inspect
import pathlib
import json
import re
from docstring_parser import parse
from functools import wraps
from typing import Callable, List
from utils import error

def find_command(command:str):
    path = pathlib.Path(r"./commands")
    for elem in path.rglob("*.py"):
        filename = str(elem).split('\\')[-1].split(".")[0]
        if filename.lower() == command.lower():
            file = open(elem, "r")
            if """def main""" or """async def main""" in file.read():
                return dict(result=True, cmd=command, cog=file, file=elem)
    return dict(result=False, cmd=None, cog=None)

def args(command:str, args:List=None):
    return dict(cmd=command, args=args)

def document_parser(content:str):
    cmd_doc = parse(content)
    return dict(command=cmd_doc.params[0].description, required_args=cmd_doc.params[1].description, help=cmd_doc.params[2].description)


def get_args(arg_list):
    return arg_list

async def run_command(path, command:str, args:List=None):
    try:

        if args[0] is None:
            """
                Running the command with no arguments
            """
            exec(open(f"{path}").read())
 

            # if command == 'clear':
            #     document = clear.main.__doc__
            #     clear.main()
            #     print(document_parser(document))
            
        else:
            """
                Running the command with arguments
            """
            print(command, args)
            # run the cmd with args
            return
    except Exception as e:
        raise error.ErrorWhileRunning().error(command, e)
        
def out_of_list(columns: List, selection: int):
    try:
        return columns[selection]
    except BaseException:
        return None

with open('config/settings.json', 'r') as config:
    settings = json.load(config)

def command_design(file_directory, time):
    def parser(content:str):
        #emojis
        content = content.replace(":dracula:", "%s" % ("🧛‍♂️"))
        content = content.replace(":gun:", "%s" % ("🔫"))

        #variables
        content = content.replace("{path}", "%s" % (file_directory))
        content = content.replace("{time}", "%s" % (time))
        
        #styles
        content = content.replace("{text.bold}", "%s" % ("[bold]"))
        content = content.replace("{text.bold.stop}", "%s" % ("[/bold]"))
        content = content.replace("{text.underline}", "%s" % ("[underline]"))
        content = content.replace("{text.underline.stop}", "%s" % ("[/underline]"))
        content = content.replace("{text.dim}", "%s" % ("[dim]"))
        content = content.replace("{text.dim.stop}", "%s" % ("[/dim]"))
        content = content.replace("{text.bright}", "%s" % ("[bright]"))
        content = content.replace("{text.bright.stop}", "%s" % ("[/bright]"))
        content = content.replace("{text.code}", "%s" % ("[bold reverse]"))
        content = content.replace("{text.code.stop}", "%s" % ("[/bold reverse]"))
        content = content.replace("{text.italic}", "%s" % ("[italic]"))
        content = content.replace("{text.italic.stop}", "%s" % ("[/italic]"))
        content = content.replace("{text.reverse}", "%s" % ("[reverse]"))
        content = content.replace("{text.reverse.stop}", "%s" % ("[/reverse]"))
        content = content.replace("{text.strike}", "%s" % ("[strike]"))
        content = content.replace("{text.strike.stop}", "%s" % ("[/strike]"))
        content = content.replace("{text.blink}", "%s" % ("[blink]"))
        content = content.replace("{text.blink.stop}", "%s" % ("[/blink]"))
        content = content.replace("{text.blink2}", "%s" % ("[blink2]"))
        content = content.replace("{text.blink2.stop}", "%s" % ("[/blink2]"))

        #colors
        content = content.replace("{red.text}", "%s" % ("[red]"))
        content = content.replace("{red.text.stop}", "%s" % ("[/red]"))
        content = content.replace("{black.text}", "%s" % ("[black]"))
        content = content.replace("{black.text.stop}", "%s" % ("[/black]"))
        content = content.replace("{blue.text}", "%s" % ("[blue]"))
        content = content.replace("{blue.text.stop}", "%s" % ("[/blue]"))
        

        #schemes
        content = content.replace("{warning}", "%s" % ("[warning]"))
        content = content.replace("{warning.stop}", "%s" % ("[/warning]"))
        content = content.replace("{danger}", "%s" % ("[danger]"))
        content = content.replace("{danger.stop}", "%s" % ("[/danger]"))
        content = content.replace("{info}", "%s" % ("[info]"))
        content = content.replace("{info.stop}", "%s" % ("[/info]"))

        if "{git}" or "{github}" in content:
            github_file = "a"
            content = content.replace("{git}" or "{github}", "%s" % (github_file))
        output = content
        return output
        
    if settings.get('cmdline') == "":
        return parser('☕ [center][grey]{path}[/grey] in {time} [blue]$[/blue][/center]')

    return parser(settings.get('cmdline'))
