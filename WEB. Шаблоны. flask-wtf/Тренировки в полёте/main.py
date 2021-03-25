from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index/<title>/<prof>')
def mission(title, prof):
    if "инженер" in prof or "строитель" in prof:
        prof = "Инженерные тренажеры"
        img = url_for('static', filename="images/ship1.jpg")
    else:
        prof = "Научные симуляторы"
        img = url_for('static', filename="images/sh1p2.jpg")
    return render_template('base.html', title=title, profession=prof, image=img)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
