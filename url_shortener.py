import hashlib, json, os

FILE = "urls.json"

def load():
     return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save(d):
     json.dump(d, open(FILE, "w"), indent=2)

def shorten(url):
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    d = load()
    d[short] = url
    save(d)
    return short

def resolve(code):
    return load().get(code)

if __name__ == "__main__":
    while True:
        c = input("1. Shorten 2. Resolve 3. Quit: ")
        if c == "1":
            print("Short code:", shorten(input("URL: ")))
        elif c == "2":
            print(resolve(input("Code: ")))
        else:
            break