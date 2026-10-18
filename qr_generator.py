import qrcode

def make(data, filename="qr.png"):
    img = qrcode.make(data)
    img.save(filename)
    print("Saved:", filename)

if __name__ == "__main__":
    make(input("Text or URL: "))

