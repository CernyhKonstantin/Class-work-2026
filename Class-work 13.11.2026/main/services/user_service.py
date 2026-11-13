from django.contrib.auth import get_user_model
User = get_user_model()
def create_user(*, username, email, password, avatar=None):
    """Create and return a user; keep persistence logic in the service layer."""
    user = User(username=username, email=email, avatar=avatar)
    user.set_password(password)
    user.save()
    return user
