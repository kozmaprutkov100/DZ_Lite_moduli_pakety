def format_book_data(data: dict) -> str:
        
    # Форматируем строку с данными книги
    formatted_string = "Title: {title}, Author: {author}, Genre: {style}".format(
        title=data['title'],
        author=data['author'],
        style=data['style']
    )
    
    return formatted_string