from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gizli_anahtar_buraya'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
db = SQLAlchemy(app)

class CayDurum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(100), nullable=False)
    cay_sayisi = db.Column(db.Integer, default=0)
    tarih = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cay-durumu', methods=['POST'])
def update_cay_durumu():
    data = request.json
    # Firebase yerine veritabanı işlemleri burada yapılacak
    return jsonify({"success": True})

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    # Geri bildirim işlemleri
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True) 