from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from datetime import datetime

app = Flask(__name__)

# ข้อมูลข่าวจำลอง
news_items = {
    1: {'id': 1, 'title': 'COVID-19 update', 'body': 'This is a news on COVID-19'},
    2: {'id': 2, 'title': 'Facemasks found', 'body': 'Recent news on facemask production'},
    3: {'id': 3, 'title': 'Python 4', 'body': 'Python 4 will be out soon.... this is FAKE'},
}

@app.route('/')
def index():
    name = 'Somchai'
    time = datetime.now()
    # ส่งตัวแปร name และ time ไปด้วย ตามแบบฝึกหัด
    return render_template('index.html', 
                           name=name, 
                           time=time,
                           news_items=news_items.values())

@app.route('/news/<id>/')
def show_news_item(id):
    news_item = news_items[int(id)]
    return render_template('news_item.html',
                           id=news_item['id'],
                           title=news_item['title'],
                           body=news_item['body'])

# --- ส่วนที่เพิ่มมาใหม่สำหรับคลิปที่ 3 (ระบบสร้างข่าว) ---

def new_news_item(title, body):
    # หา ID ใหม่ (เอาค่ามากสุด + 1)
    new_id = max(news_items.keys()) + 1
    return {
        'id': new_id,
        'title': title,
        'body': body
    }

@app.route('/news/create/', methods=['POST'])
def create_news_item():
    # รับค่าจากฟอร์ม
    item = new_news_item(request.form['title'],
                         request.form['body'])
    # บันทึกลง dictionary
    news_items[item['id']] = item
    # บันทึกเสร็จแล้วดีดกลับไปหน้าแรก
    return redirect(url_for('index'))