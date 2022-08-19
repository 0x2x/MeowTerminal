from re import A
from utils import parser, theme
from typing import List
console = theme.ColorScheme()

async def main(command):
    """
        :param name: help
        :param list args: [command]
        :param str help: Display help information about the command
    """
    argList:List = []
    try:
        cmd = parser.find_command(command.split(" ")[0])
        args = command.split(maxsplit=1).pop()
    except IndexError:
        cmd = parser.find_command(command)
        args = command.split(maxsplit=1).pop()
    if args.lower() == cmd.get('cmd'):
        args = None
    argList.append(args)
    if cmd.get('result') is True:
        args = parser.args(cmd.get('cmd'), argList)
        await parser.run_command(args.get('cmd'), args.get('args'))
    else:
        console.print(f'[red]COMMAND NOT FOUND:[/red] [underline]{command}[/underline]')

main()