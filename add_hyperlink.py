import argparse
import os
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link

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
args = parser.parse_args()

# Fill the writer with the pages you want
reader = PdfReader(args.pdf_file)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Define hyperlinks and positions
# TODO: Read this from json input file
annotations = [
    {
        "rect": (461, 787, 566, 798),
        "url": "mailto:nicolausjanos.raag@iths.se",
    },
    {
        "rect": (461, 745, 524, 756),
        "url": "https://github.com/njrg",
    },
    {
        "rect": (461, 714, 558, 734),
        "url": "https://linkedin.com/in/nicolaus-janos-raag-65613a104",
    },
]

# Add the annotations (hyperlinks)
for a in annotations:
    annotation = Link(rect=a["rect"], url=a["url"])
    writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)
