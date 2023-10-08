from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_login import LoginManager
from dotenv import load_dotenv
from os import environ


load_dotenv()

# Default Flask Initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{environ.get("DB_NAME")}'
db = SQLAlchemy(app)

login_manager = LoginManager(app)

if __name__ == "__main__":
    from views import views
    from auths.auth import auth_view
    # from test.test import tests
    
    app.register_blueprint(views, url_prefix='/amu3ze/')
    app.register_blueprint(auth_view, url_prefix='/auth/')
    # app.register_blueprint(tests, url_prefix='/test/')

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    @app.route('/')
    def index():
        return redirect(url_for("views.index"))

    
    app.run(debug=True)