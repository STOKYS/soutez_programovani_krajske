from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Cteni ze souboru
def read_file(file):
    with open(file, encoding='utf8') as f:
        t = f.read().split('\n')
        return t


def main():
    # dialog pro vyber souboru
    Tk().withdraw()
    file = read_file(askopenfilename())
    check = 1
    # kontrola zda pismena jsou v rozmezi 0-10
    while check:
        user_letters = input("Please type which letters you want to use (1 to 10): \n")
        # user_letters = "abcdefg"
        if 1 <= len(user_letters) <= 10:
            check = 0
        else:
            print("Please type only 1 to 10 letters")

    word_list = []
    for word in file:
        # porovnava vsechy pismena ve slovech
        __temp_u = user_letters.lower()
        __temp_w = word.lower()
        print(__temp_u, __temp_w)
        for letter_w in __temp_w:
            for letter_u in __temp_u:
                if letter_w == letter_u:
                    __temp_u = __temp_u.replace(letter_u, "")
                    __temp_w = __temp_w.replace(letter_w, "")
        # for letter_u in __temp_u:
        #     print(letter_u)

        if __temp_w == "":
            word_list.append(word)
    if len(word_list) == 1:
        print("No words found")
    else:
        # Vypise nejdelsi slovo z listu
        print("Longest word: " + max(word_list, key=len))


if __name__ == '__main__':
    main()
