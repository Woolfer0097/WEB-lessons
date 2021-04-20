import sqlite3


connection = sqlite3.connect("../db/books.db")
cursor = connection.cursor()
query = cursor.execute("SELECT content_analysis FROM books").fetchall()
count = 0
for i in query:
    for j in i:
        count += 1
        start = j.find("<p") - 1
        html = ""
        for k in range(len(j)):
            if start <= k:
                html += j[k]
        html = html.strip("<div>")
        html = html.strip("</div>")
        cursor.execute(f"UPDATE books set content_analysis = '{html}' WHERE id = {count}")
connection.commit()
