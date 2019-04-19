import sys
import os
import datetime
import shutil
import errno

from pprint import pprint

to_copy = [
    r'PlanetSide2_x64.exe',
    r'Locale',
    r'UI',
    r'Resources'
    ]
    

def backup_dir(dir):
    if not os.path.exists(dir[1]):
        print('Path doesn\'t exist')

    name = datetime.date.today().strftime(f'%m-%d-%y-{dir[0]}')
    path = 'Backups\\' + name
    dir = dir[1]

    # Make backup dir
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    print('Backing up files...')

    for f in to_copy:
        print(f)
        try:
            shutil.copytree(dir+'\\'+f, path+'\\'+f)
        except NotADirectoryError:
            shutil.copy(dir+'\\'+f, path)

        except FileExistsError as e:
            print(e)

    print('Finished!')

def main():
    dirs = []
    
    with open('ps2mine-dirs.txt', 'r') as in_file:
        for line in in_file:
            dirs.append(line.strip().split('='))

    for i, x in enumerate(dirs):
        print(f'[{i}]: {x[0]}')

    try:
        choice = int(input('Choose a folder >'))

    except ValueError:
        print('Please enter a number')
        main()

    if not choice < len(dirs) or choice < 0:
        print('Not a valid option')
        main()

    backup_dir(dirs[choice])

if __name__ == "__main__":
    main()
