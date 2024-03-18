print('Please wait, loading library: `platform`')
import platform
OSChoice = {'Windows': 'windows', 'Linux': 'linux', 'Darwin': 'mac-OS'}
try:
  OS = OSChoice[platform.system()]
except:
  print('Most accurate error: Unknown OS, please manually download from the branches: Windows; linux; Mac-OS ')
print(OS)  
