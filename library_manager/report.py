
from .catalog import Library
def generate_report(library: Library) -> str:
    report_lines = []
    report_lines.append("Отчет о книгах в библиотеке:\n")
    
    for book in library.books:
        report_lines.append(f'Название: {book.title}, Автор: {book.author}, Жанр: {book.style}')
    
    report = "\n".join(report_lines)
    return report
