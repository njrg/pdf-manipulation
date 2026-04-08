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
# json output file as optional (nargs='?') postitional argument with default value
parser.add_argument("json_file", help="path to output json file (default: \"annot_squares.json\")",
                    nargs='?', default="annot_squares.json")
args = parser.parse_args()

r = PdfReader(args.pdf_file) # read pdf file given as argument
p = r.pages[0] # read only first page
print(p.mediabox)

# If parsed pdf pages contain annotations of subtype square, print the coordinates
# and store them in the squares list variable (to be written to json later)
squares = []
if '/Annots' in p:
    for annot in p.annotations:
        obj = annot.get_object()
        if obj.get('/Subtype') == '/Square':
            # pypdf returns a FloatObject for \Rect with the coordinates of the
            # square, store it in the variable rect
            rect = obj.get('/Rect')
            # Append the values of rect for each square (on each run fo the for-loop)
            # to the square dictionary variable; As the FloatObject returned by pypdf
            # above is not directly JSON-serialisable we read its values as floats in
            # a list comprehension creating a list as dictionary value for the
            # "rect"-key; add url-key with placeholder string to be filled manually
            squares.append({
                "rect": [float(v) for v in rect],
                "url": "<++>"
            })

            # Print the information to STDOUT as well
            print("---")
            print(f"Subtype: {obj.get('/Subtype')}") # This will always be "/Square"
            print(f"Rect:    {rect}")


# Write coordinates of squares (rect) to the json output file
with open(args.json_file, 'w') as f:
    json.dump(squares, f, indent=4)

print(f"\nWrote {len(squares)} square annotation(s) to {args.json_file}.")
