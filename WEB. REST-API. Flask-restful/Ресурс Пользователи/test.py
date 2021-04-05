from requests import get, delete, post

# Проверка вывода
print(get("http://127.0.0.1:8080/api/v2/users").json())
print(get("http://127.0.0.1:8080/api/v2/users/4").json())

# Добавляем и проверяем добавление данных
print(post("http://127.0.0.1:8080/api/v2/users", json={
                        'surname': "Kochegarov", 'name': "Dan", 'age': 24,
                        'position': "Re-Director", 'speciality': "Environment defender",
                        'address': "module_11", 'email': "Dan100605@gmail.com"}).json())
print(get("http://127.0.0.1:8080/api/v2/users").json())

# Удаляем добавленное и печатаем
print(delete("http://127.0.0.1:8080/api/v2/users/5").json())
print(get("http://127.0.0.1:8080/api/v2/users").json())

# Ошибка вывода
print(get("http://127.0.0.1:8080/api/v2/users/999").json())  # Несуществующий ID

# Ошибка добавления данных
print(post("http://127.0.0.1:8080/api/v2/users", json={}).json())  # Пустые данные

# Ошибка удаления
print(delete("http://127.0.0.1:8080/api/v2/users/999").json())  # Несуществующий ID
