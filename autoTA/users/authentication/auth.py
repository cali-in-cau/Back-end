from users.models import User

def get_user_info(user_email):
    user = User.objects.get(email=user_email)
    return user

def valid_user(user_email):
    user = User.objects.filter(email=user_email)
    if(user.exists()):
        return True
    else:
        return False

def register(user_email):
    if valid_user(user_email):
        return False
    user = User(email=user_email)
    user.save()
    return True