import os
from bottle import run

from backend.handlers import app

if os.environ.get('APP_LOCATION') == 'heroku':
    run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(app, host='localhost', port=5000, debug=True)