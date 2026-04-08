# PDF Manipulation

Small python scripts utilizing pypdf to manipulate/edit pdf files.

Right now there are:

- `identify_rectangles.py`
- `add_hyperlink.py`

Those two scripts are used together to add hyperlinks to a given PDF and require some
manual preparation/intervention to be functional.

## Usage

1. Open the PDF you want to add Hyperlinks to in a GUI application with annotations
   functionality, e.g. Okular
2. Draw square annotations at the positions where you want to add the hyperlinks,
   save (as second file) and exit
3. Run the `identify_rectangles.py` script with your square-annotated pdf file as
   pdf_input file.
    - The script will produce a json output file (default: `annot_squares.json`, but
      you can specify your own file name as second positional argument to the script)
    - The json-file contains dictionaries with two key-value pairs each, one with the
      coordinates that the script derived from the square annotations, one for the
      url of the hyperlink you want to add (with a placeholder value)
4. Open the json file in a text editor and replace the placeholders with the actual
   urls for the hyperlinks you want to add. Save and close the file.
5. Run the `add_hyperlink.py` script with the original pdf file as first positional
   argument (unless you want the squares as well, then you can use the
   square-annotated one) and the json-file containing the coordinates and urls of the
   hyperlinks you want to add as second positional argument (again it defaults to
   `annot_squares.json`)
    - The script will add hyperlink annotations at the coordinates of the
      corresponding squares
    - The output file is written to a pdf-file with the same name as the input
      pdf-file plus `_annot`, eg. `filename_annot.pdf`

## License

MIT — see [LICENSE](LICENSE)
