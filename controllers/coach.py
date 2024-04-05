from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.coach_model import get_coach, get_coach_record

@app.route('/', methods=['get'])
def index():
    conn = get_db_connection()

    # нажата кнопка Найти
    if request.values.get('coach'):
        coach_id = int(request.values.get('coach'))
        session['coach_id'] = coach_id
        date_start = request.values.get('date_start')
        date_end = request.values.get('date_end')

     # вошли первый раз
    else:
        session['coach_id'] = 1
        date_start = '2024-04-05'
        date_end = '2024-05-07'
    df_coach = get_coach(conn)
    df_coach_record = get_coach_record(conn, session['coach_id'], date_start, date_end)


     # выводим форму
    html = render_template(
     'index.html',
     coach_id = session['coach_id'],
     combo_box = df_coach,
     coach_record = df_coach_record,
     len = len
    )
    return html