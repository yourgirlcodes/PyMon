import os
from bottle import run

from backend.handlers import app
from backend.static_handlers import staticHandler
from backend.page_handlers import pageHandler


app.merge(staticHandler)
app.merge(pageHandler)
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=5000, debug=True)