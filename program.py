import os
import platform
import subprocess
import meme_searcher


def main():
    print_header()
    folder, meme_name = get_or_create_output_folder()
    download_meme(meme_name)
    # display cats
    pass


def print_header():
    print('------------------------------------')
    print('         MEME FACTORY APP')
    print('------------------------------------')
    print('')


def get_or_create_output_folder():
    base_name = os.path.dirname(__file__)
    folder = input('What meme are you looking for? ')
    full_path = os.path.join(base_name, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating a folder called {folder}...')
        os.mkdir(full_path)

    return full_path, folder


def download_meme(folder):
    count = int(input("How many do you want to download? "))
    for i in range(1, count + 1):
        name = '{} {}'.format(folder, i)
        print(f'Downloading {name}...')
        meme_searcher.search_meme(folder, name)


def display_meme(folder):
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    if platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    if platform.system() == 'Darwin':
        subprocess.call(['xdg-open', folder])
    else:
        print(f'Sorry. Does not support {platform.system()}')


if __name__ == '__main__':
    main()
