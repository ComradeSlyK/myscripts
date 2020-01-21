# NB: this file should be launched from the directory where your repos are!
# I.e.: let's say you need to use this method to generate path for repos
# repo_1, repo_2, repo_3 within directory 'dir'; then you should enter the
# directory 'dir', and the launch the file:
# 1) cd ~/<path>/dir
# 2) python3 ~/<some_other_path>/this_file.py

if __name__ == '__main__':

    import os

    print(
        ",".join(
            sorted([
                os.path.join(os.getcwd(), o)
                for o in os.listdir('.')
                if os.path.isdir(os.path.join('.', o))
            ])
        )
    )
