from app import app
from flask import render_template, request, session
#import sqlite3
from utils import get_db_connection
from models.add_service_model import add_service

@app.route('/add_service', methods=['get'])
def add_service():
    conn = get_db_connection()

    # нажата кнопка Добавить
    if request.values.get('service_name') and request.values.get('price'):
        add_service(conn, request.values.get('service_name'), request.values.get('price'))
    # выводим форму
    html = render_template(
        'add_service.html',
        len=len
    )
    return html