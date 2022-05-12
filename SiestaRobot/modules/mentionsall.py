import os
import logging
import asyncio

from telethon import Button, TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

from SiestaRobot import telethn as Client

Pake @All buat tag 15.000 member
pake /cancel buat stop tag member

__mod_name__ = "Mentions"
