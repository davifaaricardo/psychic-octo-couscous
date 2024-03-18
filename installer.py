file = input('Insert full path (useless for now): ')
opt =  input('Would you like to [c]hange or [d]ecompile? ')
import colorama
colorama.init()

match opt:
  case 'd':
    print('insert decompiling code')
  case 'c':
    print('insert changing code')
  case _:
    print(f"{colorama.Fore.RED}ERROR option: {opt} doesn't exist.");
