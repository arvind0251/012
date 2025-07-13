from ... import console
from pyrogram import filters
from typing import Union, List


def commandx(commands: Union[str, List[str]]):
    # use explicit keyword so future Pyrogram changes don’t break
    return filters.command(commands, prefixes=console.COMMAND_PREFIXES)


def commandz(commands: Union[str, List[str]]):
    # same idea but with your secondary prefix/handler set
    return filters.command(commands, prefixes=console.COMMAND_HANDLERS)
