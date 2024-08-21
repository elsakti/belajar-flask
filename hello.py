from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Halaman Home"

@app.route('/about')
def about():
    return "Tentang Kami"

@app.route('/user/<nama>')
def show_user_profile(nama):
    return f"Nama Saya {escape(nama)}"

@app.route('/membeli')
def membeli_barang():
    item = 'Kecap Asin'
    return f"Saya Akan Membeli {item}"
