import PyPDF2 as pp2

r = pp2.PdfReader("annotated-pdf.pdf")
p = r.pages[0]
print(p.mediabox)

if '/Annots' in p:
    for annot in p.annotations:
        obj = annot.get_object()
        print("---")
        print(f"Subtype: {obj.get('/Subtype')}")
        print(f"Rect:    {obj.get('/Rect')}")
