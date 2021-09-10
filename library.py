from library_module.library import Biblioteka

file = open('data.txt', 'r')
list = []
for line in file.readlines():
    print(line.split(','))

"""ALLOWED_COMMANDS = ('add', 'delete', 'books', 'stop')
bib = Biblioteka(address="Warszawa", name="Moja Biblioteka")

while True:
    command = input("Podaj komende: ")
    if command not in ALLOWED_COMMANDS:
        print(f"Niepoprawna komenda! Dostępne komendy: {ALLOWED_COMMANDS}")
        continue
    if command == 'stop':
        break
    if command == 'add':
        bib.add_book()
    if command == 'delete':
        bib.delete_book()
    if command == 'books':
        bib.show_books()"""