from app import lm
from .models import User

@lm.user_loader
def load_user(userid):
    return User.query.get(userid)
