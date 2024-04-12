from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")

print(len(reader.pages))

page = reader.pages[len(reader.pages)]
print(page.extract_text())