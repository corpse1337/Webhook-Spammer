import os
import sys
import httpx
from colorama import Fore,init
init(convert=True)

def clsx():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

clsx()

print(Fore.YELLOW+"""

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                                         ~ [https://github.com/corpse1337][Corpse Development]""")






webhook = input(Fore.YELLOW+"Enter the Webhook Url: ")
msg = input(Fore.BLUE+"Enter the message: ")
tm = int(input(Fore.CYAN+"Enter the number of times to spam: "))


            
def proxyless_mode():
        req = httpx.post(webhook, json={'content': msg})
        if req.status_code == 204:
            print(Fore.GREEN+"Webhook sent Successfully")
        else:
            print(Fore.RED+"Action rejected, try again after checking")
            

support = input(Fore.WHITE+"Start Confirmation? (Y/N): ")


if support == "Y":
    for i in range(tm):
        proxyless_mode()
elif support == "N":
    sys.exit()