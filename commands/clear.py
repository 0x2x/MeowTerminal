import os
import sys
import asyncio

def main():
    """
        :param name: clear
        :param list args: []
        :param str help: Clearing the console
    """
    return os.system('cls' if os.name == 'nt' else 'clear')

main()