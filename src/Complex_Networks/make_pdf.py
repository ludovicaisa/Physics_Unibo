import os
from pypdf import PdfMerger

files = [
    "ER_networks",
]

merger = PdfMerger()

for file in files:
    os.system("jupyter nbconvert --to pdf {}.ipynb".format(file))
    merger.append("{}.pdf".format(file))
    os.remove("{}.pdf".format(file))

merger.write("Complex_Networks.pdf")
merger.close()