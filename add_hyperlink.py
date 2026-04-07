import argparse
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link

# Parse command line arguments for input pdf file (given as required positional
# argument) 
parser = argparse.ArgumentParser()
parser.add_argument("pdf_file", help="path to pdf file")
args = parser.parse_args()

pdf_path = args.pdf_file
# TODO: Make sure the file actually exists in the file system (use os)
# compare old code for path construction:
#pdf_path = os.path.join("./", "inputfile.pdf")

# Fill the writer with the pages you want
reader = PdfReader(pdf_path)
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
