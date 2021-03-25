from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/choice/<planet_name>')
def form_sample(planet_name):
    if planet_name == "Марс":
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css//style.css')}" />
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Моё предложение: {planet_name}</h1>
                                <div class="p-3 mb-2 bg-white text-dark">Эта планета близка к Земле;</div>
                                <div class="p-3 mb-2 bg-success text-white">На ней много необходимых ресурсов;</div>
                                <div class="p-3 mb-2 bg-light text-dark">На ней есть вода и атмосфера;</div>
                                <div class="p-3 mb-2 bg-warning text-dark">На ней есть небольшое магнитное поле;</div>
                                <div class="p-3 mb-2 bg-danger text-white">Наконец, она просто красива!</div>
                              </body>
                            </html>'''
    else:
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css//style.css')}" />
                                <title>Варианты выбора</title>
                              </head>
                              <body>
                                <h1>Моё предложение: {planet_name}</h1>
                                <div class="p-3 mb-2 bg-white text-dark">Это планета;</div>
                                <div class="p-3 mb-2 bg-success text-white">На ней много необходимых ресурсов;</div>
                                <div class="p-3 mb-2 bg-light text-dark">Она очень красивая!</div>
                                <div class="p-3 mb-2 bg-warning text-dark">На ней есть много всего интересного;</div>
                                <div class="p-3 mb-2 bg-danger text-white">Наконец, она просто очень красива!</div>
                              </body>
                            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
