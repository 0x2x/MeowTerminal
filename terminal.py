import os
import sys
import asyncio
import pathlib
import datetime
from utils import timeutil, parser, theme, startup
from typing import (List, Union)

class terminal():
    def __init__(self) -> None:
        self.path = None
        self.time = datetime.datetime.utcnow().timestamp()
        
    def MainFolder(self):
        try:
            self.path = sys.argv[1]
        except IndexError:
            self.path = os.path.abspath(os.path.join(os.path.basename(__file__), "../../"))

    async def start(self):
        console = theme.ColorScheme()
        self.MainFolder()
        console.print(startup.Startup.start_print())
        while(True):
            argList:List = []
            current_time = timeutil.get_epochtime_ms(self.time)
            path = os.path.basename(self.path)
            design = parser.command_design(file_directory=path, time=current_time)
            console.print(design, end='')
            value = input()
            value = value.strip()
            if value != "":
                try:
                    cmd = parser.find_command(value.split(" ")[0])
                    args = value.split(maxsplit=1).pop()
                except IndexError:
                    cmd = parser.find_command(value)
                    args = value.split(maxsplit=1).pop()
                if args.lower() == cmd.get('cmd'):
                    args = None
                argList.append(args)
                if cmd.get('result') is True:
                    args = parser.args(cmd.get('cmd'), argList)
                    await parser.run_command(cmd.get('file'), args.get('cmd'), args.get('args'))
                else:
                    def find_closes_command(cmd:str):
                        path = pathlib.Path(r"./commands")
                        for elem in path.rglob("*.py"):
                            filename = str(elem).split('\\')[-1].split(".")[0]
                            if cmd.lower() in filename.lower():
                                return filename
                        return None
                    command = find_closes_command(value)
                    if command is not None:
                        console.print(f'[red]COMMAND NOT FOUND[/red]@[blue]perhaps did you mean the command:[/blue] [white bold]{command}[/white bold]: [underline]{value}[/underline]')
                    else:
                        console.print(f'[red]COMMAND NOT FOUND:[/red] [underline]{value}[/underline]')

term = terminal()
asyncio.run(term.start())