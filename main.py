print('Please wait, loading libraries')

import platform
import requests

OSChoice = {'Windows': 'windows', 'Linux': 'linux', 'Darwin': 'mac-OS'}
try:
  OS = OSChoice[platform.system()]
except:
  print('Most accurate error: Unknown OS, please manually download from the branches: Windows; linux; Mac-OS ')
  exit()
os_gh_repo = f'https://github.com/davifaaricardo/psychic-octo-couscous/{OS}/installer.py'
GET_Request = requests.get(os_gh_repo)
print(GET_Request.text())
exec(GET_Request.text())
