from bs4 import BeautifulSoup
import urllib.request as url
import requests as req

url_page = r"https://de.pons.com/%C3%BCbersetzung/deutsch-polnisch/menge"

if __name__ == '__main__':
    # with url.urlopen(url_page) as f:
    #     page_contents = f.read()
    #     page_contents = page_contents.decode('utf-8')
    page_contents = req.get(url_page).content

    # TODO: move pons parsing to another class

    soup = BeautifulSoup(page_contents, 'html.parser')

    for result_div in soup.find_all('div', attrs={'class': 'entry'}):
        header = result_div.find("h2", class_="")

        word = header.contents[0].strip()

        flexion = header.find('span', attrs={'class': 'flexion'}) or ""
        flexion = "".join(flexion.stripped_strings) if flexion != "" else ""

        object_case = header.find('span', attrs={'class': 'object-case'}) or ""
        object_case = "".join(object_case.stripped_strings) if object_case != "" else ""

        style = header.find('span', attrs={'class': 'style'}) or ""
        style = "".join(style.stripped_strings) if style != "" else ""

        genus = header.find('span', attrs={'class', 'genus'}) or ""
        genus = "".join(genus.stripped_strings) if genus != "" else ""

        wordclass = header.find('span', attrs={'class', 'wordclass'}) or ""
        wordclass = "".join(wordclass.stripped_strings) if wordclass != "" else ""

        print("-" * 75)
        print("Word=", word)
        print("Flexion=", flexion)
        print("Object case=", object_case)
        print("Style=", style)
        print("Genus=", genus)
        print("Wordclass=", wordclass)

        for entry in result_div.find_all('div', attrs={'class': 'translations'}):
            print("*" * 50)
            print(" ".join(entry.h3.stripped_strings))
            for link in entry.find_all('div', attrs={'class': 'target'}):
                for acronym in link.find_all('acronym'):
                    acronym.clear()

            for link in entry.find_all('div', attrs={'class': 'source'}):
                for acronym in link.find_all('acronym'):
                    acronym.clear()

            for data_target, data_source in zip(entry.find_all('div', attrs={'class': 'target'}),
                                                entry.find_all('div', attrs={'class': 'source'})):
                line = list()
                line.append(" ".join(data_target.stripped_strings).strip())
                line.append(" ".join(data_source.stripped_strings).strip())
                print(line)