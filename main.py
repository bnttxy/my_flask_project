# แก้บรรทัดบนสุด เพิ่ม url_for เข้ามา (จำเป็นต้องใช้ในการสร้างลิงก์)
from flask import Flask, render_template, url_for

# ... (ส่วน news_items และ index เหมือนเดิม) ...

# เพิ่มส่วนนี้ต่อท้ายสุด (ห้ามย่อหน้า)
@app.route('/news/<id>/')
def show_news_item(id):
    # ดึงข่าวตาม id ที่ส่งมา (ต้องแปลง id เป็น int ก่อนเพราะ url ส่งมาเป็น string)
    news_item = news_items[int(id)]
    
    # ส่งข้อมูล title และ body ไปให้ template ใหม่
    return render_template('news_item.html',
                           id=news_item['id'],
                           title=news_item['title'],
                           body=news_item['body'])