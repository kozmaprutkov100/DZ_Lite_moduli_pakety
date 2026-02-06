from utils.data_validation import validate_book_data
class Book:
    def __init__(self, title: str, author: str, style: str):
        self.title = title
        self.author = author
        self.style = style

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, style: str):
        new_book = Book(title, author, style)
        if validate_book_data(new_book):
            self.books.append(new_book)
            print(f'Книга "{title}" автора "{author}" жанр "{style}" \
                добавлена в библиотеку.')
        else:
            print('Книга не прошла валидацию.')

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Книга "{title}" удалена из библиотеки.')
            else:    
                print(f'Книга "{title}" не найдена в библиотеке.')

    def find_book(self, title: str = None, author: str = None, style: str = None):
        found_books = []
        for book in self.books:
            if (book.title == title) or \
               (book.author == author) or \
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

