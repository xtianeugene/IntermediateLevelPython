import requests

def convert(amount, frm, to):
    url = "https://api.frankfurter.app/latest"
    params = {"amount": amount, "from": frm, "to": to}
    r = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.json()["rates"][to]

if __name__ == "__main__":
    a = float(input("Amount: "))
    f = input("From (e.g., USD): ").upper()
    t = input("To (e.g., EUR): ").upper()
    print(f"{a} {f} = {convert(a, f, t):.2f} {t}")