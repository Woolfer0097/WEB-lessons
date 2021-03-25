from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def form_sample(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Результат отбора</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>На участие в миссии {nickname}:</h2>
                            <div class="p-3 mb-2 bg-success text-white">Поздравляем ваш рейтинг после {level} этапа отбора</div>
                            <div class="p-3 mb-2 bg-light text-dark">составляет {rating}!</div>
                            <div class="p-3 mb-2 bg-warning text-dark">Желаем удачи!</div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
