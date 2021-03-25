from flask import Flask, render_template, redirect
from fileload import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/carousel', methods=['GET', 'POST'])
def sample_file_upload():
    files = sorted(os.listdir("static/images"))
    form = FileLoad()
    if form.validate_on_submit():
        f = form.file_load.data
        return redirect("/carousel")
    return render_template('carousel.html', title="Карусель", files=files, form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
