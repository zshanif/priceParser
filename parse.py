from download import Page
import re

class PriceParser:

    def __init__(self, pages):

        if type(pages) == Page:
            self.pages = [pages]
        elif type(pages) == list and all(map(lambda x: (True if type(x) == Page else False), pages)):
            self.pages = pages
        else:
            raise Exception("Invalid pages")

        self.data = [None] * len(self.pages)

    def parse(self):

        self.data = list(map(self.__parsePage__, self.pages))

    def __parsePage__(self, page):

        currencies = "£|$|€|₩|¥|₭|₮|₦|﷼|₽|฿|ƒ|ден|₡|₱"

        if not page.downloaded:
            page.download()

        if not page.content:
            return None

        ans = page.content

        m = len(re.findall(currencies, page.content.get_text()))

        for item in page:

            lm = len(re.findall(currencies, str(item)))

            if lm >= 0.75 * m:
                ans = item

        return ans


if __name__ == "__main__":

    # test
    import requests
    s = requests.Session()

    p = Page(s, "https://www.kent.ac.uk/accommodation/canterbury/accommodation-fees.html", True)
    parser = PriceParser([p])
    
    parser.parse()
    print(parser.data)
