import os

from flask import Flask
from flask import render_template

#Making the app
######################################################################
def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

######################################################################
#Home page
    @app.route("/")
    def index():
        return render_template("home_page.html")


#Page Second
    @app.route("/next_page")
    def next_page():
        
        return render_template("next.html")


    
#Making the app run
    return app


