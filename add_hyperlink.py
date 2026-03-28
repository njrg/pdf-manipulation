import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

# Fill the writer with the pages you want
pdf_path = os.path.join("./", "Raag_N-CV_sv.pdf")
reader = PdfReader(pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Define hyperlinks and positions
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
    annotation = AnnotationBuilder.link(rect=a["rect"], url=a["url"])
    writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)
