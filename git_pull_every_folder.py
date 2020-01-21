# NB: this file should be launched from the directory where your repos are!
# I.e.: let's say you need to use this method on three git repos with paths
# ~/<path>/dir/repo_1, ~/<path>/dir/repo_2, ~/<path>/dir/repo_3
# then you should enter the directory 'dir', and the launch the file:
# 1) cd ~/<path>/dir
# 2) python3 ~/<some_other_path>/this_file.py

if __name__ == '__main__':

    import os
    from subprocess import call

    path = os.getcwd()
    dir_names = [
        file_name
        for file_name in os.listdir(path)
        if '.' not in file_name
    ]

    keep_on_counter = 1
    keep_on = input(
        f"> You're in {path} and the selected directories are"
        f" {', '.join(dir_names)}.\n"
        f"You wish to continue? (Y/N)\n"
    ).strip()

    while keep_on not in ('y', 'Y', 'n', 'N') and keep_on_counter < 3:
        keep_on = input(
            f"> Could not determine your previous answer.\n"
            f"Please just enter 'Y' for yes, 'N' for no.\n"
        ).strip()
        keep_on_counter += 1

    if keep_on not in ('y', 'Y', 'n', 'N') and keep_on_counter >= 3:
        print(
            f"> Cannot determine whether the program should still run or"
            f" not.\n"
            f"Aborting."
        )
        exit()

    if keep_on in ('y', 'Y'):

        check_values_counter = 1
        check_values = input(
            f"> Would you like to stop the execution to check the pulls'"
            f" data and result? \n"
            f"'Y-b' to stop execution before the pull; \n"
            f"'Y-a' to stop execution after the pull; \n"
            f"'Y-all' to stop execution before and after the pull; \n"
            f"'N' to avoid stopping execution. \n"
        ).strip()

        while check_values not in ('Y-b', 'Y-a', 'Y-all', 'N', 'n') \
         and check_values_counter < 3:
            keep_on = input(
                f"> Could not determine your previous answer.\n"
                f"Please retry.\n"
            ).strip()
            check_values_counter += 1

        if check_values not in ('Y-b', 'Y-a', 'Y-all', 'N', 'n') \
         and check_values_counter < 3:
            print(
                f"> Cannot determine whether the program should stop or not.\n"
                f"Aborting.")
            exit()

        branch = input(
            "> Choose which branch should be pulled (or leave blank for"
            " general pull):\n"
        ).strip()

        for dir_name in dir_names:
            os.chdir(path + '/' + dir_name)
            inner_file_names = os.listdir(os.getcwd())
            if '.git' in inner_file_names:
                if check_values in ('Y-b', 'Y-all'):
                    before_pull = input(
                        f"> Pull yet to be done for '{dir_name}'.\n"
                        f"Write any git command here to be executed, leave"
                        f" blank to skip.\n"
                    ).strip()
                    while before_pull != "":
                        command = [c for c in before_pull.split(' ')
                                   if c.strip() != '']
                        call(command)
                        before_pull = input(
                            f"> Pull yet to be done for '{dir_name}'.\n"
                            f"Write any git command here to be executed, leave"
                            f" blank to skip.\n"
                        ).strip()

                print(f"> In directory {path}/{dir_name}")
                if branch:
                    call(['git', 'checkout', branch])
                    call(['git', 'pull', 'origin', branch])
                else:
                    call(['git', 'pull'])
                if check_values in ('Y-a', 'Y-all'):
                    after_pull = input(
                        f"> Pull done for '{dir_name}'.\n"
                        f"Write any git command here to be executed, leave"
                        f" blank to skip.\n"
                    ).strip()
                    while after_pull != "":
                        command = [c for c in after_pull.split(' ')
                                   if c.strip() != '']
                        call(command)
                        after_pull = input(
                            f"> Pull done for '{dir_name}'.\n"
                            f"Write any git command here to be executed, leave"
                            f" blank to skip.\n"
                        ).strip()

        print(f"> Thanks for your patience! See ya next time!")

    else:
        print(f"> Thank you anyway! See ya next time!")
