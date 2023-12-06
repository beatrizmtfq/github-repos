from models.models import get_users

def fetch_github_repos(username):
    try:
        repos = get_users(username)
        return {"repos": repos}
    except Exception as e:
        return {"error": str(e)}
