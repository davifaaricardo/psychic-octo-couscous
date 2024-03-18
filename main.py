try: 
  from platform import system # not used delete
except: 
  print('Please install `platform` ')
  exit()
try: 
  from requests import get # not used delete
except: 
  print('Please install `requests` ')
  exit()
try: 
  OS = {'Windows': 'windows', 'Linux': 'linux', 'Darwin': 'mac-OS'}[system()] # not used delete
except: 
  print(' Syntax Error; or ')
  print(' you changed some code in platform; or ')
  print(' Most accurate error: Unknown OS, please manually download from the branches: Windows; linux; Mac-OS;')
  exit()
try: 
  os_gh_repo = f'https://raw.githubusercontent.com/davifaaricardo/psychic-octo-couscous/{OS}/installer.py' # not used delete
except: 
  print('error in OS')
  exit()
try:
  GET_Request = get(os_gh_repo)
except: 
  print('Unknown link or error in `os_gh_repo`')
  exit()
try: 
  del os_gh_repo, OS, get, system
  exec(GET_Request.text) # not used delete
  del GET_Request
except: 
  print(f'error in the os local install.py or error in GET_Request');
  exit()
