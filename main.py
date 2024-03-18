try: 
  import platform 
except: 
  print('Please install `platform` ')
  exit()
try: 
  import requests 
except: 
  print('Please install `requests` ')
  exit()
try: 
  OS = {'Windows': 'windows', 'Linux': 'linux', 'Darwin': 'mac-OS'}[platform.system()]
except: 
  print(' Syntax Error;\n you changed some code in platform;\n Most accurate error: Unknown OS, please manually download from the branches: Windows; linux; Mac-OS'); exit()
try: 
  os_gh_repo = f'https://raw.githubusercontent.com/davifaaricardo/psychic-octo-couscous/{OS}/installer.py'
except: 
  print('error in OS')
  exit()
try:
  GET_Request = requests.get(os_gh_repo)
except: 
  print('Unknown link or error in `os_gh_repo`')
  exit()
try: 
  exec(GET_Request.text)
except: 
  print(f'error in `{OS}/install.py` or error in GET_Request');
  exit()
