from fpdf import FPDF
import pandas as pd


def add_header(pdf, text):
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=text, align='L', ln=1)
    pdf.line(10, 20, 200, 20)


def add_lines(pdf, start, end, line_height):
    for height in range(start, end, line_height):
        pdf.cell(w=0, h=24)
        pdf.line(10, height, 200, height)


def add_footer(pdf, text):
    pdf.set_y(-15)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=text, align='R')


def main():
    df = pd.read_csv("topics.csv")
    pdf = FPDF(orientation='portrait', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)

    for index, row in df.iterrows():
        # main page
        pdf.add_page()
        add_header(pdf, row['Topic'])
        add_lines(pdf, 30, 290, 10)
        add_footer(pdf, row['Topic'])

        # sub-pages
        for page in range(row['Pages'] - 1):
            pdf.add_page()
            add_lines(pdf, 20, 290, 10)
            add_footer(pdf, row['Topic'])

    pdf.output("output.pdf")


if __name__ == '__main__':
    main()
