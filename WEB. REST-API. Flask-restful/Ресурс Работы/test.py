from requests import get, post, put, delete

# Проверка вывода
print(get("http://127.0.0.1:8080/api/v2/jobs").json())
print(get("http://127.0.0.1:8080/api/v2/jobs/1").json())

# Добавляем и проверяем добавление данных
print(post("http://127.0.0.1:8080/api/v2/jobs", json={
    "team_leader": 3, "job": "super mega duper creator", "work_size": 32,
    "collaborators": "2, 4", "is_finished": False}).json())
print(get("http://127.0.0.1:8080/api/v2/jobs").json())

# Изменяем добавленное и печатаем
print(put("http://127.0.0.1:8080/api/v2/jobs/2", json={
    "team_leader": 2, "job": "super mega duper creator", "work_size": 33,
    "collaborators": "1, 65", "is_finished": True}).json())
print(get("http://127.0.0.1:8080/api/v2/jobs").json())

# Удаляем добавленное и печатаем
print(delete("http://127.0.0.1:8080/api/v2/jobs/2").json())
print(get("http://127.0.0.1:8080/api/v2/jobs").json())

# Ошибка вывода
print(get("http://127.0.0.1:8080/api/v2/jobs/999").json())  # Несуществующий ID

# Ошибка добавления данных
print(post("http://127.0.0.1:8080/api/v2/jobs", json={}).json())  # Пустые данные

# Ошибка изменения данных
print(put("http://127.0.0.1:8080/api/v2/jobs/1", json={}).json())  # Пустые данные

# Ошибка удаления
print(delete("http://127.0.0.1:8080/api/v2/jobs/999").json())  # Несуществующий ID
