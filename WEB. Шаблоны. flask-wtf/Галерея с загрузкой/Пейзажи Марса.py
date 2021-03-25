from flask import Flask, render_template, redirect, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/gallery', methods=['GET', 'POST'])
def sample_file_upload():
    files = os.listdir("static/images")
    if request.method == "GET":
        return render_template('carousel.html', title="Карусель", files=files, length=len(files))
    elif request.method == "POST":
        file = request.files['file']
        with open(f"static/images/slide{len(files) + 1}.png", "wb") as file_write:
            file_write.write(file.read())
        return redirect("/gallery")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
