import os
from bottle import run

from backend.handlers import app

run(app, host='0.0.0.0', port=os.environ.get('PORT', 5000))