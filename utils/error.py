from rich.console import Console
console = Console()
class CommandNotFound(Exception):
    """If the command does not exist"""

class ErrorWhileRunning(Exception):
    def error(self, command, error):
        console.print(f'[bold red]I could not process command[/bold red]: {command} # {error}')
