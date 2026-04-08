import argparse, os
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
import json
from pprint import pprint

# Function to check that file given as argument acutally exists
def existing_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"File not found: {path}")
    return(path)

# Parse command line arguments for input pdf file (given as required positional
# argument) 
parser = argparse.ArgumentParser()
# add pdf_file as positional argument (with help-text), type parameter calls
# existing_file function during parsing to check that file actually exists
parser.add_argument("pdf_file", help="path to pdf file", type=existing_file)
# json input file containing coordinates and corresponding links/urls, optional
# (nargs='?') postitional argument, default value, check taht file actually exists
parser.add_argument("json_file", help="path to input json file (default: \"annot_squares.json\")",
                    nargs='?', default="annot_squares.json", type=existing_file)
args = parser.parse_args()

# Fill the writer with the pages you want
reader = PdfReader(args.pdf_file)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Read hyperlinks and positions from json input file
# (containing two key-value pairs per entry, "rect" with the list-value containing
# the four corners coordinates, and the "url" key
with open(args.json_file, 'r') as fj:
    annotations = json.load(fj) # load the json data into a dictionary

print(f"The following hyperlinks will be added at the corresponding positions in \"{args.pdf_file}\"")
print()
pprint(annotations)

# Add the annotations (hyperlinks)
for a in annotations:
    annotation = Link(rect=a["rect"], url=a["url"])
    writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
# Derive name of output file from input file (with "_annot" added)
# Split input file into basename and extension
base, ext = os.path.splitext(args.pdf_file)
output_path = f"{base}_annot{ext}"

with open(output_path, "wb") as fp:
    writer.write(fp)
