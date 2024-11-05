import re

def parse_email(email):

    pattern = r'^(?P<username>[a-zA-Z][a-zA-Z0-9._%+-]*)@(?P<domain>[a-zA-Z][a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$'
    match = re.match(pattern, email)

    if match:
        username = match.group('username')
        domain = match.group('domain')
        return username, domain
    else:
        raise ValueError("Некорректный формат email.")

email = input("Введите email: ")
try:
    username, domain = parse_email(email)
    print(f"Имя пользователя: {username}, Домен: {domain}")
except ValueError as e:
    print(e)