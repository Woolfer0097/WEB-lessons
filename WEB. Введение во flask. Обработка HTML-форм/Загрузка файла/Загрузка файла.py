import urllib.request

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload(photo=None):
    if request.method == 'GET':
        return f'''<!doctype html>
                                    <html lang="en">
                                      <head>
                                        <meta charset="utf-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                         <link rel="stylesheet"
                                         href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                         integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                         crossorigin="anonymous">
                                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                        <title>Загрузка файла</title>
                                      </head>
                                      <body>
                                        <form method="post" enctype="multipart/form-data">
                                           <h1>Загрузка фотографии</h1>
                                           <h2>для участия в миссии</h2>
                                           <div class="form-group">
                                                <label for="photo">Выберите файл</label>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                            </div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                      </body>
                                    </html>'''
    elif request.method == 'POST':
        file = request.files['file']
        with open("static/img/image.jpg", "wb") as file_write:
            file_write.write(file.read())
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
                            <title>Загрузка файла</title>
                          </head>
                          <body>
                            <form method="post" enctype="multipart/form-data">
                               <h1>Загрузка фотографии</h1>
                               <h2>для участия в миссии</h2>
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <images src="static/images/image.jpg" alt="Изображение не найдено">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
