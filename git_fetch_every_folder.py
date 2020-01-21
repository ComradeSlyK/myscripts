# NB: this file should be launched from the directory where your repos are!
# I.e.: let's say you need to use this method on three git repos with paths
# ~/<path>/dir/repo_1, ~/<path>/dir/repo_2, ~/<path>/dir/repo_3
# then you should enter the directory 'dir', and the launch the file:
# 1) cd ~/<path>/dir
# 2) python3 ~/<some_other_path>/this_file.py

if __name__ == '__main__':

    import os
    from subprocess import call

    current_path = os.getcwd()
    dir_names = sorted([
        file_name
        for file_name in os.listdir(current_path)
        if '.' not in file_name
    ])

    branch = input(
        "> Choose which branch should be fetched (or leave blank for"
        " general fetch):\n"
    ).strip()

    for dir_name in dir_names:
        os.chdir(current_path + '/' + dir_name)
        inner_file_names = os.listdir(os.getcwd())
        if '.git' in inner_file_names:
            print(f"In directory {current_path}/{dir_name}")
            call(['git', 'fetch', branch or '--all'])
