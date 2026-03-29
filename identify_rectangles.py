from PyPDF2 import PdfReader 

r = PdfReader("annotated-pdf.pdf")
p = r.pages[0]
print(p.mediabox)

if '/Annots' in p:
    for annot in p.annotations:
        obj = annot.get_object()
        print("---")
        print(f"Subtype: {obj.get('/Subtype')}")
        print(f"Rect:    {obj.get('/Rect')}")
