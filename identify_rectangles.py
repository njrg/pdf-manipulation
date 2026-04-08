from pypdf import PdfReader 
import argparse, os
import json

# Function to check that file given as argument acutally exists
def existing_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"File not found: {path}")
    return(path)

# Give the pdf file as command line argument
# using argparse
parser = argparse.ArgumentParser()
# add pdf_file as positional argument (with help-text), type parameter calls
# existing_file function during parsing to check that file actually exists
parser.add_argument("pdf_file", help="path to pdf file", type=existing_file)
args = parser.parse_args()

r = PdfReader(args.pdf_file) # read pdf file given as argument
p = r.pages[0] # read only first page
print(p.mediabox)

# TODO: skriv output till json-file, men bara for subtype "/Square"
if '/Annots' in p:
    for annot in p.annotations:
        obj = annot.get_object()
        if obj.get('/Subtype') == '/Square':
            print("---")
            print(f"Subtype: {obj.get('/Subtype')}")
            print(f"Rect:    {obj.get('/Rect')}")
