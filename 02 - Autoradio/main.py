import unicodedata
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory


def strip_name(folder, name):
    # Prevede na relativni cestu
    __tmp = folder.split("/")[-1]
    return f"{__tmp}{name.replace(folder, '')}"


def convert_name(name):
    # Zbavi se diakritiky
    return unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')


def main():

    Tk().withdraw()
    folder = askdirectory()

    # Cesta k vybrane slozce
    # folder = '/home/david_stocek/Documents/Programming/Python/stocek_soutez_krajske/02 - Autoradio/data/Jindřicův archív'
    # Zjisti zda slozka existuje
    if os.path.exists(folder):
        # Projde vsechny soubory ve slozce
        for root, dirs, files in os.walk(folder, topdown=False):
            for x, name in enumerate(files):
                print(f'{os.path.join(strip_name(folder, root), name)} -> {convert_name(name)}')
                if len(files) - 1 == x:
                    print(f'{strip_name(folder, root)} -> {convert_name(strip_name(folder, root))}')
        print(f'{strip_name(folder, folder)} -> {convert_name(strip_name(folder, folder))}')
    else:
        print(f'{folder} does not exist')


if __name__ == "__main__":
    main()
