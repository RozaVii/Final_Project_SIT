from flask import Flask, session

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import controllers.coach
import controllers.client
import controllers.record
import controllers.add_client
import controllers.cancel_record
import controllers.add_service
