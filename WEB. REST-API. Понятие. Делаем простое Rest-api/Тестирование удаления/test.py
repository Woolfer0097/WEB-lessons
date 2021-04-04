from requests import delete, get

print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ(проверка данных)
print(delete("http://127.0.0.1:8080/api/jobs/2").json())  # Удаление данных по ID = 1
print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ(проверка удаления данных)

print(delete("http://127.0.0.1:8080/api/jobs/2").json())  # Ошибочный запрос (Обращение к несуществующему ID)

# {'jobs': [{'collaborators': '2, 5', 'id': 2, 'is_finished': True, 'team_leader': 2, 'work_size': 34},
# {'collaborators': '3, 4', 'id': 3, 'is_finished': False, 'team_leader': 4, 'work_size': 35}]}

# {'success': 'OK'}

# {'jobs': [{'collaborators': '3, 4', 'id': 3, 'is_finished': False, 'team_leader': 4, 'work_size': 35}]}

# {'error': 'Id does not exist'}
