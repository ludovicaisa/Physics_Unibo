import nbformat
import nbconvert

files = [
    "leggi_pdb",
    "PCM_permute",
    "ER_networks",
    "real_net_analysis",
]

out_notebook = nbformat.v4.new_notebook()
for file in files:
    temp_notebook = nbformat.read('{}.ipynb'.format(file), as_version=4)
    out_notebook.cells.extend(temp_notebook.cells)

out_pdf = nbconvert.PDFExporter().from_notebook_node(out_notebook)[0]
with open('Complex_Networks.pdf', 'wb') as f:
    f.write(out_pdf)