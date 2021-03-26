from flask import Flask, render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/member', methods=['GET', 'POST'])
def sample_file_upload():
    with open("templates/info.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return render_template('self_card.html', data=data, keys=list(data.keys()))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
