import os
from flask import Flask,request,session,g,redirect,url_for
from werkzeug.utils import find_modules, import_string
from database import db_session, init_db

app = Flask(__name__)

def create_app(config=None):

    #app = Flask("bpet_login")
    app.config.update(dict(
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    ))
    app.config.update(config or {})
    app.config.from_envvar("BPET_SETTINGS", silent=True)

    register_blueprints(app)
    register_cli()
    register_teardowns()
    return app

def register_blueprints(app):
    for name in find_modules("login"):
        print("mod name: " + name)
        mod = import_string(name)
        if hasattr(mod, "bp"):
            app.register_blueprint(mod.bp, url_prefix="/login")

    return None

def register_cli():
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        print('Initialized the database begin...')
        init_db()
        print('Initialized the database. completed')

def register_teardowns():
    @app.teardown_appcontext
    def close_db(Exception=None):
        """Closes the database again at the end of the request."""
        db_session.remove()

#url part
@app.route("/")
def index():
    return redirect(url_for("login.login"))

if __name__ == "__main__":
    app = create_app()
    app.debug = True
    app.run()

