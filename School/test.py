from os import system as cmd
from os import chdir as cd
from os.path import join
from os.path import normcase as nc
from os.path import normpath as np
path = "C:\\"
cd(path)
while True:
    i = input('> ')
    if i.startswith('cd ') and not i == 'cd ':
        path = nc(np(join(path, i[3:])))
        cd(path)
    else:
        cmd(i)