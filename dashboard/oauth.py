import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Needed paramenters for the api
clientId = os.environ["CLIENT_ID"]
secret = os.environ["CLIENT_SECRET"]
login = os.environ["OAUTH_URL"]


class Oauth:
    """Used to simulate a oauth2 request which returns the user information"""

    client_id = clientId
    client_secret = secret
    redirect_uri = os.environ["REDIRECT_URL"]
    scope = "identify%20email%20guilds"
    discord_login_url = login
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"

    @staticmethod
    def get_access_token(code):
        payload = {
            "client_id": Oauth.client_id,
            "client_secret": Oauth.client_secret,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": Oauth.redirect_uri,
            "scope": Oauth.scope,
        }

        access_token = requests.post(url=Oauth.discord_token_url, data=payload).json()
        return access_token.get("access_token")

    @staticmethod
    def get_user_json(access_token):
        url = f"{Oauth.discord_api_url}/users/@me"
        headers = {"Authorization": f"Bearer {access_token}"}

        user_object = requests.get(url=url, headers=headers).json()
        return user_object
