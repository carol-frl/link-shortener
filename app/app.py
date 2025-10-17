import os
import secrets
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24) # For flashing messages

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

# --- Database Initialization (Run once on startup) ---
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS links (
            id SERIAL PRIMARY KEY,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    cur.close()
    conn.close()
    print("Database initialized or already exists.")

# Call init_db once when the app starts
with app.app_context():
    init_db()

# --- Routes ---

@app.route('/', methods=('GET', 'POST'))
def index():
    short_url = None
    if request.method == 'POST':
        original_url = request.form['original_url']
        if not original_url:
            flash('URL is required!')
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            try:
                short_code = secrets.token_urlsafe(6) # Generate a 6-character unique code
                cur.execute(
                    "INSERT INTO links (original_url, short_code) VALUES (%s, %s) RETURNING short_code;",
                    (original_url, short_code)
                )
                short_code = cur.fetchone()[0]
                conn.commit()
                short_url = url_for('redirect_to_original', short_code=short_code, _external=True)
            except psycopg2.errors.UniqueViolation:
                flash('Generated short code was not unique. Please try again.')
                conn.rollback()
            except Exception as e:
                flash(f'An error occurred: {e}')
                conn.rollback()
            finally:
                cur.close()
                conn.close()
    return render_template('index.html', short_url=short_url)

@app.route('/<short_code>')
def redirect_to_original(short_code):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT original_url FROM links WHERE short_code = %s;", (short_code,))
    link = cur.fetchone()
    cur.close()
    conn.close()

    if link:
        return redirect(link[0])
    else:
        flash(f"Short URL '{short_code}' not found.")
        return redirect(url_for('index')) # Or render a 404 page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)