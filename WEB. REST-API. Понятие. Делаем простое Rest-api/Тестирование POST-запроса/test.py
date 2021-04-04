from requests import post
from requests import get

print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ

print(post('http://127.0.0.1:8080/api/jobs/3',
           json={'team_leader': 4,
                 'job': 'супер пупер инженер вау',
                 'work_size': 35,
                 'collaborators': '3, 4',
                 'is_finished': False}).json())  # Правильный запрос, добавление новых данных

print(get('http://127.0.0.1:8080/api/jobs').json())  # Вывод всех работ(проверка добавления данных)

print(post('http://127.0.0.1:8080/api/jobs/1',
           json={'team_leader': 2,
                 'job': 'super puper engineer wow',
                 'work_size': 34,
                 'collaborators': '2, 5',
                 'is_finished': True}).json())  # Ошибочный запрос (проверка на существующий ID)

print(post('http://127.0.0.1:8080/api/jobs/3',
           json={}).json())  # Ошибочный запрос (json данные пустые)

print(post('http://127.0.0.1:8080/api/jobs/string',
           json={'team_leader': 2,
                 'job': 'super puper engineer wow',
                 'work_size': 34,
                 'collaborators': '2, 5',
                 'is_finished': True}).json())  # Ошибочный запрос (вместо ID введена строка)

# {'jobs': [{'collaborators': '2, 3', 'id': 1, 'is_finished': False, 'team_leader': 1, 'work_size': 15},
# {'collaborators': '2, 5', 'id': 2, 'is_finished': True, 'team_leader': 2, 'work_size': 34}]}

# {'success': 'OK'}

# {'jobs': [{'collaborators': '2, 3', 'id': 1, 'is_finished': False, 'team_leader': 1, 'work_size': 15},
# {'collaborators': '2, 5', 'id': 2, 'is_finished': True, 'team_leader': 2, 'work_size': 34},
# {'collaborators': '3, 4', 'id': 3, 'is_finished': False, 'team_leader': 4, 'work_size': 35}]}

# {'error': 'Id already exists'}

# {'error': 'Empty request'}

# {'error': 'ID must be integer'}
