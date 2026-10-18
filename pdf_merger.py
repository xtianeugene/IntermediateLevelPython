from PyPDF2 import PdfMerger

def merge(files, output):
    merger = PdfMerger()
    for f in files:
        merger.append(f)
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    files = input("PDF files (comma-separated): ").split(",")
    merge([f.strip() for f in files], "merged.pdf")
    print("Saved merged.pdf")