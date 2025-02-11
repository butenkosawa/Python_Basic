from string import punctuation
from keyword import kwlist

name_of_var = input('Enter name of variable: ')

if name_of_var.startswith('_') and len(name_of_var) == 1:
    print('True')
else:
    if name_of_var[0].isdigit():
        print('False')
    elif name_of_var in kwlist:
        print('False')
    elif not name_of_var.islower():
        print('False')
    elif len(name_of_var) > 0:
        for sym in punctuation.replace('_',' '):
            if sym in name_of_var:
                print('False')
                break
        else:
            print('True')
