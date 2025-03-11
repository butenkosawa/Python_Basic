import pdfplumber
import os

os.chdir("C:\\Users\\SecAdmin\\PycharmProjects\\PythonBasic\\PDF\\cadastral_number")
pdf_files = os.listdir()
print(pdf_files)


data = []

for file in pdf_files:

    with pdfplumber.open(file) as pdf:
        page = pdf.pages[0]
        text = page.extract_text()
        data.append((text.split('\n')[-2].split()))

print(data)

# data = zip(pdf_files, data)

for i in range(len(data)):
    data[i][1] = float(data[i][1])

data = sorted(data, key= lambda x: x[1])

data_w = ''
for idx, cadastral in enumerate(data, 1):
    data_w += f'{idx} {cadastral}\n'

os.chdir('..\\')
print(data_w)

with open('cadastral.txt', 'w', encoding='utf-8-sig') as file:
    file.write(data_w)