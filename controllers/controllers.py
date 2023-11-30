from models.models import get_users


def get_users_route_handler(username):
    repos = get_users(username)
    return ({"repos":repos})
