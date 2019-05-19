from parse import Page, PriceParser
import requests

if __name__ == "__main__":

    # create global session
    s = requests.Session()

    # create Page object and download the url
    p = Page(s, "https://www.kent.ac.uk/accommodation/canterbury/accommodation-fees.html", True)

    # parser is initialized with a list of pages
    # alternatively, the parser can also take a page object
    parser = PriceParser([p])

    # run PriceParser.__parse__ on every page in the pages list
    # uses map
    parser.parse()

    # parsed prices stored in parser.data
    # .data is a list of the bottom-most recursive level of HTML Objects
    # containing price data. In order for .data to return a value, over
    # 75% of total Page price information must reside in a singular Object.
    print(parser.data)
