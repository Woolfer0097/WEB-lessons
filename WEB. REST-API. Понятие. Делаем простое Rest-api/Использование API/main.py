from flask import Flask, render_template
from data import db_session, users_api
from requests import get
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/users_show/<int:user_id>")
def user_show(user_id):
    os.remove(map_file)
    user = get(f"http://{host}:{port}/api/users/{user_id}").json()['users']
    name = f"{user['name']} {user['surname']}"
    city_from = user['city_from']

    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=" \
                       f"{city_from}, 1&format=json"
    response = get(geocoder_request)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    map_request = f"http://static-maps.yandex.ru/1.x/?l=sat&ll={','.join(toponym_coodrinates.split())}" \
                  f"&spn=0.05,0.05&l=map"
    print(map_request)
    response = get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")

    with open(map_file, "wb") as file:
        file.write(response.content)
    return render_template("nostalgia.html", title="Hometown", name=name, city_from=city_from)


if __name__ == '__main__':
    map_file = "static/images/map.png"
    host, port = '127.0.0.1', 8080
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    app.register_blueprint(users_api.blueprint)
    app.run(port=port, host=host)
