from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/promotion_image')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <href><images src="{url_for('static', filename='images/MARS.jpg')}"
                    alt="здесь должна была быть картинка, но не нашлась" height=600></href>
                    <div class="alert-dark" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert-success" role="alert">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert-light" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты
                    </div>
                    <div class="alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
