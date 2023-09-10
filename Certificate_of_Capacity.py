import tkinter as tk
from tkinter import filedialog
from datetime import datetime
from pdf_annotate import PdfAnnotator, Appearance, Location

# Ask user to select PDF
root = tk.Tk()
root.withdraw()
pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Ask user for date input
date_input = input("Please enter a date in DDMMYYYY format: ")

# Convert date input to datetime object
date = datetime.strptime(date_input, "%d%m%Y").strftime('%d/%m/%Y')
file_name = str(datetime.strptime(date_input, "%d%m%Y").strftime('%y.%m.%d')) + ' Certificate of Capacity.pdf'

# Assign Annotation File Path
annotator = PdfAnnotator(pdf_path)

# Create Date Annotation on Page 1
annotator.add_annotation(
    'text',
    Location(x1=330, y1=342, x2=430, y2=352, page=0),
    Appearance(content=str(date), font_size=10, fill = (0,0,0), fill_transparency = 1)
    )
# Create Date Annotation on Page 3
annotator.add_annotation(
    'text',
    Location(x1=330, y1=163, x2=430, y2=213, page=2),
    Appearance(content=str(date), font_size=10, fill = (0,0,0), fill_transparency = 1)
    )

# Write PDF
annotator.write(str(file_name))
