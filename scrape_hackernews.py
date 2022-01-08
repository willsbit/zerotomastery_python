import pprint
import requests
from bs4 import BeautifulSoup

n_pages = input('Quantas páginas você quer scrapar?')
print('processando....')
url = 'https://news.ycombinator.com/news'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')


for i in range(2, int(n_pages) + 1):
    url_temp = f'https://news.ycombinator.com/news?p={i}'
    res = requests.get(url_temp)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(mega_links)
    # print(mega_subtext)
    mega_links = soup.select('.titlelink') + links
    mega_subtext = soup.select('.subtext') + subtext


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(mega_links, mega_subtext):
    hn = []
    for idx, item in enumerate(mega_links):
        title = mega_links[idx].getText()
        href = mega_links[idx].get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
