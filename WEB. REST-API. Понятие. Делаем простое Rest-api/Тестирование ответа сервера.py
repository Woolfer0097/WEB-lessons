from requests import get

print(get('http://127.0.0.1:8080/api/news').json())
print(get('http://127.0.0.1:8080/api/news/1').json())
print(get('http://127.0.0.1:8080/api/news/999').json())
print(get('http://127.0.0.1:8080/api/news/string').json())
