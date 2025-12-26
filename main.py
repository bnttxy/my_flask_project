from flask import Flask, render_template

app = Flask(__name__)

# 1. เพิ่มข้อมูลข่าวด้านบน (จำลอง Database)
news_items = {
    1: {'id': 1, 'title': 'COVID-19 update', 'body': 'This is a news on COVID-19'},
    2: {'id': 2, 'title': 'Facemasks found', 'body': 'Recent news on facemask production'},
    3: {'id': 3, 'title': 'Python 4', 'body': 'Python 4 will be out soon.... this is FAKE'},
}

@app.route("/")
def index():
    # 2. ส่งข้อมูลข่าว (news_items.values()) ไปที่ template
    return render_template('index.html', news_items=news_items.values())