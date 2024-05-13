import requests
from bs4 import BeautifulSoup, Comment

import sys

sys.path.append(".")

from util import save_password

url = "http://challenge01.root-me.org/web-serveur/ch1"

r = requests.get(url)

soup = BeautifulSoup(r.text, features="html.parser")

comments = soup.find_all(string=lambda e: isinstance(e, Comment))
comment = [c for c in comments if "password" in c][0]

result = comment.split("password : ")[-1]

dir = save_password(result, __file__)