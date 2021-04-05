from bs4 import BeautifulSoup
import urllib.request as url

url_page = r"https://de.pons.com/%C3%BCbersetzung/deutsch-polnisch/kraft"

if __name__ == '__main__':
    with url.urlopen(url_page) as f:
        page_contents = f.read()
        page_contents = page_contents.decode('utf-8')
    # print(page_contents)
    # print(type(page_contents))

    soup = BeautifulSoup(page_contents, 'html.parser')
    # print(soup.prettify())
    for link in  soup.find_all('div', attrs={'class' : 'results'}):
        print(link)


