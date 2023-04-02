import os
from pypdf import PdfMerger

files = [
    "simple_perceptron",
    "neuron_class",
    "scikit_intro",
]

merger = PdfMerger()

for file in files:
    os.system("jupyter nbconvert --to pdf {}.ipynb".format(file))
    merger.append("{}.pdf".format(file))
    os.remove("{}.pdf".format(file))

merger.write("Pattern_Recognition.pdf")
merger.close()