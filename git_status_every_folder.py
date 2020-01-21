# NB: this file should be launched from the directory where your repos are!
# I.e.: let's say you need to use this method on three git repos with paths
# ~/<path>/dir/repo_1, ~/<path>/dir/repo_2, ~/<path>/dir/repo_3
# then you should enter the directory 'dir', and the launch the file:
# 1) cd ~/<path>/dir
# 2) python3 ~/<some_other_path>/this_file.py

import os
from subprocess import call


def check_directory(path):
    os.chdir(path)
    dir_files = os.listdir(path)
    if '.git' in dir_files:
        call(['git', 'remote', '-v'])
        call(['git', 'status'])
        input(">>> Press 'Enter' when ready to continue...")

    for dname in dir_files:
        try:
            check_directory(path + '/' + dname)
        except (FileNotFoundError, NotADirectoryError, PermissionError):
            continue


if __name__ == '__main__':
    check_directory(os.getcwd())
