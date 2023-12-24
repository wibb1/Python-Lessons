import glob
from fpdf import FPDF


def get_filepaths(directory):
    file_location = directory + "*.txt"
    return glob.glob(file_location)


def set_header(filepath, pdf):
    start = filepath.rfind('\\') + 1
    end = filepath.rfind(".txt")
    header = filepath[start:end].capitalize()
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=header, ln=1)


def set_text(data, pdf):
    pdf.set_font(family='Times', size=12, style='')
    pdf.multi_cell(w=0, h=8, txt=data)


def build_pdfs(directory):
    filepaths = get_filepaths(directory)
    pdf = FPDF(orientation='P', unit='mm', format="A4")
    for filepath in filepaths:
        pdf.add_page()
        file = open(filepath)
        set_header(filepath, pdf)
        set_text(file.read(), pdf)
    pdf.output(f"PDFs/animals.pdf")


if __name__ == '__main__':
    base_directory = 'text-files/'
    build_pdfs(base_directory)
