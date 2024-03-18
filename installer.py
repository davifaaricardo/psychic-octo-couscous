file = input('Insert full path: ')
opt =  input('Would you like to [c]hange or [d]ecompile? ')
print('getting decompile from decompiler.py on davifaaricardo/psychic-octo-couscous/windows')
exec(__import__('requests').get('https://raw.githubusercontent.com/davifaaricardo/psychic-octo-couscous/windows/decompiler.py').text)
if opt == 'd':exec(f'decompile({file},'.')')
elif opt == 'c':print('insert changing code')
else:print(f"ERROR, option {opt} doesn't exist.");
