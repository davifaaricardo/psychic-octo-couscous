file = input('Insert full path: ')
opt =  input('Would you like to [c]hange or [d]ecompile? ')

print('getting decompile from decompiler.py on davifaaricardo/psychic-octo-couscous/windows')
exec(__import__('requests').get('https://raw.githubusercontent.com/davifaaricardo/psychic-octo-couscous/windows/decompiler.py').text)

match opt:
  case 'd':
    exec(f'decompile({file},'.')')
  case 'c':
    print('insert changing code')
  case _:
    print(f"ERROR, option {opt} doesn't exist.");
