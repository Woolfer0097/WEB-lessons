from requests import put, get

print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ(проверка данных)
print(put("http://127.0.0.1:8080/api/jobs/3",
          json={'team_leader': 5,
                'job': 'супер пуавыапер инженер вау',
                'work_size': 352,
                'collaborators': '34, 4',
                'is_finished': True}).json())  # Удаление данных по ID = 1
print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ(проверка удаления данных)

print(put("http://127.0.0.1:8080/api/jobs/999",
          json={'team_leader': 5,
                'job': 'супер пуавыапер инженер вау',
                'work_size': 352,
                'collaborators': '34, 4',
                'is_finished': True}).json())  # (Ошибка) Удаление данных по несуществующему ID

print(put("http://127.0.0.1:8080/api/jobs/999",
          json={}).json())  # (Ошибка) Не указаны изменения

# {'jobs': [{'collaborators': '2, 5', 'id': 2, 'is_finished': True, 'team_leader': 2, 'work_size': 34},
# {'collaborators': '3, 4', 'id': 3, 'is_finished': False, 'team_leader': 4, 'work_size': 35}]}

# {'success': 'OK'}

# {'jobs': [{'collaborators': '2, 5', 'id': 2, 'is_finished': True, 'team_leader': 2, 'work_size': 34},
# {'collaborators': '34, 4', 'id': 3, 'is_finished': True, 'team_leader': 5, 'work_size': 352}]}
