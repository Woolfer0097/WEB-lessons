from requests import get, delete, post, put

# ------------------------------------------------------------------------------#
#                      Печать информации о пользователе                         #
# ------------------------------------------------------------------------------#

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей
print(get('http://127.0.0.1:8080/api/users/1').json())  # Вывод одного пользователя

# ------------------------------------------------------------------------------#
#                           Добавление пользователя                             #
# ------------------------------------------------------------------------------#

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей

print(post('http://127.0.0.1:8080/api/users/4',
           json={'surname': "Kochegarov", 'name': "Danila",
                 'age': 21, 'position': "Programmer",
                 'speciality': "Super-director", 'address': "module_42",
                 'email': "Woolfer0097@yandex.ru"}).json())  # Правильный запрос, добавление новых данных

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей (проверка добавления данных)

print(post('http://127.0.0.1:8080/api/users/1',
           json={'surname': "Kochegarov", 'name': "Danila",
                 'age': 21, 'position': "Programmer",
                 'speciality': "Super-director", 'address': "module_42",
                 'email': "Woolfer0097@yandex.ru"}).json())  # Ошибочный запрос (проверка на существующий ID)

print(post('http://127.0.0.1:8080/api/users/3',
           json={}).json())  # Ошибочный запрос (json данные пустые)

print(post('http://127.0.0.1:8080/api/users/string',
           json={'team_leader': 2,
                 'job': 'super puper engineer wow',
                 'work_size': 34,
                 'collaborators': '2, 5',
                 'is_finished': True}).json())  # Ошибочный запрос (вместо ID введена строка)

# ------------------------------------------------------------------------------#
#                             Удаление пользователя                             #
# ------------------------------------------------------------------------------#

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей

print(delete('http://127.0.0.1:8080/api/users/4').json())  # Правильный запрос, удаляем пользователя

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей (проверка удаления данных)

print(delete("http://127.0.0.1:8080/api/users/4").json())  # Ошибочный запрос (Удаление несуществующего пользователя)

# ------------------------------------------------------------------------------#
#                            Изменение пользователя                             #
# ------------------------------------------------------------------------------#

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей

print(post('http://127.0.0.1:8080/api/users/4',
           json={'surname': "Kochegarov", 'name': "Danila",
                 'age': 21, 'position': "Programmer",
                 'speciality': "Super-director", 'address': "module_42",
                 'email': "Woolfer0097@yandex.ru"}).json())  # Правильный запрос, добавление новых данных

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей (проверка добавления данных)

print(put('http://127.0.0.1:8080/api/users/4',
          json={'surname': "Kochegarov", 'name': "Jack",
                'age': 24, 'position': "Technologist",
                'speciality': "Main-director", 'address': "module_41",
                'email': "Woolfer0097@yandex.ru"}).json())

print(get('http://127.0.0.1:8080/api/users').json())  # Вывод всех пользователей (проверка изменения данных)
