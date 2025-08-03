from flask import Flask, request
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')  # ✅ Secure secret

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # In real apps, verify against hashed passwords in DB
    if username == 'admin' and password == os.environ.get('ADMIN_PASSWORD'):
        return 'Logged in!'
    return 'Invalid credentials!'

@app.route('/delete', methods=['POST'])
def delete():
    filename = request.form['filename']
    if '..' in filename or '/' in filename or '\' in filename:
        return 'Invalid file path!'
    try:
        os.remove(filename)
        return f'Deleted {filename}'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    debug = os.environ.get('DEBUG', 'False') == 'True'
    app.run(debug=debug)
