
from .catalog import Library
from utils.formatting import format_book_data
def generate_report(library: Library) -> str:
    report_lines = []
    report_lines.append("Отчет о книгах в библиотеке:\n")
    
    for book in library.books:
        
        report_lines.append(format_book_data(book))
    
    report = "\n".join(report_lines)
    return report
