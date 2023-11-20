from flask import Flask, render_template, request, session
from dashboard.oauth import Oauth

# App configuration
app = Flask(__name__)
app.config["SECRET_KEY"] = "test123"


@app.route("/")
def home():
    """Home page"""
    return render_template("index.html", discord_url=Oauth.discord_login_url)


@app.route("/login")
def login():
    """Logins in with to discord with our oauth2 implentation"""
    code = request.args.get("code")
    print("here")
    at = Oauth.get_access_token(code)
    session["token"] = at

    user = Oauth.get_user_json(at)
    user_name = user.get("username")

    return f"Success, logged in as {user_name}"
