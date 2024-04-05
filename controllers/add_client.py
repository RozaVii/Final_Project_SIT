from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.add_client_models import add_client

@app.route('/add_client', methods=['get'])
def add_client():
    conn = get_db_connection()

    # нажата кнопка Добавить
    if request.values.get('client_full_name') and request.values.get('client_phone'):
        add_client(conn, request.values.get('client_full_name'), request.values.get('client_phone'))
     # выводим форму
    html = render_template(
     'add_client.html',
     len = len
    )
    return html