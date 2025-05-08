#------------- IMPORT ------------#
from os import system as c
import time
import random

#---------------- COLOUR ----------------#
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'
B = '\x1b[38;5;51m'

#---------------- LOGO ----------------#
def logo():
    c('clear')
    print(f"""{R}
 █     █░ ██▓ ██▓███   ██▓  ██████ 
▓█░ █ ░█░▓██▒▓██░  ██▒▓██▒▒██    ▒ 
▒█░ █ ░█ ▒██▒▓██░ ██▓▒▒██▒░ ▓██▄   
░█░ █ ░█ ░██░▒██▄█▓▒ ▒░██░  ▒   ██▒
░░██▒██▓ ░██░▒██▒ ░  ░░██░▒██████▒▒
░ ▓░▒ ▒  ░▓  ▒▓▒░ ░  ░░▓  ▒ ▒▓▒ ▒ ░
  ▒ ░ ░   ▒ ░░▒ ░      ▒ ░░ ░▒  ░ ░
  ░   ░   ▒ ░░░        ▒ ░░  ░  ░  
    ░     ░            ░        ░  

        {Y}>>> HACKING WORLD - WIFI VIP TOOL <<<
""")

#---------------- LOADING ANIMATION ----------------#
def loading(text):
    for i in range(3):
        print(f"{Y}{text}{'.' * (i+1)}")
        time.sleep(0.5)

#---------------- MAIN MENU ----------------#
def menu():
    logo()
    print(f"{A}[1] WIFI PASSWORD HACK (ULTRA VIP)")
    print(f"{A}[0] EXIT TOOL")
    print(f"{A}---------------------------------------------")
    choice = input(f"{C}[?] SELECT OPTION: ")
    if choice == '1':
        wifi_hack()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] INVALID OPTION")
        time.sleep(1)
        menu()

#---------------- WIFI HACK ULTRA PRANK ----------------#
def wifi_hack():
    logo()
    c('espeak "Starting WiFi Password Hack"')
    target = input(f"{C}ENTER TARGET WIFI NAME (SSID): ")
    loading(f"{B}Scanning Network {target}")
    print(f"{G}[✓] {target} Found!")
    time.sleep(1)
    loading(f"{Y}Launching Bruteforce Attack")

    # Ultra VIP password list
    passwords = [
        '12345678','password2024','letmein123','admin@2024',
        'supersecurewifi','hackingworld123','vipaccess2025',
        'bangladesh007','superkingpass','netbreaker2025',
        'bosswifi2025','rootaccess@wifi','secretbase2024',
        'hackersquad2025','privatepass123','wifi_crack_me',
        'n3tw0rk@vip','007JamesHack','firewifi2025'
    ]

    for pw in passwords:
        print(f"{C}[*] Testing Password: {pw}")
        time.sleep(0.6)

    # Dramatic password found effect
    time.sleep(1)
    print(f"\n{R}===============================================")
    print(f"{G}[✓] PASSWORD CRACK SUCCESSFUL !!")
    final_pass = f"{target}@2025"
    print(f"{Y}[+] PASSWORD: {P}{final_pass}")
    print(f"{R}===============================================")
    time.sleep(1)
    print(f"{B}\n[!] WARNING: Use this only for educational HACK!")
    input(f"\n{A}Press Enter To Return To Menu...")
    menu()

#---------------- START TOOL ----------------#
menu()