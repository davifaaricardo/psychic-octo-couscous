file = input('Insert full path (useless for now): ')
opt =  input('Would you like to [c]hange or [d]ecompile? ')

match opt:
  case 'd':
    print('insert decompiling code')
  case 'c':
    print('insert changing code')
  case _:
    print(f"ERROR, option {opt} doesn't exist.");
