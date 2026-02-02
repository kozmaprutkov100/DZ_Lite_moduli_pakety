def validate_book_data(data: dict) -> bool:
    # Проверяем, что все обязательные поля присутствуют
    required_fields = ['title', 'author', 'style']
    
    for field in required_fields:
        if field not in data:
            print(f"Отсутствует обязательное поле: {field}")
            return False
    
    # Проверяем, что значения полей не пустые
    if not data['title'] or not data['author'] or not data['style']:
        print("Все поля должны быть заполнены.")
        return False
    
    # Можно добавить дополнительные проверки, например, на тип данных
    if not isinstance(data['title'], str) or not isinstance(data['author'], str) or not isinstance(data['style'], str):
        print("Все поля должны быть строками.")
        return False
    
    return True