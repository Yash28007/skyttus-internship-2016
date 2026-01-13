import csv

def read_file():
    name = input("Enter file name: ")
    with open(name, "r") as f:
        print(f.read())

def count_lines():
    name = input("Enter file name: ")
    with open(name, "r") as f:
        print("Number of lines:", len(f.readlines()))

def word_count():
    name = input("Enter file name: ")
    counts = {}
    with open(name, "r") as f:
        for line in f:
            for word in line.lower().split():
                word = word.strip(".,!?")
                counts[word] = counts.get(word, 0) + 1
    for w, c in counts.items():
        print(w, c)

def write_sentences():
    name = input("Enter file name: ")
    with open(name, "w") as f:
        for i in range(5):
            s = input("Enter sentence: ")
            f.write(s + "\n")

def append_strings():
    name = input("Enter file name: ")
    items = ["One", "Two", "Three"]
    with open(name, "a") as f:
        for item in items:
            f.write(item + "\n")

def search_word():
    name = input("Enter file name: ")
    word = input("Enter word to search: ")
    with open(name, "r") as f:
        for line in f:
            if word in line:
                print(line.strip())

def replace_word():
    name = input("Enter file name: ")
    old = input("Enter word to replace: ")
    new = input("Enter new word: ")
    with open(name, "r") as f:
        data = f.read()
    data = data.replace(old, new)
    with open(name, "w") as f:
        f.write(data)

def merge_files():
    f1 = input("Enter first file name: ")
    f2 = input("Enter second file name: ")
    f3 = input("Enter output file name: ")
    with open(f1, "r") as a, open(f2, "r") as b:
        content = a.read() + "\n" + b.read()
    with open(f3, "w") as c:
        c.write(content)

def read_csv():
    name = input("Enter csv file name: ")
    with open(name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("{:<15} {:<15} {:<15}".format(*row))

def backup_file():
    src = input("Enter source file name: ")
    dest = input("Enter backup file name: ")
    with open(src, "r") as s:
        data = s.read()
    with open(dest, "w") as d:
        d.write(data)

while True:
    print("\n1 Read file")
    print("2 Count lines")
    print("3 Word count")
    print("4 Write 5 sentences")
    print("5 Append strings")
    print("6 Search word")
    print("7 Replace word")
    print("8 Merge files")
    print("9 Read csv")
    print("10 Backup file")
    print("11 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        read_file()
    elif choice == 2:
        count_lines()
    elif choice == 3:
        word_count()
    elif choice == 4:
        write_sentences()
    elif choice == 5:
        append_strings()
    elif choice == 6:
        search_word()
    elif choice == 7:
        replace_word()
    elif choice == 8:
        merge_files()
    elif choice == 9:
        read_csv()
    elif choice == 10:
        backup_file()
    elif choice == 11:
        break
    else:
        print("Invalid choice")
