from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_login import LoginManager
DB_NAME = 'amu3ze.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = "cb69a3368e03cb8df685b0c5a54582a9"
app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)


login_manager = LoginManager(app)





@app.route('/')
def index():
    return redirect(url_for("views.index"))



if __name__ == "__main__":
    from views import views
    from auths.auth import auth_view
    
    app.register_blueprint(views, url_prefix='/amu3ze/')
    app.register_blueprint(auth_view, url_prefix='/auth/')
    
    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.run(debug=True, port=5000)