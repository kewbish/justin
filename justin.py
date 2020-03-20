from dotenv import load_dotenv
from logging import debug
from os import getenv, popen, startfile, system
from requests import get
from sys import argv
from webbrowser import open_new
from terminaltables import SingleTable


def socials():
    open_new("https://mail.google.com/mail/u/0")
    open_new("https://discordapp.com/channels/@me")
    open_new("https://app.slack.com/client/TFFEQ2X61/CTUSAU05S")
    open_new("https://www.instagram.com/direct/inbox/")
    open_new("https://reddit.com/r/memes/rising")
    startfile(r"C:\Users\offic\Downloads\Dev\Tools\Shortcuts\Telegram.lnk")
    debug("Opened socials.")


def local():
    system("bash -c 'curl wttr.in?0'")
    cw = get("https://coronavirus-tracker-api.herokuapp.com/v2/latest").json()
    bc = get("https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=CA").json()
    cor_table = [["Latest", "World", "BC"],
                 ["Cases", cw['latest']['confirmed'],
                  bc['locations'][0]['latest']['confirmed']],
                 ["Deaths", cw['latest']['deaths'],
                  bc['locations'][0]['latest']['deaths']],
                 ["Recoveries", cw['latest']['recovered'],
                  bc['locations'][0]['latest']['recovered']]]
    print("\n")
    print(SingleTable(cor_table, title="Coronavirus Updates").table)
    system("bash -c 'cal'")
    print("\nCurrent time is:")
    system("time /t")
    debug("Opened local information.")


def news():
    load_dotenv(r"C:\Users\offic\Downloads\Dev\Justin\files\.env")
    key = getenv("NEWSAPI")
    news = get(f"http://newsapi.org/v2/top-headlines?country=ca&apiKey={key}").json()
    for a in news["articles"]:
        print(f"⚬ {a['title']} - {a['description']}")
    print("\nNews courtesy of the NewsAPI - https://newsapi.org")
    debug("Printed news to terminal.")


def github_issues():
    print("Currently, these are the issues you have open.")
    p = system("bash -c 'curl -u 'kewbish' https://api.github.com/issues'")
    debug("Opened issues.")


def github_init():
    gh_repo_name = argv[2]
    system("git init")
    system(f"git remote add https://github.com/kewbish/{gh_repo_name}.git")
    print(f"Setting up at: https://github.com/kewbish/{gh_repo_name}.git")
    system("git add . && github")
    debug("Set up repo.")


def help():
    print(r"""       _           _   _
      | |         | | (_)
      | |_   _ ___| |_ _ _ __
  _   | | | | / __| __| | '_ \
 | |__| | |_| \__ \ |_| | | | |_
  \____/ \__,_|___/\__|_|_| |_(_)
 """)
    options = [["Program", "What it does"],
               ["socials", "Opens fresh social media tabs."],
               ["local", "Bringing local information to terminal."],
               ["news", "Prints national news thru NewsAPI."],
               ["ghissues", "Notes open issues - req. auth."],
               ["ghinit", "Prepares Git repo for use."]]
    print(SingleTable(options, title="Here to help.").table)
    print("Usage: justin [program] [options]")


try:
    if len(argv) == 1:
        a = "help"
    else:
        a = argv[1].lower()
        args = argv[2:]
    if a == "socials":
        socials()
    elif a == "local":
        local()
    elif a == "news":
        news()
    elif a == "ghissues":
        github_issues()
    elif a == "ghinit":
        github_init()
    elif a == "help":
        help()
    else:
        help()
except IndexError:
    print("Error: Usage: justin [program] [options]")
