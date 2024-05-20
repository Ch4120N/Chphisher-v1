import requests
import os
import subprocess
import zipfile
import platform
import shutil
import sys
import time
from colorama import Fore, init
from modules.check import system
init()


units = {     
'B' : {'size':1, 'speed':'B/s'}, 
'KB' : {'size':1024, 'speed':'KB/s'}, 
'MB' : {'size':1024*1024, 'speed':'MB/s'}, 
'GB' : {'size':1024*1024*1024, 'speed':'GB/s'} 
} 
  
def check_unit(length): # length in bytes 
    if length < units['KB']['size']: 
        return 'B'
    elif length >= units['KB']['size'] and length <= units['MB']['size']: 
        return 'KB'
    elif length >= units['MB']['size'] and length <= units['GB']['size']: 
        return 'MB'
    elif length > units['GB']['size']: 
        return 'GB'


# Download Binaries
def download(url, output):

    file = os.path.basename(url)
    try:
        if os.path.exists(file) or os.path.exists(output):
            os.remove(file)
            os.remove(output)
    except:
        pass
    try:
        with open(file, 'wb') as f:
            # r = requests.get(url)
            # files.write(r.content)
            start = time.time() # start time 
            r = requests.get(url, stream=True) 

            # total length in bytes of the file 
            total_length = float(r.headers.get('content-length'))

            d = 0 # counter for amount downloaded  

            if total_length is None: 
                f.write(r.content)
            else:
                for chunk in r.iter_content(8192):
                    d += float(len(chunk)) 
                    f.write(chunk) # writing the file in chunks of 8192 bytes 
    
                    # amount downloaded in proper units 
                    downloaded = d/units[check_unit(d)]['size'] 
                    
                    # converting the unit of total length or size of file from bytes. 
                    tl = total_length / units[check_unit(total_length)]['size']  
                    
                    trs = d // (time.time() - start) # speed in bytes per sec 
                    
                    #speed in proper unit 
                    download_speed = trs/units[check_unit(trs)]['size'] 
                    
                    speed_unit = units[check_unit(trs)]['speed'] # speed in proper units 

                    done = 100 * d / total_length # percentage downloaded or done. 
                    
                    fmt_string = Fore.LIGHTRED_EX+"\r%6.2f %s [%s%s] %7.2f%s  /  %4.2f %s  %7.2f %s"
                    
                    set_of_vars = ( float(done), '%', 
                                    '#' * int(done/2),   
                                    '.' * int(50-done/2),   
                                    downloaded, check_unit(d),   
                                    tl, check_unit(total_length),   
                                    download_speed, speed_unit) 
    
                    sys.stdout.write(fmt_string % set_of_vars) 
    
                    sys.stdout.flush() 
    except:
        print(f"{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Internet Connection Error or somthing wrong!!")
        sys.exit()
        # return (time.time() - start) # total time taken for download 
  


    if os.path.exists(file):
        if file.split(".")[-1] == "zip":
            filename = zipfile.PyZipFile(file).namelist()[0]
            zipfile.PyZipFile(file).extractall('.')
            try:
                shutil.move(filename, f'.server/{output}')
            except:
                pass
        elif file.split(".")[-1] == "tgz":
            subprocess.run(["tar", "-zxf", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["mv", "-f", output, ".server/" + output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            try:
                shutil.move(file, f'.server/{output}')
            except:
                pass
        if system() == "windows":
            pass
        else:
            subprocess.run(["chmod", "+x", ".server/" + output], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            os.remove(file)
        except:
            pass

    else:
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.YELLOW}!{Fore.LIGHTBLUE_EX}]{Fore.LIGHTRED_EX} Error occurred while downloading {output}.")
        sys.exit(1)

# Install Cloudflared
def install_cloudflared():
    if os.path.exists(".server/cloudflared"):
        print(f"\n{Fore.LIGHTGREEN_EX}[+] Cloudflared already installed.")
    elif os.path.exists(".server/cloudflared.exe"):
        print(f"\n{Fore.LIGHTGREEN_EX}[+] cloudflared already installed.")
    else:
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} Installing Cloudflared...", end='')
        arch = platform.uname().machine.lower()
        if 'arm' in arch or 'Android' in arch:
            download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm', 'cloudflared')
        elif 'aarch64' in arch:
            download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64', 'cloudflared')
        elif 'x86_64' in arch:
            download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64', 'cloudflared')
        elif system() == "windows":
            if 'amd64' in arch:
                download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe', 'cloudflared.exe')
            else:
                download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-386.exe', 'cloudflared.exe')
        else:
            download('https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386', 'cloudflared')

# Install LocalXpose
def install_localxpose():
    if os.path.exists(".server/loclx"):
        print(f"\n{Fore.LIGHTGREEN_EX}[+] LocalXpose already installed.")
    elif os.path.exists(".server/localx.exe"):
        print(f"\n{Fore.LIGHTGREEN_EX}[+] LocalXpose already installed.")
    else:
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} Installing LocalXpose...", end='')
        arch = platform.uname().machine.lower()
        if 'arm' in arch or 'Android' in arch:
            download('https://api.localxpose.io/api/v2/downloads/loclx-linux-arm.zip', 'loclx')
        elif 'aarch64' in arch:
            download('https://api.localxpose.io/api/v2/downloads/loclx-linux-arm64.zip', 'loclx')
        elif 'x86_64' in arch:
            download('https://api.localxpose.io/api/v2/downloads/loclx-linux-amd64.zip', 'loclx')
        elif system() == "windows":
            if 'amd64' in arch:
                download('https://loclx-client.s3.amazonaws.com/loclx-windows-amd64.zip', 'localx.exe')
            else:
                download('https://api.localxpose.io/api/downloads/loclx-windows-386.zip', 'localx.exe')
        else:
            download('https://api.localxpose.io/api/v2/downloads/loclx-linux-386.zip', 'loclx')



def install_ngrok():
    if os.path.exists(".server/ngrok"):
        print(f"\n\n{Fore.LIGHTGREEN_EX}[+] Ngrok already installed.")
    elif os.path.exists('.server/ngrok.exe'):
        print(f"\n\n{Fore.LIGHTGREEN_EX}[+] Ngrok already installed.")
    else:
        print(f"\n{Fore.LIGHTBLUE_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTBLUE_EX}]{Fore.LIGHTCYAN_EX} Installing Ngrok...", end='')

        arch = platform.uname().machine.lower()
        if 'arm' in arch or 'Android' in arch:
            download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.tgz', 'ngrok')
        elif 'aarch64' in arch:
            download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz', 'ngrok')
        elif 'x86_64' in arch:
            download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz', 'ngrok')
        elif system() == "windows":
            if 'amd64' in arch:
                download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip', 'ngrok.exe')
            else:
                download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-386.zip', 'ngrok.exe')
        else:
            download('https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.tgz', 'ngrok')
    