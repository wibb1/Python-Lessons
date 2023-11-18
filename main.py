import pandas as pd
import glob



def get_files(file_location):
    file_location = file_location + "*.xlsx"
    filepaths = glob.glob(file_location)

    for filepath in filepaths:
        df = pd.read_excel(filepath, sheet_name="Sheet 1")
        print(df)


if __name__ == '__main__':
    get_files("invoices/")
