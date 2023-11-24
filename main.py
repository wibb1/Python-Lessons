import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


def get_filepaths(file_location):
    file_location = file_location + "*.xlsx"
    return glob.glob(file_location)


def build_header(pdf, filename):
    pdf.add_page()
    pdf.set_font(family='Times', size=16, style='B')
    invoice_info = filename.split('-')
    pdf.cell(w=50, h=8, txt="Invoice: " + invoice_info[0])
    pdf.cell(w=50, h=8, txt="Date: " + invoice_info[1])
    pdf.output(f"PDFs/{filename}.pdf")


if __name__ == '__main__':
    filepaths = get_filepaths("invoices/")

    for filepath in filepaths:
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        filename = Path(filepath).stem
        pdf = FPDF(orientation='P', unit="mm", format="A4")
        build_header(pdf, filename)
