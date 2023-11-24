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
    invoice_no, invoice_date = filename.split('-')
    pdf.cell(w=50, h=8, txt="Invoice: " + invoice_no, ln=1)
    pdf.cell(w=50, h=8, txt="Date: " + invoice_date, ln=1)


def add_table_headers(headers, pdf):
    headers = [sub.replace("_", " ").title() for sub in headers]
    pdf.cell(w=30, h=8, txt=str(headers[0]), border=1)
    pdf.cell(w=60, h=8, txt=str(headers[1]), border=1)
    pdf.cell(w=40, h=8, txt=str(headers[2]), border=1)
    pdf.cell(w=30, h=8, txt=str(headers[3]), border=1)
    pdf.cell(w=30, h=8, txt=str(headers[4]), border=1, ln=1)
    pdf.set_font(family='Times', size=10, style='')


def add_table_data(rows, pdf):
    total_price = 0
    for index, row in rows:
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)
        total_price += row['total_price']
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=60, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_price), border=1, ln=1)
    return total_price


def build_table(pdf, df):
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    add_table_headers(df.columns, pdf)
    return add_table_data(df.iterrows(), pdf)


def add_footer(total_price):
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=50, h=8, txt=f"The total price: {total_price}", ln=1)
    pdf.set_font(family='Times', size=10, style='B')
    pdf.cell(w=20, h=8, txt=f"PythonHow")
    pdf.image("images/pythonhow.png", w=10)


if __name__ == '__main__':
    filepaths = get_filepaths("invoices/")

    for filepath in filepaths:
        df = pd.read_excel(filepath, sheet_name="Sheet 1", header=0)
        filename = Path(filepath).stem
        pdf = FPDF(orientation='P', unit="mm", format="A4")
        build_header(pdf, filename)
        total_price = build_table(pdf, df)
        add_footer(total_price)
        pdf.output(f"PDFs/{filename}.pdf")
