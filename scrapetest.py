from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_title('https://www.iodine.com/drug/effexor')
if title == None:
    print("title is not found")

