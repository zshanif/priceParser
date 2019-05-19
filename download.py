import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class Page:

    def __init__(self, session, url, download = False):

        self.__session__ = session

        self.originalURL = url
        self.url = self.__genURL__()
        self.content = None
        self.downloaded = False

        if download:
            self.download()

    def download(self):

        try:
            request = self.__session__.get(self.originalURL)
            self.content = BeautifulSoup(request.content, "lxml")

        except:
            self.content = None

        self.downloaded = True

    def printContent(self):

        if self.content:
            print(self.content.prettify())
        else:
            print(None)

    def __genURL__(self):

        try:
            url = urlparse(self.originalURL)
            return "{}://{}{}".format(url.scheme, url.netloc, url.path)
        except:
            return ""

    def __iter__(self):

        if not self.content:
            return

        for item in self.content.descendants:
            yield item

    def __len__(self):

        if not self.content:
            return 0
        else:
            return len(list(self.content.descendants))


if __name__ == "__main__":

    # test
    s = requests.Session()
    p = Page(s, "https://www.kent.ac.uk/accommodation/canterbury/accommodation-fees.html", True)
    print(str(p.content).count("£"))
    # for i in p:
    #     print(i)
