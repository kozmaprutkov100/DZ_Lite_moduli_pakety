from library_manager.catalog import Library

my_library = Library()
#Добавление книг в библиотеку
my_library.add_book('Братья Карамазовы', 'Федор Достоевский', 'филосовский роман' )
my_library.add_book('Основание', 'Айзек Азимов', 'научная фантастика' )
my_library.add_book('123', '456', '789' )

#Просмотр всех книг в библиотеке
my_library.view_books()

#Поиск книги по названию, автору, или жанру
my_library.find_book('Братья Карамазовы', 'Федор Достоевский', '')
my_library.find_book('', 'Айзек Азимов', '')

#Удаление книги по названию
my_library.remove_book('Братья Карамазовы')

#Просмотр всех книг в библиотеке
my_library.view_books()