from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# إعدادات الاتصال بقاعدة البيانات
db_config = {
    'user': 'app_user',
    'password': 'password',
    'host': 'localhost',
    'database': 'notes_db'
}

# HTML Template بسيط داخل الكود
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Note Taking App</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 20px auto; padding: 20px; }
        .note { border-bottom: 1px solid #ddd; padding: 10px 0; }
        .time { color: #888; font-size: 0.8em; }
    </style>
</head>
<body>
    <h2>📝 Simple Note App</h2>
    <form method="POST">
        <textarea name="note" rows="4" style="width:100%" placeholder="Write your note here..."></textarea><br><br>
        <button type="submit">Save Note</button>
    </form>
    <hr>
    <h3>Recent Notes:</h3>
    {% for note in notes %}
        <div class="note">
            <div class="time">🕒 {{ note[2] }}</div>
            <div>📌 {{ note[1] }}</div>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        note_content = request.form.get('note')
        if note_content:
            cursor.execute("INSERT INTO notes (content) VALUES (%s)", (note_content,))
            conn.commit()


    cursor.execute("SELECT * FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()

    cursor.close()
    conn.close()
    return render_template_string(HTML_TEMPLATE, notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
