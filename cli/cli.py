import colorama
import os
import sys
from typing import Optional
from colorama import Style, Fore
from string import Template
from cli import utils
colorama.init()

def generate_project(token: str = None, prefix: Optional[str] = "!", owner_id: int = None, support_id: int = None,
                           debug: Optional[bool] = True, client_id: Optional[str] = None, client_secret: Optional[str] = None,
                           oauth_url: Optional[str] = None, redirect_url: Optional[str] = None):
    """Generates a project with the given arguments

    Args:
        token (str, optional): Token of the bot. Defaults to None.
        prefix (Optional[str], optional): Prefix if the bot. Defaults to "!".
        owner_id (int, optional): Owner id of the bot. Defaults to None.
        support_id (int, optional): Server id of your support / testing server. Defaults to None.
        debug (Optional[bool], optional): Debug mode. Defaults to True.
        client_id (Optional[str], optional): Client id for oauth2. Defaults to None.
        client_secret (Optional[str], optional): Client secret for oauth2. Defaults to None.
        oauth_url (Optional[str], optional): Oauth2 invite url. Defaults to None.
        redirect_url (Optional[str], optional): Oauth2 redirect url. Defaults to None.
    """
    if client_id & client_secret & oauth_url & redirect_url is not None:
        utils.copy_and_rename("./dashboard.env", "./dashboard/.env")
        with open("./dashboard/.env", 'w+') as f:
            dash_temp = Template(f.read())
            dash_temp.substitute({
                "CI": client_id,
                "CS": client_secret,
                "OURL": oauth_url,
                "RURL": redirect_url
            })
    utils.copy_and_rename("./bot.env", "./bot/.env")
    with open("./bot/.env", 'w+') as f:
        bot_temp = Template(f.read())
        bot_temp.substitute({
            "TOKEN": token,
            "PRE": prefix,
            "OID": owner_id,
            "SID": support_id,
            "DEB": debug
        })

    
def main():
    """Takes in all the input for the user and generate the needed .env"""
    print(f"{Fore.RED}{Style.BRIGHT}Welcome to the Example-Bot cli, If you don't understand how to get anything, check out the HELP.md file.{Style.RESET_ALL}\n")
    dashboard = bool(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}First, do you want the dashboard enviorment setup? (True, False){Style.RESET_ALL}\n"))
    if dashboard:
        client_id = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot oauth2's client id? (Should be numbers){Style.RESET_ALL}\n"))
        client_secret = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot oauth2's client secret? (Should be numbers and letters){Style.RESET_ALL}\n"))
        oauth_url = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot oauth2's url invite? (Should be a a generated url){Style.RESET_ALL}\n"))
        redirect_url = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot oauth2's redirect url? (Should be a localhost url){Style.RESET_ALL}\n"))
    token = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot's token'? (Should be numbers and letters){Style.RESET_ALL}\n"))
    prefix = str(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot's command prefix? (Should be one or a few characters){Style.RESET_ALL}\n"))
    owner_id = int(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot's owner id? (Should be numbers){Style.RESET_ALL}\n"))
    support_id = int(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}What is your bot's support / testing server id? (Should be numbers){Style.RESET_ALL}\n"))
    debug = bool(input(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}Should the bot be in debug mode? (True, False){Style.RESET_ALL}\n"))
    
    if dashboard:
        generate_project(token, prefix, owner_id, support_id, debug, client_id, client_secret, oauth_url, redirect_url)
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}Your bot & dashboard is ready for usage!{Style.RESET_ALL}\n")
    else:
        generate_project(token, prefix, owner_id, support_id, debug)
        print(f"{Fore.LIGHTCYAN_EX}{Style.BRIGHT}[Example-Bot]-> {Fore.GREEN}Your bot is ready for usage!{Style.RESET_ALL}\n")