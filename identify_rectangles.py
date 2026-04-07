from pypdf import PdfReader 
import argparse

# Give the pdf file as command line argument
# using argparse
parser = argparse.ArgumentParser()
# add pdf_file as positional argument (with help-text)
parser.add_argument("pdf_file", help="path to pdf file")
args = parser.parse_args()

r = PdfReader(args.pdf_file) # read pdf file given as argument
p = r.pages[0] # read only first page
print(p.mediabox)

# TODO: skriv output till json-file, men bara for subtype "/Square"
if '/Annots' in p:
    for annot in p.annotations:
        obj = annot.get_object()
        print("---")
        print(f"Subtype: {obj.get('/Subtype')}")
        print(f"Rect:    {obj.get('/Rect')}")
