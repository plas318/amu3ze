from models import User
from app import db
from werkzeug.security import check_password_hash, generate_password_hash

def user_create(email, password):
    exist_user = User.query.filter_by(email=email).first()
    
    if exist_user:
        print('Failed in creating user')
        return 'Failed in creating user'
    try:
        new_user = User(email=email, password= generate_password_hash(password, 'sha256'))
        db.session.add(new_user)
        db.session.commit()
        return True
    except:
        print('Failed creating new user')
        return 'Failed in creating user'
    
def user_authenticate(email, password):
    exist_user = User.query.filter_by(email=email).first()
    if exist_user:
        if check_password_hash(exist_user.password, password):
            return exist_user
    
    else:
        return False