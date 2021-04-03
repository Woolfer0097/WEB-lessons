from requests import post

print(post('http://127.0.0.1:8080/api/news',
           json={'team_leader': 2,
                 'job': 'super puper engineer wow',
                 'work_size': 34,
                 'collaborators': '2, 5',
                 'is_finished': True}).json())
