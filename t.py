# from modules.banner import Menu


# Menu.main_menu()


# from modules.settings import Read_Setting, Write_Setting



# print(Read_Setting()['website'])

# Write_Setting('website', 'microsoft')
# import zipfile
import platform
arch = platform.uname().machine.lower()
# print(zipfile.PyZipFile('loclx-windows-amd64.zip').namelist()[0])
# print(zipfile.ZipFile('loclx-windows-amd64.zip').filelist[0]['filename'])


print(arch)

import requests

print(requests.get("http://127.0.0.1:4040/api/tunnels").json()['tunnels'][0]['public_url'])