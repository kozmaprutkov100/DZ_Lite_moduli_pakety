class Book:
    def __init__(self, title, author, style):
        self.title = title
        self.author = author
        self.style = style

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, style):
        new_book = Book(title, author, style)
        self.books.append(new_book)
        print(f'Книга "{title}" автора "{author}" жанр "{style}" \
              добавлена в библиотеку.')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книга "{title}" удалена из библиотеки.')
            else:    
                print(f'Книга "{title}" не найдена в библиотеке.')

    def find_book(self, title=None, author=None, style=None):
        found_books = []
        for book in self.books:
            if (book.title == title) and \
               (book.author == author) and \
               (book.style == style):
                    found_books.append(book)
        for book in found_books:
            print('Найденная книга: \n')
            print(f'Название: {book.title}, Автор: {book.author}, Жанр: {book.style}')
        return found_books

    def view_books(self):
        if not self.books:
            print("Библиотека пуста.")
            return
        print("Список книг в библиотеке: \n")
        for book in self.books:
            print(f'Название: {book.title}, Автор: {book.author}, Жанр: {book.style}')

