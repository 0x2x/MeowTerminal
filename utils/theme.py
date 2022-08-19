import json
from rich.console import Console
from rich.theme import Theme

with open('config/settings.json', 'r') as config:
    settings = json.load(config)

def ColorScheme():
    theme = settings.get('theme')
    if theme == 'default':
        custom_theme = Theme({
            "info": "dim cyan",
            "warning": "magenta",
            "danger": "bold red"
        })
        console = Console(theme=custom_theme)
        return console
    elif theme == 'dracula':
        custom_theme = Theme({

        })
        console = Console(theme=custom_theme)
        return console
    else:
        return 



