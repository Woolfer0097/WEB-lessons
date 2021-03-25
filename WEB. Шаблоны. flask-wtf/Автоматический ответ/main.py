from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/auto_answer')
@app.route('/answer')
def auto_answer():
    return render_template('base.html', title=dicta["title"], dict_items=dicta,
                           url=url_for('static', filename='css/style.css'))


if __name__ == '__main__':
    dicta = {
        "title": "Анкета",
        "Фамилия": "Watny",
        "Имя": "Mark",
        "Образование": "выше среднего",
        "Профессия": "штурман марсохода",
        "Пол": "male",
        "Мотивация": "Всегда мечтал застрять на Марсе!",
        "Готовы остаться на Марсе?": True
    }
    app.run(port=8080, host='127.0.0.1')
