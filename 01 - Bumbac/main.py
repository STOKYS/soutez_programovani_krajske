def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("bumbác")
        elif i % 3 == 0:
            print("bum")
        elif i % 5 == 0:
            print("bác")
        else:
            print(i)


if __name__ == '__main__':
    main()
