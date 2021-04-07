from bs4 import BeautifulSoup
import urllib.request as url

url_page = r"https://de.pons.com/%C3%BCbersetzung/deutsch-polnisch/kraft"

if __name__ == '__main__':
    with url.urlopen(url_page) as f:
        page_contents = f.read()
        page_contents = page_contents.decode('utf-8')

    # TODO: ADD THE HEADERS FROM PONS!!!

    soup = BeautifulSoup(page_contents, 'html.parser')
    for link in soup.find_all('div', attrs={'class': 'target'}):
        for acronym in link.find_all('acronym'):
            # print(acronym)
            acronym.clear()

        line = []
        for txt in link.stripped_strings:
            line.append(txt)
        print(" ".join(line))

    for link in soup.find_all('div', attrs={'class': 'source'}):
        for acronym in link.find_all('acronym'):
            acronym.clear()
        line = []
        for txt in link.stripped_strings:
            line.append(txt)
        print(" ".join(line))

        # print(link)
        # print("-" * 70)
        # for txt in link.stripped_strings:
        #     print(txt, end=" ")
        # print("")
        # for ahref in link.find_all('a'):
        #     print(ahref.string, sep=" ")
