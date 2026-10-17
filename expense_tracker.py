import csv, os
from datetime import date

FILE = "expenses.csv"

def add(amount, category, note=""):
    new = not os.path.exists(FILE)
    with open(FILE, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "amount", "category", "note"])
        w.writerow([date.today().isoformat(), amount, category, note])

def report():
    if not os.path.exists(FILE):
        print("No expenses yet.")
        return
    totals = {}
    with open(FILE, "r") as f:
        for row in csv.DictReader(f):
            totals[row["category"]] = totals.get(row["category"], 0) + float(row["amount"])
    for cat, total in totals.items():
        print(f"{cat}: {total:.2f}")

if __name__ == "__main__":
    while True:
        c = input("1. Add 2. Report 3. Quit: ")
        if c == "1":
            add(float(input("Amount: ")), input("Category:"))
        elif c == "2":
            report()
        else:
            break