import urllib.request
from html.parser import HTMLParser

class HeadlineParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_h2 = False
        self.headlines = []
    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.in_h2 = True
    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h2 = False
    def handle_data(self, data):
        if self.in_h2 and data.strip():
            self.headlines.append(data.strip())

if __name__ == "__main__":
    url = input("URL: ")
    html = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    p = HeadlineParser()
    p.feed(html)
    for h in p.headlines[:20]:
        print("-", h)