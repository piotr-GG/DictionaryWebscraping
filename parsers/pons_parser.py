from parser_base import ParserBaseClass
from bs4 import BeautifulSoup
import urllib.request as url

url_page = r"https://de.pons.com/%C3%BCbersetzung/deutsch-polnisch/kraft"


class PonsParser(ParserBaseClass):
    def __init__(self):
        super().__init__()

    def parse(self):
        pass


if __name__ == '__main__':
    with url.urlopen(url_page) as f:
        page_contents = f.read()
        page_contents = page_contents.decode('utf-8')

    # TODO: move pons parsing to another class

    soup = BeautifulSoup(page_contents, 'html.parser')
    for result_div in soup.find_all('div', attrs={'class': 'entry'}):
        header = result_div.find("h2", class_="")

        # header_data = [str(el.string).strip() for el in header.contents]

        word = header.contents[0].strip()
        flexion = header.find('span', attrs={'class': 'flexion'}) or ""
        if flexion != "":
            flexion = "".join(flexion.stripped_strings)
        object_case = header.find('span', attrs={'class': 'object-case'}) or ""
        if object_case != "":
            object_case = "".join(object_case.stripped_strings)
        style = header.find('span', attrs={'class': 'style'}) or ""
        if style != "":
            style = "".join(style.stripped_strings)
        genus = header.find('span', attrs={'class', 'genus'}) or ""
        if genus != "":
            genus = "".join(genus.stripped_strings)
        wordclass = header.find('span', attrs={'class', 'wordclass'}) or ""
        if wordclass != "":
            wordclass = "".join(wordclass.stripped_strings)

        print("-" * 75)
        print("Word=", word)
        print("Flexion=", flexion)
        print("Object case=", object_case)
        print("Style=", style)
        print("Genus=", genus)
        print("Wordclass=", wordclass)

        # print("Header data =", header_data)
        # print("Header data len=", len(header_data))

        for link in result_div.find_all('div', attrs={'class': 'target'}):
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
