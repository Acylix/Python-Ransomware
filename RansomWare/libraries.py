from cryptography.fernet import Fernet
from win32api import GetSystemMetrics
from datetime import datetime
from threading import Thread
from getpass import getuser
from subprocess import call
from time import sleep
import tkinter
import os

from utils.webhooks import send
